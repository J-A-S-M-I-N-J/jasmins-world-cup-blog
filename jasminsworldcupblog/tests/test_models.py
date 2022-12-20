from django.test import TestCase
from ..models import Post
from ..forms import PostForm

def test_title_is_required(self):
        """
        Test if form submits with empty title field
        """
        form = PostForm({
            'title': '',
            'author': 'test',
            'content': 'test',
        })
        # Form should not be valid - name required
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['title'][0], 'This field is required.')