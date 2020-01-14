from django.test import TestCase
from .models import Post
from django.urls import reverse


class PostModelTest(TestCase):
    

    def setUp(self):
        Post.objects.create(text='test case')


    def test_text_content(self):
        post = Post.objects.get(id=1)
        expectd_object_name = f'{post.text}'
        self.assertEqual(expectd_object_name,'test case') 

class HomePAgeViewTest(TestCase):

    def setUp(self):
        Post.objects.create(text = 'an other test')
        

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code , 200)
    
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp,'home.html')