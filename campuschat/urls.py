"""
URL configuration for campuschat project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from chat.views import (
    chat_home,
    users_list,
    private_chat,
    meeting_room,
    upload_meeting_file,
    meeting_files_list,
    download_meeting_file,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "login/",
        auth_views.LoginView.as_view(template_name="login.html"),
        name="login",
    ),

    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    path("users/", users_list, name="users_list"),
    path("chat/<int:user_id>/", private_chat, name="private_chat"),

    path("meeting/<slug:room_name>/", meeting_room, name="meeting_room"),

    path(
        "meeting/<slug:room_name>/files/upload/",
        upload_meeting_file,
        name="upload_meeting_file",
    ),

    path(
        "meeting/<slug:room_name>/files/",
        meeting_files_list,
        name="meeting_files_list",
    ),

    path(
        "meeting/<slug:room_name>/files/<int:file_id>/download/",
        download_meeting_file,
        name="download_meeting_file",
    ),

    path("", chat_home, name="chat_home"),
]

