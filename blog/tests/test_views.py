from django.test import TestCase
from django.urls import reverse
from blog.models import Post
from django.contrib.auth.models import User
from django.utils import timezone
from blog import views


class TestViews(TestCase):
    
    def test_post_list_page_returns_published(self):
        user = User.objects.create_user("user1", "pw432joij")
        Post.objects.create(title='Another post1', slug='another-post1', body='Post body.', author=user, status='published')
        Post.objects.create(title='Another post2', slug='another-post2', body='Post body.', author=user)
        Post.objects.create(title='Another post3', slug='another-post3', body='Post body.', author=user, status='published')
        response = self.client.get(reverse("blog:post_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My Blog")
        post_list = Post.published.all().order_by('-publish',)
        #self.assertEqual(list(response.context["object_list"]), list(post_list),)
        self.assertEqual(list(response.context["posts"]), list(post_list),)

    def test_post_detail_page_returns_published(self):
        user = User.objects.create_user("user1", "pw432joij")
        Post.objects.create(title='Another post4', slug='another-post4', body='Post body.', author=user, status='published')
        date = timezone.now()        
        response = self.client.get(reverse('blog:post_detail', args=[date.year, date.month, date.day, 'another-post4']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Another post4")

    def test_post_detail_page_not_published(self):
        user = User.objects.create_user("user1", "pw432joij")
        Post.objects.create(title='Another post5', slug='another-post5', body='Post body.', author=user)
        date = timezone.now()        
        response = self.client.get(reverse('blog:post_detail', args=[date.year, date.month, date.day, 'another-post5']))
        self.assertEqual(response.status_code, 404)

    def test_share_email_post_page_works(self):
        user = User.objects.create_user("user1", "pw432joij")
        post = Post.objects.create(title='Another post1234', slug='another-post1234', body='text...', author=user, status='published') 
        response = self.client.get(reverse('blog:post_share', args=[post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Another post1234")


    def test_post_search_works(self):
        user = User.objects.create_user("user1", "pw432joij")
        post1 = Post.objects.create(title='Post 1', slug='post-1', body='This is text of post1', author=user, status='published')
        post1 = Post.objects.create(title='Post 2', slug='post-2', body='This is text of post2', author=user) 
        post1 = Post.objects.create(title='Post 3', slug='post-3', body='This is text of post3', author=user, status='published')
        query = 'post1'
        response = self.client.get('{}?query={}'.format(reverse('blog:post_search'), query))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Post 1")
        self.assertNotContains(response, "Post 2")



