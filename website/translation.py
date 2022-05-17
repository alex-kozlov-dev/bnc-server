from modeltranslation.translator import translator, TranslationOptions

from . import models


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


class WebsiteMetaTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'address')


class IconTextItemTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


class TextItemTranslationOptions(TranslationOptions):
    fields = ('text',)


class HomepageTranslationOptions(TranslationOptions):
    fields = ('splash_title', 'splash_text', 'intro_text',
              'intro_text_2', 'cta', 'outro_text')


class FileTranslationOptions(TranslationOptions):
    fields = ('title',)


class PaymentDetailTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


class LegalTranslationOptions(TranslationOptions):
    fields = ('terms_of_use', 'privacy_policy')


translator.register(models.WebsiteMeta, WebsiteMetaTranslationOptions)
translator.register(models.Homepage, HomepageTranslationOptions)
translator.register(models.TextItem, TextItemTranslationOptions)
translator.register(models.WartimeItem, IconTextItemTranslationOptions)
translator.register(models.PeacetimeItem, IconTextItemTranslationOptions)
translator.register(models.Post, PostTranslationOptions)
translator.register(models.File, FileTranslationOptions)
translator.register(models.PaymentDetail, PaymentDetailTranslationOptions)
translator.register(models.Legal, LegalTranslationOptions)
