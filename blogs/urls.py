from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="blogs"

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('blog_details/<int:pk>', views.BlogDetailView.as_view(), name='details'),
    path('create_posts/', views.CreateBlogPostView.as_view(), name='create'),
    path('edit_posts/<int:id>', views.EditBlogPostView.as_view(), name='edit_post'),
]


if settings.DEBUG:
    urlpatterns.extend(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
    urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

