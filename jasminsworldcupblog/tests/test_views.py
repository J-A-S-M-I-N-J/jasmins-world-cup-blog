from django.test import TestCase
from ..models import Post
from django.contrib.auth.models import User
from django.urls import reverse
import os
from django.conf import settings
from django.contrib.auth import get_user_model

class TestView(TestCase):

    def home_page_test(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_that_post_detail_view_loads(self):
        post = Post.objects.create(
            topic=self.topic, title='xxx',
            
        url = reverse('post_detail', kwargs={"pk": 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')

    def superuser_can_add_a_post(self):
        # tutor service of CodeInstitute helped with
        # logging in the user and with uploading the image

        # login
        logged_in = self.client.login(
            username=self.is_superuser¶[0]['username'],
            password=self.is_superuser¶[0]['password'])

        # check we are indeed logged in
        self.assertTrue(logged_in)

        # make post request
        response = self.client.post('/add_item/', {
            'title': title.objects.first().id,
            'title': 'xxx',
    
        })

        # check response and status code
        self.assertEquals(response.status_code, 302)

        # check that new post has been made
        posts = Post.objects.filter(title='xxx')
        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0].title, 'xxx')

    def superuser_can_delete_post(self):
        # tutor service of CodeInstitute helped with
        # logging in the user and with uploading the image

        # login
        logged_in = self.client.login(
            username=self.is_superuser¶[0]['username'],
            password=self.is_superuser¶[0]['password'])

        # check we are indeed logged in
        self.assertTrue(logged_in)

        post = Post.objects.create(
            title=self.title, title='xxx',
        url = reverse('post_delete', kwargs={"pk": 1})
        response = self.client.post(url)

        # check that new post has been made
        posts = Post.objects.filter(title='xxx')
        self.assertEqual(len(posts), 0)

        # make post request
        response = self.client.post('/delete_item/1/', {
            'title': title.objects.first().id,
            'title': 'xxx',
    
        })

        # check redirect
        self.assertRedirects(response, '/')

        # check that new post has been made
        posts = Post.objects.filter(title='xxx')
        self.assertEqual(len(posts), 0)

    

  