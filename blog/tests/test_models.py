from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post


class TestModel(TestCase):
    def test_published_manager_works(self):
        user = User.objects.create_user("user1", "pw432joij")
        Post.objects.create(title='Another post1', slug='another-post1', body='Post body.', author=user, status='published')
        Post.objects.create(title='Another post2', slug='another-post2', body='Post body.', author=user)
        Post.objects.create(title='Another post3', slug='another-post3', body='Post body.', author=user, status='published')
        self.assertEqual(len(Post.published.all()), 2)


