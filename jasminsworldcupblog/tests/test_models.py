from django.test import TestCase
from ..models import Post

class TestModels(TestCase):

    def test_that_post_is_created_properly(self):
        title = title.objects.create(name="xxx")
        self.assertEqual(topic.name, "xxx")
