
from django.test import TestCase
from django.urls import reverse
from todo.models import Schedule
from django.http import HttpRequest
from todo.views import CreateView, UpdateView, DeleteView


class TestUrls(TestCase):

    def test_home_page_status_code(self): # homepage contains the list of topics or schedules
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_schedule_create_status_code(self):
        response = self.client.get(reverse('schedule_create'))
        self.assertEquals(response.status_code, 200)

    def test_home_page_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_create_page_uses_correct_templates(self):
        response = self.client.get(reverse('schedule_create'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'schedule_create.html')


class TestModel(TestCase):

    def setUp(self):  # created a new schedule or topic
        self.post = Schedule.objects.create(
            topic = 'any topic'
            )

    def test_todo_model_content(self):
        self.assertEqual(f'{self.post.topic}', 'any topic')

    def test_todo_model_content_using_id(self):
        data = Schedule.objects.get(id=1)
        expected_result = f'{data.topic}'
        self.assertEquals(expected_result, 'any topic')
    
    # Note: there is no detail page in this project thats why i didnt test that

    def test_create_new_schedule(self):
        request = self.client.post(reverse('schedule_create'),{
            'topic': 'new schedule',
        })
        self.assertEqual(request.status_code, 302)  # 302 beacuse, reverse_lazy('home') views.py
    

    def test_schedule_update_view(self): # new
        response = self.client.post(reverse('schedule_update', args='1'), {
            'topic': 'Updated title',
            })
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self): # new
        response = self.client.post(reverse('schedule_delete', args='1'))
        self.assertEqual(response.status_code, 302)


# Note: 302
# This status occurs when a resource or page you're attempting
# to load has been temporarily moved to a different location
    
