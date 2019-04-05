from rest_framework import generics
from blog.models import Post, Comment
from blog.api.serializers import PostSerializer, CommentSerializer
from rest_framework import permissions 
from blog.api import custompermission 
from rest_framework.response import Response 
from rest_framework.reverse import reverse


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-list'
    permission_classes = ( 
        permissions.IsAuthenticatedOrReadOnly,
        #permissions.DjangoModelPermissionsOrAnonReadOnly,
        )
    
    def perform_create(self, serializer):
        # переопределяем метод чтобы автором поста сохранить того кто его создал,
        # не зависимо от полученных данных
        serializer.save(author=self.request.user)            


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-detail'
    permission_classes = ( 
        permissions.IsAuthenticatedOrReadOnly,
        custompermission.IsCurrentUserAuthorOrReadOnly, 
        )


class CommentListView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-list'


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-detail'



class ApiRoot(generics.GenericAPIView): 
    name = 'api-root' 
    def get(self, request, *args, **kwargs): 
        return Response({ 
            'posts': reverse(PostListView.name, request=request),
            'comments': reverse(CommentListView.name, request=request), 
            }) 
