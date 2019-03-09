from django.test import TestCase
import datetime
from django.utils import timezone
from blog.forms import EmailPostForm, CommentForm, SearchForm
from blog.models import Post
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class TestForm(TestCase):

    def test_email_post_form_page_works(self):
        user = User.objects.create_user("user1", "pw432joij")
        post = Post.objects.create(title='Another post1234', slug='another-post1234', body='text...', author=user, status='published') 
        response = self.client.get(reverse('blog:post_share', args=[post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Another post1234")
        self.assertIsInstance(response.context["form"], EmailPostForm)

    def test_email_post_form_date_field_label(self):
        form = EmailPostForm()        
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'name')

    def test_valid_email_post_form_sends_email(self):
        form = EmailPostForm({
            'name': 'Luke Skywalker',
            'email': 'one@one.com',
            'to': 'two@two.com',
            'comments': 'This is comments...'
        })
        self.assertTrue(form.is_valid())
    
    def test_invalid_email_post_form_without_name_field(self):
        form = EmailPostForm({
            'email': 'one@one.com',
            'to': 'two@two.com',            
            'comments': 'This is comments...'})
        self.assertFalse(form.is_valid())

    def test_invalid_email_post_form_without_email_field(self):
        form = EmailPostForm({
            'name': 'Luke Skywalker',
            'to': 'two@two.com',            
            'comments': 'This is comments...'})
        self.assertFalse(form.is_valid())

    def test_invalid_email_post_form_without_to_field(self):
        form = EmailPostForm({
            'name': 'Luke Skywalker', 
            'email': 'one@one.com',          
            'comments': 'This is comments...'})
        self.assertFalse(form.is_valid())

    def test_invalid_email_post_form_without_all_fields(self):
        form = EmailPostForm({})
        self.assertFalse(form.is_valid())

    def test_valid_comment_form(self):
        form = CommentForm({
            'name': 'Luke Skywalker',
            'email': 'one@one.com',
            'body': 'This is body ...'
            })        
        self.assertTrue(form.is_valid())
    
    def test_invalid_comment_form_without_name_field(self):
        form = CommentForm({
            'email': 'one@one.com',
            'body': 'This is body ...'
            })        
        self.assertFalse(form.is_valid())

    def test_invalid_comment_form_without_email_field(self):
        form = CommentForm({
            'name': 'Luke Skywalker',
            'body': 'This is body ...'
            })        
        self.assertFalse(form.is_valid())

    def test_invalid_comment_form_without_body_field(self):
        form = CommentForm({
            'email': 'one@one.com',
            'name': 'Luke Skywalker',
            })        
        self.assertFalse(form.is_valid())

    def test_invalid_comment_form_without_all_fields(self):
        form = CommentForm({})        
        self.assertFalse(form.is_valid())

    def test_comment_form_page_works(self):
        user = User.objects.create_user("user1", "pw432joij")
        Post.objects.create(title='Another post4', slug='another-post4', body='Post body.', author=user, status='published')
        date = timezone.now()        
        response = self.client.get(reverse('blog:post_detail', args=[date.year, date.month, date.day, 'another-post4']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Another post4")
        self.assertIsInstance(response.context["comment_form"], CommentForm)

    def test_search_form_page_works(self):
        response = self.client.get(reverse('blog:post_search'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], SearchForm)

    def test_valid_search_form(self):
        form = SearchForm({
            'query': 'Django',
        })
        self.assertTrue(form.is_valid())

    def test_invalid_search_form_without_all_fields(self):
        form = SearchForm({})
        self.assertFalse(form.is_valid())

    def test_invalid_search_form_with_empty_query(self):
        form = SearchForm({
            'query': '',
        })
        self.assertFalse(form.is_valid())

