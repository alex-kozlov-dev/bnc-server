from django.contrib import admin
from solo.admin import SingletonModelAdmin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline, TranslationTabularInline
from nested_admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline
from django.utils.html import mark_safe
from imagekit.admin import AdminThumbnail

from bnc.settings import MEDIA_URL

from . import models


class ImageInline(NestedStackedInline, TranslationStackedInline):
    fields = ('src', 'preview', 'alt')
    readonly_fields = ('preview', 'thumb')
    preview = AdminThumbnail(image_field='thumb')
    model = models.Image
    extra = 0


@admin.register(models.Post)
class PostAdmin(TranslationAdmin, NestedModelAdmin):
    fields = ('status', 'title', 'text', 'main_image', 'image_preview')
    inlines = [ImageInline]
    readonly_fields = ('image_preview', 'main_image_thumb')
    image_preview = AdminThumbnail(image_field='main_image_thumb')

    class Media:
        css = {
            'all': ('admin/css/quill.css',)
        }


class SocialLinkInline(NestedTabularInline):
    model = models.SocialLink
    extra = 1


@admin.register(models.WebsiteMeta)
class WebsiteMetaAdmin(SingletonModelAdmin, TranslationAdmin, NestedModelAdmin):
    inlines = [SocialLinkInline]


class IconTextItemInline(NestedStackedInline, TranslationStackedInline):
    model = models.IconTextItem
    extra = 0


class QuestionInline(NestedStackedInline, TranslationStackedInline):
    model = models.Question
    extra = 0


class PartnerInline(NestedStackedInline):
    model = models.Partner
    extra = 0


class TextItemInline(NestedStackedInline, TranslationStackedInline):
    model = models.TextItem
    extra = 0


class PageSectionInline(NestedStackedInline, TranslationStackedInline):
    model = models.PageSection
    inlines = [TextItemInline, PartnerInline,
               QuestionInline, IconTextItemInline]

    readonly_fields = ('image_preview',)

    image_preview = AdminThumbnail(image_field='image')

    extra = 0


@admin.register(models.Homepage)
class HomepageAdmin(SingletonModelAdmin, TranslationAdmin, NestedModelAdmin):
    fieldsets = [
        ('Splash screen', {'fields': [
         'splash_title', 'splash_text', 'splash_image', 'image_preview']})
    ]
    inlines = [PageSectionInline]
    readonly_fields = ('image_preview',)
    image_preview = AdminThumbnail(image_field='splash_image')

    class Media:
        js = (
            'https://code.jquery.com/jquery-3.6.0.min.js',
            'admin/js/homepage_sections_admin.js',
        )


@admin.register(models.File)
class FileAdmin(TranslationAdmin):
    pass


@admin.register(models.PaymentDetail)
class PaymentDetailAdmin(TranslationAdmin):
    pass


@admin.register(models.CryptoPaymentDetail)
class CryptoPaymentDetailAdmin(admin.ModelAdmin):
    pass
