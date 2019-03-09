from django.test import TestCase
from django.urls import reverse
from blog.models import Post, Comment
from django.contrib.auth.models import User
from django.utils import timezone


class TestTemplatetags(TestCase):
    
    def test_total_posts_templatetags_works(self):
        user = User.objects.create_user("user1", "pw432joij")
        Post.objects.create(title='Another post1', slug='another-post1', body='Post 1 body.', author=user, status='published')
        Post.objects.create(title='Another post2', slug='another-post2', body='Post 2 body.', author=user)
        Post.objects.create(title='Another post3', slug='another-post3', body='Post 3 body.', author=user, status='published')
        response = self.client.get(reverse("blog:post_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "I've written 2 posts so far.")
        self.assertNotContains(response, "I've written 3 posts so far.")

    def test_show_latest_posts_templatetags_works(self):
        user = User.objects.create_user("user1", "pw432joij")
        Post.objects.create(title='Another post1', slug='another-post1', body='Post 1 body.', author=user, status='published')
        Post.objects.create(title='Another post2', slug='another-post2', body='Post 2 body.', author=user)
        Post.objects.create(title='Another post3', slug='another-post3', body='Post 3 body.', author=user, status='published')
        Post.objects.create(title='Another post4', slug='another-post4', body='Post 4 body.', author=user, status='published')
        Post.objects.create(title='Another post5', slug='another-post5', body='Post 5 body.', author=user)
        Post.objects.create(title='Another post6', slug='another-post6', body='Post 6 body.', author=user, status='published')
        response = self.client.get(reverse("blog:post_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Another post1")
        self.assertNotContains(response, "Another post2")
        self.assertContains(response, "Another post3")
        self.assertContains(response, "Another post4")
        self.assertNotContains(response, "Another post5")
        self.assertContains(response, "Another post6")
        self.assertTemplateUsed(response, 'blog/post/list.html')
        self.assertTemplateUsed(response, 'blog/post/latest_posts.html')

    def test_get_most_commented_posts_templatetags_works(self):
        user = User.objects.create_user("user1", "pw432joij")
        post1 = Post.objects.create(title='Another post1', slug='another-post1', body='Post 1 body.', author=user, status='published')
        post2 = Post.objects.create(title='Another post2', slug='another-post2', body='Post 2 body.', author=user)
        post3 = Post.objects.create(title='Another post3', slug='another-post3', body='Post 3 body.', author=user, status='published')
        post4 = Post.objects.create(title='Another post4', slug='another-post4', body='Post 4 body.', author=user, status='published')
        post5 = Post.objects.create(title='Another post5', slug='another-post5', body='Post 5 body.', author=user)
        post6 = Post.objects.create(title='Another post6', slug='another-post6', body='Post 6 body.', author=user, status='published')
        Comment.objects.create(post=post1, name='Vasya', email='vasya@vasya.com', body='Comment body...', active=True)
        Comment.objects.create(post=post2, name='Anna', email='anna@anna.com', body='Comment body...', active=True)
        response = self.client.get(reverse("blog:post_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Another post1")
        self.assertContains(response, "Another post6")
        self.assertNotContains(response, "Another post2")

    def test_markdown_format_templatetags_works(self):
        user = User.objects.create_user("user1", "pw432joij")
        Post.objects.create(
            title='Markdown post',
            slug='markdown-post', 
            body='*This is emphasized* and **this is more emphasized**.', 
            author=user, 
            status='published'
        )
        date = timezone.now()        
        response = self.client.get(reverse('blog:post_detail', args=[date.year, date.month, date.day, 'markdown-post']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Markdown post")
        self.assertContains(response, "<em>This is emphasized</em> and <strong>this is more emphasized</strong>.", html=True)

      




