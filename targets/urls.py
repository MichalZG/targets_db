from django.urls import path
from targets import views

urlpatterns = [
    path('targets/', views.target_list),
    path('targets/<int:pk>/', views.target_detail),
]