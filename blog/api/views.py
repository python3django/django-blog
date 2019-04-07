from rest_framework import generics
from blog.models import Post, Comment
from blog.api.serializers import PostSerializer, CommentSerializer, UserSerializer
from rest_framework import permissions 
from blog.api import custompermission 
from rest_framework.response import Response 
from rest_framework.reverse import reverse
from rest_framework.throttling import ScopedRateThrottle 
from rest_framework import filters 
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter 
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication


class PostListView(generics.ListCreateAPIView):
    throttle_scope = 'posts' 
    throttle_classes = (ScopedRateThrottle,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-list'
    filter_fields = ('title', 'author',) 
    search_fields = ('title', 'body',) 
    ordering_fields = ('title', 'created', 'status',) 
    permission_classes = ( 
        permissions.IsAuthenticatedOrReadOnly,
        )
    
    def perform_create(self, serializer):
        # переопределяем метод чтобы автором поста сохранить того кто его создал,
        # не зависимо от полученных данных
        serializer.save(author=self.request.user)              
    

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope = 'posts' 
    throttle_classes = (ScopedRateThrottle,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-detail'
    permission_classes = (
        custompermission.IsCurrentUserAuthorOrAdminUserOrReadOnly,
        )


class CommentListView(generics.ListCreateAPIView):
    throttle_scope = 'comments' 
    throttle_classes = (ScopedRateThrottle,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-list'
    filter_fields = ('name', 'email',) 
    search_fields = ('body',) 
    ordering_fields = ('created',) 

    def perform_create(self, serializer):
        # переопределяем метод чтобы добавить ссылку на пост,
        # к которому относится данный комментарий
        serializer.save(post_id=serializer.initial_data['post_id'])


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope = 'comments' 
    throttle_classes = (ScopedRateThrottle,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-detail'
    permission_classes = ( 
        custompermission.IsAdminUserOrReadOnly, 
        )


class UserListView(generics.ListAPIView):
    throttle_scope = 'users' 
    throttle_classes = (ScopedRateThrottle,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'
    filter_fields = ('username', 'email', 'groups',) 
    search_fields = ('username', 'first_name',) 
    ordering_fields = ('id', 'username', 'first_name',)        
    authentication_classes = (
        TokenAuthentication,
        )
    permission_classes = (
        permissions.IsAuthenticated,
        )

class UserDetailView(generics.RetrieveAPIView):
    throttle_scope = 'users' 
    throttle_classes = (ScopedRateThrottle,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'
    authentication_classes = (
        TokenAuthentication,
        )
    permission_classes = (
        permissions.IsAuthenticated,
        )


class ApiRoot(generics.GenericAPIView): 
    name = 'api-root' 
    def get(self, request, *args, **kwargs): 
        return Response({ 
            'posts': reverse(PostListView.name, request=request),
            'comments': reverse(CommentListView.name, request=request),
            'users': reverse(UserListView.name, request=request),
            }) 
