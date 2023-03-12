"""wku_textbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from article.views import ArticleViewSet, CategoryViewSet, TagViewSet, AvatarViewSet
from comment.views import CommentViewSet
from user_info.views import UserViewSet
from textbook.views import BookTagViewSet, CourseViewSet, TextbookViewSet, SyllabusViewSet

router = DefaultRouter()
router.register(r'article', ArticleViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'tag', TagViewSet)
router.register(r'avatar', AvatarViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'user', UserViewSet)
router.register(r'booktag', BookTagViewSet)
router.register(r'course', CourseViewSet)
router.register(r'textbook', TextbookViewSet)
router.register(r'syllabus', SyllabusViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
