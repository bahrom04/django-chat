from django.contrib import admin
from django.urls import path, include
from chat import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("chat/", include("chat.urls")),
    path("messages/", views.MessageListView.as_view()),
]
