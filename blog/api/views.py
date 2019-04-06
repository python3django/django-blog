from rest_framework import generics
from blog.models import Post, Comment
from blog.api.serializers import PostSerializer, CommentSerializer
from rest_framework import permissions 
from blog.api import custompermission 
from rest_framework.response import Response 
from rest_framework.reverse import reverse
from rest_framework.throttling import ScopedRateThrottle 
from rest_framework import filters 
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter 


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
        permissions.IsAuthenticatedOrReadOnly,
        custompermission.IsCurrentUserAuthorOrReadOnly, 
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


class ApiRoot(generics.GenericAPIView): 
    name = 'api-root' 
    def get(self, request, *args, **kwargs): 
        return Response({ 
            'posts': reverse(PostListView.name, request=request),
            'comments': reverse(CommentListView.name, request=request), 
            }) 
