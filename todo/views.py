from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm, SignUpForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    form = TodoForm()
    
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo_list')
    
    context = {
        'todos': todos,
        'form': form,
    }
    return render(request, 'todo/todo_list.html', context)

@login_required
def update_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    
    context = {
        'form': form,
        'todo': todo,
    }
    return render(request, 'todo/update_todo.html', context)

@login_required
def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo/delete_todo.html', {'todo': todo})

@login_required
def toggle_todo_status(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.status = 'completed' if todo.status == 'pending' else 'pending'
    todo.save()
    return redirect('todo_list')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todo_list')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def logout(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('todo_list')