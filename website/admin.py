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
    # sortable_field_name = "position"
    extra = 0


@admin.register(models.Post)
class PostAdmin(TranslationAdmin, NestedModelAdmin):
    fields = ('status', 'title', 'slug', 'text', 'main_image', 'image_preview')
    prepopulated_fields = {"slug": ("title_uk",)}
    inlines = [ImageInline]
    readonly_fields = ('image_preview', 'main_image_thumb')
    image_preview = AdminThumbnail(image_field='main_image_thumb')
    sortable_field_name = "position"
    fieldsets_and_inlines_order = ('f', 'i')

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


class WartimeItemInline(NestedStackedInline, TranslationStackedInline):
    model = models.WartimeItem
    sortable_field_name = "position"
    extra = 0


class PeacetimeItemInline(NestedStackedInline, TranslationStackedInline):
    model = models.PeacetimeItem
    sortable_field_name = "position"
    extra = 0


class PartnerInline(NestedStackedInline):
    model = models.Partner
    sortable_field_name = "position"
    extra = 0


class TextItemInline(NestedStackedInline, TranslationStackedInline):
    model = models.TextItem
    sortable_field_name = "position"
    verbose_name = 'Item'
    verbose_name_plural = 'Who are we helping?'
    extra = 0


@admin.register(models.Homepage)
class HomepageAdmin(SingletonModelAdmin, TranslationAdmin, NestedModelAdmin):
    fieldsets = [
        ('Splash screen', {
            'fields': [
                'splash_title',
                'splash_text',
                'splash_image',
                'splash_image_preview'
            ]
        }),
        ('Intro', {
            'fields': [
                'intro_text',
                'intro_image',
                'intro_text_2',
            ]
        }),
        ('Wartime', {
            'fields': [
                'wartime_image',
                # 'wartime_items'
            ]
        }),
        ('Peacetime', {
            'fields': [
                'peacetime_image',
                # 'peacetime_items'
            ]
        }),
        ('CTA', {
            'fields': ['cta']
        }),
        # ('Partners', {
        #     'fields': ['partners']
        # }),
        # ('Who are we helping?', {
        #     'fields': ['who_we_help']
        # }),
        ('Outro', {
            'fields': ['outro_text']
        })
    ]
    inlines = [WartimeItemInline, PeacetimeItemInline,
               PartnerInline, TextItemInline]
    readonly_fields = ('splash_image_preview',)
    splash_image_preview = AdminThumbnail(image_field='splash_image')
    fieldsets_and_inlines_order = (
        'f', 'f', 'f', 'i', 'f', 'i', 'f', 'i', 'i', 'f')


@admin.register(models.File)
class FileAdmin(TranslationAdmin, NestedModelAdmin):
    fieldsets_and_inlines_order = ('f',)
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
    fieldsets_and_inlines_order = ('f', 'i', 'i')


@admin.register(models.Legal)
class LegalAdmin(SingletonModelAdmin, TranslationAdmin):
    fieldsets = [
        ('Terms of use', {'fields': ['terms_of_use_enabled', 'terms_of_use']}),
        ('Privacy policy', {'fields': [
         'privacy_policy_enabled', 'privacy_policy']}),
    ]
    fieldsets_and_inlines_order = ('f', 'f')
