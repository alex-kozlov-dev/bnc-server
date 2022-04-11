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


class IconTextItemSerializer(serializers.ModelSerializer):
    summary = QuillHtmlField()
    details = QuillHtmlField()

    class Meta:
        model = models.IconTextItem
        fields = ['id', 'icon', 'title', 'summary', 'details']


class QuestionSerializer(serializers.ModelSerializer):
    answer = QuillHtmlField()

    class Meta:
        model = models.Question
        fields = ['id', 'question', 'answer']


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Partner
        fields = ['id', 'title', 'image']


class TextItemSerializer(serializers.ModelSerializer):
    text = QuillHtmlField()

    class Meta:
        model = models.TextItem
        fields = ['id', 'text']


class PageSectionSerializer(serializers.ModelSerializer):
    icon_text_items = IconTextItemSerializer(
        source='icontextitem_set',
        many=True,
        read_only=True,
    )

    text_items = TextItemSerializer(
        source='textitem_set',
        many=True,
        read_only=True
    )

    partners = PartnerSerializer(
        source='partner_set',
        many=True,
        read_only=True,
    )

    questions = QuestionSerializer(
        source='question_set',
        many=True,
        read_only=True,
    )

    text = QuillHtmlField()

    class Meta:
        model = models.PageSection
        fields = ['id', 'section_type', 'title',
                  'text', 'cta', 'image', 'text_items', 'partners', 'questions', 'icon_text_items']


class HomepageSerializer(serializers.ModelSerializer):
    page_sections = PageSectionSerializer(
        source='pagesection_set',
        many=True,
        read_only=True
    )

    class Meta:
        model = models.Homepage
        fields = ['id', 'splash_title', 'splash_text',
                  'splash_image', 'page_sections']
