from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import BlogView, PostView, PostDelete, PostDetailsView

urlpatterns = [
    # Блог
    path('blog/', login_required(BlogView.as_view()), name='blog'),
    path('blog/create/', login_required(PostDetailsView.as_view()), name='post_create'),
    path('blog/<post_id>/', PostView.as_view(), name='post'),
    path('blog/<post_id>/update', login_required(PostDetailsView.as_view()), name='post_update'),
    path('blog/<post_id>/del', login_required(PostDelete.as_view()), name='post_delete'),
]
