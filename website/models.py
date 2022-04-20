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


class Legal(SingletonModel):
    terms_of_use_enabled = models.BooleanField(default=False)
    terms_of_use = QuillField(null=True, blank=True)
    privacy_policy_enabled = models.BooleanField(default=False)
    privacy_policy = QuillField(null=True, blank=True)


class WebsiteMeta(SingletonModel):
    title = models.CharField(max_length=255, default='Title')
    description = models.TextField(default='')
    logo = models.FileField(validators=[is_svg])
    logo_inverted = models.FileField(validators=[is_svg])
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address = QuillField(default='')
    copyright = models.CharField(max_length=255, default="© BNC, 2022")


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
    splash_title = models.CharField(max_length=255, default='Title')
    splash_text = models.TextField(default='Lorem ipsum...')
    splash_image = ProcessedImageField(
        format='JPEG', options={'quality': 90}, processors=[ResizeToFit(width=1280)])

    # --- Splash END

    def __str__(self) -> str:
        return 'Homepage'

    class Meta:
        verbose_name = 'Homepage'


def is_type(type):
    return lambda s: s.section_type == type


class PageSection(FieldValidationMixin, SortableModel):
    SECTION_TYPES = (
        ('text', 'Text'),
        ('text_image', 'Text + Image'),
        ('donate_cta', 'CTA + Donate button'),
        ('text_list', 'Numbered text list'),
        ('partners', 'Partners list'),
        ('qa', 'Questions & Answers'),
        ('icon_text_list', 'Icon+Text list'),
    )
    section_type = models.CharField(max_length=255, choices=SECTION_TYPES)
    page = models.ForeignKey(
        Homepage, on_delete=models.CASCADE, null=True, blank=True)

    title = models.CharField(max_length=255, null=True, blank=True)
    cta = models.CharField(max_length=255, null=True, blank=True)
    text = QuillField(null=True, blank=True)
    image_on_the_left = models.BooleanField(default=False)
    image = ProcessedImageField(null=True, blank=True, format='JPEG', options={
        'quality': 80}, processors=[ResizeToFit(width=500, upscale=True)])

    REQUIRED_FIELDS = ['section_type']
    CONDITIONAL_REQUIRED_FIELDS = [
        (is_type('text'), i18nfields(['title', 'text'])),
        (is_type('text_image'), i18nfields(['title', 'text']) + ['image']),
        (is_type('donate_cta'), i18nfields(['cta'])),
    ]

    def __str__(self) -> str:
        return self.section_type


class TextItem(SortableModel):
    text = QuillField(default='')
    section = models.ForeignKey(PageSection, on_delete=models.CASCADE)


class Partner(SortableModel):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    section = models.ForeignKey(PageSection, on_delete=models.CASCADE)


class Question(SortableModel):
    question = models.CharField(max_length=255)
    answer = QuillField(default='')
    section = models.ForeignKey(PageSection, on_delete=models.CASCADE)


class IconTextItem(SortableModel):
    icon = models.FileField(validators=[is_svg])
    title = models.CharField(max_length=255)
    summary = QuillField(default='')
    details = QuillField(null=True, blank=True)
    section = models.ForeignKey(PageSection, on_delete=models.CASCADE)


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
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class File(SortableModel):
    src = models.FileField('File')
    title = models.CharField(max_length=255)


class Payment(SingletonModel):
    liqpay_link = models.CharField(max_length=255, null=True, blank=True)


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
