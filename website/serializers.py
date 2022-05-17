from rest_framework import serializers
from django_quill.drf.fields import QuillHtmlField, QuillPlainField

from . import models
from .fields import ThumbnailField


class CryptoPaymentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CryptoPaymentDetail
        fields = ['id', 'crypto_type', 'wallet']


class PaymentDetailSerializer(serializers.ModelSerializer):
    text = QuillHtmlField()

    class Meta:
        model = models.PaymentDetail
        fields = ['id', 'title', 'text']


class PaymentSerializer(serializers.ModelSerializer):
    payment_details = PaymentDetailSerializer(
        source='paymentdetail_set',
        many=True,
        read_only=True
    )
    crypto_payment_details = CryptoPaymentDetailSerializer(
        source='cryptopaymentdetail_set',
        many=True,
        read_only=True
    )

    class Meta:
        model = models.Payment
        fields = ['id', 'liqpay_link',
                  'payment_details', 'crypto_payment_details']


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.File
        fields = ['id', 'src', 'title']


class ImageSerializer(serializers.ModelSerializer):
    thumb = serializers.ImageField(read_only=True)

    class Meta:
        model = models.Image
        fields = ['id', 'src', 'thumb']


class PostShortSerializer(serializers.ModelSerializer):
    main_image_thumb = serializers.ImageField(read_only=True)

    class Meta:
        model = models.Post
        fields = ['id', 'title', 'slug', 'main_image_thumb']


class PostSerializer(serializers.ModelSerializer):
    text = QuillHtmlField()
    images = ImageSerializer(
        source='image_set',
        many=True,
        read_only=True
    )
    main_image_thumb = serializers.ImageField(read_only=True)

    class Meta:
        model = models.Post
        fields = ['id', 'title', 'text', 'main_image',
                  'main_image_thumb', 'images']


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SocialLink
        fields = ['id', 'social_type', 'link']


class WebsiteMetaSerializer(serializers.ModelSerializer):
    address = QuillHtmlField()
    social_links = SocialLinkSerializer(
        source='sociallink_set',
        many=True,
        read_only=True
    )

    class Meta:
        model = models.WebsiteMeta
        fields = ['id', 'title', 'description',
                  'social_links', 'email', 'phone_number',
                  'address', 'logo', 'logo_inverted', 'copyright']


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Partner
        fields = ['id', 'title', 'image']


class WartimeItemSerializer(serializers.ModelSerializer):
    text = QuillHtmlField()

    class Meta:
        model = models.WartimeItem
        fields = ['id', 'icon', 'title', 'text']


class PeacetimeItemSerializer(serializers.ModelSerializer):
    text = QuillHtmlField()

    class Meta:
        model = models.PeacetimeItem
        fields = ['id', 'icon', 'title', 'text']


class TextItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TextItem
        fields = ['id', 'text']


class HomepageSerializer(serializers.ModelSerializer):
    wartime_items = WartimeItemSerializer(
        many=True,
        read_only=True
    )
    peacetime_items = PeacetimeItemSerializer(
        many=True,
        read_only=True
    )
    intro_text = QuillHtmlField()
    intro_text_2 = QuillHtmlField()
    partners = PartnerSerializer(
        many=True,
        read_only=True
    )
    who_we_help = TextItemSerializer(
        many=True,
        read_only=True
    )
    outro_text = QuillHtmlField()

    class Meta:
        model = models.Homepage
        fields = [
            'id',
            'splash_title',
            'splash_text',
            'splash_image',
            'intro_text',
            'intro_image',
            'intro_text_2',
            'wartime_image',
            'wartime_items',
            'peacetime_image',
            'peacetime_items',
            'cta',
            'partners',
            'who_we_help',
            'outro_text',
        ]


class LegalSerializer(serializers.ModelSerializer):
    terms_of_use = QuillHtmlField()
    privacy_policy = QuillHtmlField()

    class Meta:
        model = models.Legal
        fields = ['terms_of_use_enabled', 'terms_of_use',
                  'privacy_policy_enabled', 'privacy_policy']
