from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home(request):
    # Redirect to a specific board if it exists, or handle as needed
    return redirect('board_detail', pk=1)  # Ensure a board with pk=1 exists

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Define the root URL pattern
    path('boards/', include('board.urls')),  # Include board app URLs
]
