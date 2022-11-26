from rest_framework import permissions, generics

from ..viewsets.classes import CreateUpdateDestroy, CreateRetrieveUpdateDestroy
from ..viewsets.permissions import IsAuthor
from .models import Post, Comment
from .serializers import (PostSerializer, ListPostSerializer, CreateCommentSerializer, ListCommentSerializer)
# Create your views here.

class PostListView(generics.ListAPIView):
    """
    Список постов на стене пользователя
    """
    serializer_class = ListPostSerializer

    def get_queryset(self):
        return Post.objects.filter(user_id=self.kwargs.get('pk'))



class PostView(CreateRetrieveUpdateDestroy):
    """ CRUD поста"""
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes_by_action = {'get': [permissions.AllowAny],
                                    'update': [IsAuthor],
                                    'destroy': [IsAuthor]}

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentsView(CreateUpdateDestroy):
    """Редактирование комментариев к запси"""
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CreateCommentSerializer
    permission_classes_by_action = {'update': [IsAuthor],
                                    'destroy': [IsAuthor]}

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()