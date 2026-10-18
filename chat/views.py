from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Message,SharedFile
from django.contrib.auth.models import User
from django.http import JsonResponse, FileResponse, Http404
from django.views.decorators.http import require_POST
from django.core.exceptions import ValidationError
from django.utils.text import get_valid_filename

@login_required
def chat_home(request):
    return render(request, "chat.html")


@login_required
def users_list(request):
    users = User.objects.exclude(username=request.user.username)

    return render(request, "users.html", {
        "users": users
    })

@login_required
def private_chat(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    if other_user == request.user:
        return redirect("users_list")
    messages = Message.objects.filter(
        sender__in=[request.user, other_user],
        receiver__in=[request.user, other_user]
    ).order_by("timestamp")

    return render(request, "chat.html", {
        "other_user": other_user,
        "messages": messages
    })
@login_required
def meeting_room(request, room_name):
    return render(request, "meeting.html", {
        "room_name": room_name
    })

@login_required
@require_POST
def upload_meeting_file(request, room_name):
    uploaded_file = request.FILES.get("file")

    if not uploaded_file:
        return JsonResponse(
            {"error": "Please choose a file first."},
            status=400
        )

    # Limit uploads to 10 MB
    if uploaded_file.size > 10 * 1024 * 1024:
        return JsonResponse(
            {"error": "File size must not exceed 10 MB."},
            status=400
        )

    original_name = get_valid_filename(
        uploaded_file.name.replace("\\", "/").split("/")[-1]
    )

    if not original_name:
        return JsonResponse(
            {"error": "Invalid filename."},
            status=400
        )

    shared_file = SharedFile.objects.create(
        sender=request.user,
        room_name=room_name,
        file=uploaded_file,
        original_name=original_name
    )

    return JsonResponse({
        "message": "File uploaded successfully.",
        "file": {
            "id": shared_file.id,
            "name": shared_file.original_name,
            "sender": request.user.username,
            "url": f"/meeting/{room_name}/files/{shared_file.id}/download/"
        }
    })


@login_required
def meeting_files_list(request, room_name):
    files = SharedFile.objects.filter(
        room_name=room_name
    ).select_related("sender").order_by("-uploaded_at")

    return JsonResponse({
        "files": [
            {
                "id": item.id,
                "name": item.original_name,
                "sender": item.sender.username,
                "url": f"/meeting/{room_name}/files/{item.id}/download/"
            }
            for item in files
        ]
    })


@login_required
def download_meeting_file(request, room_name, file_id):
    shared_file = get_object_or_404(
        SharedFile,
        id=file_id,
        room_name=room_name
    )

    try:
        response = FileResponse(
            shared_file.file.open("rb"),
            as_attachment=True,
            filename=shared_file.original_name
        )
        return response
    except (FileNotFoundError, ValueError):
        raise Http404("File not found.")


