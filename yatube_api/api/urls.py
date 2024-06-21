from django.urls import path, include
from rest_framework import routers

from api.views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet

v1_router = routers.DefaultRouter()
v1_router.register('posts', PostViewSet, basename='posts')
v1_router.register('groups', GroupViewSet, basename='groups')
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)
v1_router.register('follow', FollowViewSet, basename='follow')


urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(v1_router.urls)),
]
