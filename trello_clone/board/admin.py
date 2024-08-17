from django.contrib import admin
from .models import Board, List, Card

# Register the Board model
@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Register the List model
@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('name', 'board')

# Register the Card model
@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('title', 'list')
