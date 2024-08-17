from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.board_detail, name='board_detail'),
    path('move-card/', views.move_card, name='move_card'),
    path('add-card/<int:list_id>/', views.add_card, name='add_card'),
]
