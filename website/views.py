from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from . import models, serializers


def index_redirect(request):
    return redirect('/admin/')


@api_view(['GET'])
def homepage_view(request):
    homepage = models.Homepage.get_solo()
    serializer = serializers.HomepageSerializer(homepage)
    return Response(serializer.data)


@api_view(['GET'])
def meta_view(request):
    meta = models.WebsiteMeta.get_solo()
    serializer = serializers.WebsiteMetaSerializer(meta)

    posts = models.Post.objects.all()
    files = models.File.objects.all()

    if not request.GET.get('preview'):
        posts = posts.filter(status='published')

    data = serializer.data
    data['posts_exists'] = posts.exists()
    data['files_exists'] = files.exists()

    legal = models.Legal.get_solo()
    data['terms_of_use_enabled'] = legal.terms_of_use_enabled
    data['privacy_policy_enabled'] = legal.privacy_policy_enabled

    return Response(data)


@api_view(['GET'])
def posts_view(request):
    posts = models.Post.objects.all()

    if not request.GET.get('preview'):
        posts = posts.filter(status='published')

    serializer = serializers.PostShortSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def post_detail_view(request, slug):
    try:
        post = models.Post.objects.get(slug=slug)
    except models.Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    post_serializer = serializers.PostSerializer(post)

    other_posts = models.Post.objects.filter(~Q(slug=slug))

    if not request.GET.get('preview'):
        other_posts = other_posts.filter(status='published')

    other_posts_serializer = serializers.PostShortSerializer(
        other_posts[:2], many=True)

    return Response({'post': post_serializer.data, 'other_posts': other_posts_serializer.data})


@api_view(['GET'])
def payment_details_view(request):
    payment = models.Payment.get_solo()
    serializer = serializers.PaymentSerializer(payment)

    return Response(serializer.data)


@api_view(['GET'])
def files_view(request):
    files = models.File.objects.all()
    files_serializer = serializers.FileSerializer(files, many=True)

    return Response(files_serializer.data)


@api_view(['GET'])
def legal_view(request):
    legal = models.Legal.get_solo()
    serializer = serializers.LegalSerializer(legal)

    return Response(serializer.data)
