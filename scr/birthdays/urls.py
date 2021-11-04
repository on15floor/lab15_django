from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import BirthdaysView

urlpatterns = [
    path('birthdays/<filter>/', login_required(BirthdaysView.as_view()), name='birthdays'),
    # path('blog/create/', login_required(PostDetailsView.as_view()), name='post_create'),
    # path('blog/<post_id>/', PostView.as_view(), name='post'),
    # path('blog/<post_id>/update', login_required(PostDetailsView.as_view()), name='post_update'),
    # path('blog/<post_id>/del', login_required(PostDelete.as_view()), name='post_delete'),
]
