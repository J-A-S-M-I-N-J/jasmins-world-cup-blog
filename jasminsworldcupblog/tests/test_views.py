from django.test import TestCase
from ..models import Post
from django.contrib.auth.models import User
from django.urls import reverse
import os
from django.conf import settings
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

def test_home_page_test(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

def test_that_post_detail_view_loads(self):
    author = User(username="author", password='author*12345')
    author.save()
    post = Post.objects.create(
        title='xxx',
        author=author,
        content='post content',
        status=1
    )
    url = reverse('post_detail', kwargs={"slug": post.slug})
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'post_detail.html')

