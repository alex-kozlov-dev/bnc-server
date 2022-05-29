from django.db import models
from solo.models import SingletonModel
from extra_validator import FieldValidationMixin
from django_quill.fields import QuillField
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import SmartResize, ResizeToFit

from website.utils import i18nfields
from website.validators import is_svg


class SortableModel(models.Model):
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['position']
        abstract = True


class IconTextItemModel(SortableModel):
    icon = models.FileField(validators=[is_svg])
    title = models.CharField(max_length=255)
    text = QuillField(default='')

    class Meta:
        abstract = True


class Legal(SingletonModel):
    terms_of_use_enabled = models.BooleanField(default=False)
    terms_of_use = QuillField(null=True, blank=True, default='')
    privacy_policy_enabled = models.BooleanField(default=False)
    privacy_policy = QuillField(null=True, blank=True, default='')


class WebsiteMeta(SingletonModel):
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    logo = models.FileField(validators=[is_svg])
    logo_inverted = models.FileField(validators=[is_svg])
    email = models.CharField(max_length=255)
    address = QuillField(default='')
    copyright = models.CharField(max_length=255, default="")


class PhoneNumber(SortableModel):
    phone_number = models.CharField(max_length=255)
    meta = models.ForeignKey(
        WebsiteMeta,
        on_delete=models.CASCADE,
        related_name='phone_numbers'
    )


class SocialLink(SortableModel):
    SOCIAL_TYPES = (
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('twitter', 'Twitter'),
        ('telegram', 'Telegram'),
    )
    social_type = models.CharField(max_length=255, choices=SOCIAL_TYPES)
    link = models.CharField(max_length=255)
    meta = models.ForeignKey(
        WebsiteMeta, on_delete=models.CASCADE, null=True, blank=True)


class Homepage(SingletonModel):

    # --- Splash
    splash_title = models.CharField(max_length=255, default='')
    splash_text = models.TextField(default='')
    splash_image = ProcessedImageField(
        format='PNG', options={'quality': 90}, processors=[ResizeToFit(width=1280)])
    # --- Splash END

    # --- Intro
    intro_text = QuillField(null=True, blank=True)
    intro_image = ProcessedImageField(
        format='JPEG', options={'quality': 90}, processors=[ResizeToFit(width=1280)])
    intro_text_2 = QuillField(null=True, blank=True)
    # --- Intro END

    # --- Wartime
    wartime_image = ProcessedImageField(
        format='JPEG', options={'quality': 90}, processors=[ResizeToFit(width=1280)])
    # --- Wartime END

    # --- Peacetime
    peacetime_image = ProcessedImageField(
        format='JPEG', options={'quality': 90}, processors=[ResizeToFit(width=1280)])
    # --- Wartime END

    # --- CTA
    cta = models.CharField(max_length=255, null=True, blank=True)
    # --- CTA END

    # --- Outro
    outro_text = QuillField(null=True, blank=True)
    # --- Outro END

    def __str__(self) -> str:
        return 'Homepage'

    class Meta:
        verbose_name = 'Homepage'


class WartimeItem(IconTextItemModel):
    homepage = models.ForeignKey(
        Homepage,
        on_delete=models.CASCADE,
        related_name='wartime_items'
    )


class PeacetimeItem(IconTextItemModel):
    homepage = models.ForeignKey(
        Homepage,
        on_delete=models.CASCADE,
        related_name='peacetime_items'
    )


class Partner(SortableModel):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    homepage = models.ForeignKey(
        Homepage,
        on_delete=models.CASCADE,
        related_name='partners'
    )


class TextItem(SortableModel):
    text = models.CharField(max_length=255)
    homepage = models.ForeignKey(
        Homepage,
        on_delete=models.CASCADE,
        related_name='who_we_help'
    )


class Post(SortableModel):
    STATUSES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    slug = models.SlugField(max_length=100, unique=True)
    status = models.CharField(
        max_length=255, default='draft', choices=STATUSES)
    title = models.CharField(max_length=255)
    text = QuillField(default='')
    created_at = models.DateField(auto_now_add=True)
    main_image = ProcessedImageField(format='JPEG', options={'quality': 80}, processors=[
                                     ResizeToFit(width=1280)])
    main_image_thumb = ImageSpecField(
        source='main_image', processors=[SmartResize(360, 203)])

    def __str__(self):
        return 'Post: ' + self.title

    class Meta:
        verbose_name_plural = 'Posts'


class Image(SortableModel):
    src = ProcessedImageField(format='JPEG', options={'quality': 80}, processors=[
                              ResizeToFit(width=1400)])
    thumb = ImageSpecField(source='src', processors=[SmartResize(360, 203)])
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, null=True, blank=True)


class File(SortableModel):
    src = models.FileField('File')
    title = models.CharField(max_length=255)


class Payment(SingletonModel):
    pass


class CryptoPaymentDetail(SortableModel):
    CRYPTO_TYPES = (
        ('btc', 'Bitcoin'),
        ('eth', 'Etherium'),
        ('bch', 'Bitcoin Cash'),
        ('ltc', 'Litecoin'),
        ('usdt', 'Tether'),
    )
    crypto_type = models.CharField(max_length=255, choices=CRYPTO_TYPES)
    wallet = models.CharField(max_length=255)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)

    def __str__(self):
        return self.crypto_type.capitalize() + ' ' + self.wallet


class PaymentDetail(SortableModel):
    title = models.CharField(max_length=255)
    text = QuillField(default='')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
