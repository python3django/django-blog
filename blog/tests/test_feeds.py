from django.test import TestCase
from django.urls import reverse
from blog.models import Post
from django.contrib.auth.models import User
from blog.feeds import LatestPostsFeed


class TestFeeds(TestCase):
    
    def test_sitemap_works(self):
        user = User.objects.create_user("user1", "pw432joij")
        post1 = Post.objects.create(title='Another post1', slug='another-post1', body='Post 1 body.', author=user, status='published')
        post2 = Post.objects.create(title='Another post2', slug='another-post2', body='Post 2 body.', author=user)
        post3 = Post.objects.create(title='Another post3', slug='another-post3', body='Post 3 body.', author=user, status='published')
        response = self.client.get(reverse("blog:post_feed"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post1.get_absolute_url())
        self.assertNotContains(response, post2.get_absolute_url())
        self.assertContains(response, post3.get_absolute_url())
        self.assertContains(response, '<title>{}</title>'.format(LatestPostsFeed.title))
        self.assertContains(response, '<description>{}</description>'.format(LatestPostsFeed.description))
        self.assertContains(response, '<title>{}</title>'.format(post1.title))
        self.assertNotContains(response, '<title>{}</title>'.format(post2.title))
        self.assertContains(response, '<title>{}</title>'.format(post3.title))
        self.assertContains(response, '<description>{}</description>'.format(post1.body[:30]))
        self.assertNotContains(response, '<description>{}</description>'.format(post2.body[:30]))
        self.assertContains(response, '<description>{}</description>'.format(post3.body[:30]))

