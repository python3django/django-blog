from django.test import TestCase
from django.urls import reverse
from blog.models import Post
from django.contrib.auth.models import User
from blog.sitemaps import PostSitemap


class TestSitemap(TestCase):
    
    def test_sitemap_works(self):
        user = User.objects.create_user("user1", "pw432joij")
        post1 = Post.objects.create(title='Another post1', slug='another-post1', body='Post body.', author=user, status='published')
        post2 = Post.objects.create(title='Another post2', slug='another-post2', body='Post body.', author=user)
        post3 = Post.objects.create(title='Another post3', slug='another-post3', body='Post body.', author=user, status='published')
        response = self.client.get(reverse("django.contrib.sitemaps.views.sitemap"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post1.get_absolute_url())
        self.assertNotContains(response, post2.get_absolute_url(), html=True)
        self.assertContains(response, post3.get_absolute_url())
        self.assertContains(response, '<changefreq>{}</changefreq>'.format(PostSitemap.changefreq), html=True)
        self.assertContains(response, '<priority>{}</priority>'.format(PostSitemap.priority), html=True)
        self.assertNotContains(response, '<priority>{}</priority>'.format(PostSitemap.priority - 0.1), html=True)


