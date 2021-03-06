"""bnc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from website import views

urlpatterns = [
    path('', views.index_redirect),
    path('admin/', admin.site.urls),
    path('_nested_admin/', include('nested_admin.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('homepage/', views.homepage_view),
    path('meta/', views.meta_view),
    path('posts/', views.posts_view),
    path('posts/<str:slug>/', views.post_detail_view),
    path('payment_details/', views.payment_details_view),
    path('files/', views.files_view),
    path('legal/', views.legal_view),
)
