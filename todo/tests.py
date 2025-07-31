from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Todo

class TodoTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.todo = Todo.objects.create(
            user=self.user,
            title='Test Todo',
            description='Test Description',
            status='pending'
        )

    def test_todo_list_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Todo')

    def test_todo_creation(self):
        self.client.login(username='testuser', password='testpass123')
        initial_count = Todo.objects.count()  # Get count before creation
        
        response = self.client.post(reverse('todo_list'), {
            'title': 'New Test Todo',
            'description': 'New Description',
            'status': 'pending'
        })
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Todo.objects.count(), initial_count + 1)  # Should have one more todo
        new_todo = Todo.objects.latest('created_at')  # Get the most recently created
        self.assertEqual(new_todo.title, 'New Test Todo')