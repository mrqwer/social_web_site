from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.GetCustomUserView.as_view())
]