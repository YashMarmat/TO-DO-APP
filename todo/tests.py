
from django.test import TestCase
from django.urls import reverse
from todo.models import Schedule


class ScheduleTest(TestCase):

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
    
