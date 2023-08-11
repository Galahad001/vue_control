from django.urls import path
from . import views

urlpatterns = [
    path('api/book/v1/', views.APIView, name='apiTest'),
    path('api/book/<int:pk>/', views.APIView_datail, name='datail')
]