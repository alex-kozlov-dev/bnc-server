from django.contrib import admin
from solo.admin import SingletonModelAdmin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
from nested_admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline
from imagekit.admin import AdminThumbnail

from . import models


class ImageInline(NestedStackedInline):
    fields = ('src', 'preview')
    readonly_fields = ('preview', 'thumb')
    preview = AdminThumbnail(image_field='thumb')
    model = models.Image
    sortable_field_name = "position"
    extra = 0


@admin.register(models.Post)
class PostAdmin(TranslationAdmin, NestedModelAdmin):
    fields = ('status', 'title', 'slug', 'text', 'main_image', 'image_preview')
    prepopulated_fields = {"slug": ("title_uk",)}
    inlines = [ImageInline]
    readonly_fields = ('image_preview', 'main_image_thumb')
    image_preview = AdminThumbnail(image_field='main_image_thumb')
    sortable_field_name = "position"

    class Media:
        css = {
            'all': ('admin/css/quill.css',)
        }


class SocialLinkInline(NestedTabularInline):
    model = models.SocialLink
    sortable_field_name = "position"
    extra = 0


@admin.register(models.WebsiteMeta)
class WebsiteMetaAdmin(SingletonModelAdmin, TranslationAdmin, NestedModelAdmin):
    inlines = [SocialLinkInline]


class IconTextItemInline(NestedStackedInline, TranslationStackedInline):
    model = models.IconTextItem
    sortable_field_name = "position"
    extra = 0


class QuestionInline(NestedStackedInline, TranslationStackedInline):
    model = models.Question
    sortable_field_name = "position"
    extra = 0


class PartnerInline(NestedStackedInline):
    model = models.Partner
    sortable_field_name = "position"
    extra = 0


class TextItemInline(NestedStackedInline, TranslationStackedInline):
    model = models.TextItem
    sortable_field_name = "position"
    extra = 0


class PageSectionInline(NestedStackedInline, TranslationStackedInline):
    model = models.PageSection
    inlines = [TextItemInline, PartnerInline,
               QuestionInline, IconTextItemInline]

    readonly_fields = ('image_preview',)

    image_preview = AdminThumbnail(image_field='image')

    sortable_field_name = "position"

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
class FileAdmin(TranslationAdmin, NestedModelAdmin):
    sortable_field_name = "position"


class PaymentDetailInline(NestedStackedInline, TranslationStackedInline):
    model = models.PaymentDetail
    sortable_field_name = "position"
    extra = 0


class CryptoPaymentDetailInline(NestedStackedInline):
    model = models.CryptoPaymentDetail
    sortable_field_name = "position"
    extra = 0


@admin.register(models.Payment)
class PaymentAdmin(SingletonModelAdmin, NestedModelAdmin):
    inlines = [PaymentDetailInline, CryptoPaymentDetailInline]


@admin.register(models.Legal)
class LegalAdmin(SingletonModelAdmin, TranslationAdmin):
    fieldsets = [
        ('Terms of use', {'fields': ['terms_of_use_enabled', 'terms_of_use']}),
        ('Privacy policy', {'fields': [
         'privacy_policy_enabled', 'privacy_policy']}),
    ]
