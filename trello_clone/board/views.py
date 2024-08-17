from django.shortcuts import render, get_object_or_404, redirect
from .models import Board, Card, List
from .forms import CardForm

# View for displaying the details of a specific board
def board_detail(request, pk):
    board = get_object_or_404(Board, pk=pk)
    lists = board.lists.all()
    
    if request.method == 'POST':
        card_id = request.POST.get('card_id')
        new_list_id = request.POST.get('new_list_id')

        if card_id and new_list_id:
            card = get_object_or_404(Card, pk=card_id)
            new_list = get_object_or_404(List, pk=new_list_id)
            card.list = new_list
            card.save()

        return redirect('board_detail', pk=pk)

    return render(request, 'board/board_detail.html', {'board': board, 'lists': lists})

# View for handling card movement via AJAX
def move_card(request):
    if request.method == 'POST':
        card_id = request.POST.get('card_id')
        list_id = request.POST.get('list_id')

        if card_id and list_id:
            card = get_object_or_404(Card, id=card_id)
            new_list = get_object_or_404(List, id=list_id)

            card.list = new_list
            card.save()

            # Redirect back to the board detail page
            return redirect('board_detail', pk=card.list.board.pk)
    return redirect('board_detail', pk=request.POST.get('board_id', 1))  # Default to board 1 if board_id is not found

# View for adding a new card to a list
def add_card(request, list_id):
    list_instance = get_object_or_404(List, id=list_id)
    
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.list = list_instance  # Set the list instance here
            card.save()
            return redirect('board_detail', pk=list_instance.board.pk)
    else:
        form = CardForm()

    return render(request, 'board/add_card.html', {'form': form, 'list': list_instance})
