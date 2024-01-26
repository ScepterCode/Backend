from django.urls import path
from ferrari.views import PostList, PostDetail

urlpatterns = [
    path("Post/", PostList.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetail.as_view(), name="post-detail"),
]
