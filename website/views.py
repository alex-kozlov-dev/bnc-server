from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from . import models, serializers


@api_view(['GET'])
def homepage_view(request):

    homepage = models.Homepage.get_solo()
    serializer = serializers.HomepageSerializer(homepage)
    return Response(serializer.data)


@api_view(['GET'])
def meta_view(request):

    meta = models.WebsiteMeta.get_solo()
    serializer = serializers.WebsiteMetaSerializer(meta)
    return Response(serializer.data)


@api_view(['GET'])
def posts_view(request):
    posts = models.Post.objects.filter(status='published')
    serializer = serializers.PostShortSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def post_detail_view(request, pk):
    try:
        post = models.Post.objects.get(pk=pk)
    except models.Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    post_serializer = serializers.PostSerializer(post)
    other_posts = models.Post.objects.filter(
        status='published').filter(~Q(pk=pk))[:2]
    other_posts_serializer = serializers.PostShortSerializer(
        other_posts, many=True)

    return Response({'post': post_serializer.data, 'other_posts': other_posts_serializer.data})


@api_view(['GET'])
def payment_details_view(request):
    payment_details = models.PaymentDetail.objects.all()
    crypto_payment_details = models.CryptoPaymentDetail.objects.all()

    payment_details_serializer = serializers.PaymentDetailSerializer(
        payment_details, many=True)
    crypto_payment_details_serializer = serializers.CryptoPaymentDetailSerializer(
        crypto_payment_details, many=True)

    return Response({
        'payment_details': payment_details_serializer.data,
        'crypto_payment_details': crypto_payment_details_serializer.data,
    })


@api_view(['GET'])
def files_view(request):
    files = models.File.objects.all()
    files_serializer = serializers.FileSerializer(files, many=True)

    return Response(files_serializer.data)
