from modeltranslation.translator import translator, TranslationOptions

from . import models


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


class WebsiteMetaTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'address')


class IconTextItemTranslationOptions(TranslationOptions):
    fields = ('title', 'summary', 'details')


class QuestionTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')


class TextItemTranslationOptions(TranslationOptions):
    fields = ('text',)


class HomepageTranslationOptions(TranslationOptions):
    fields = ('splash_title', 'splash_text')


class PageSectionTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'cta')


class FileTranslationOptions(TranslationOptions):
    fields = ('title',)


class PaymentDetailTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


class LegalTranslationOptions(TranslationOptions):
    fields = ('terms_of_use', 'privacy_policy')


translator.register(models.WebsiteMeta, WebsiteMetaTranslationOptions)
translator.register(models.Homepage, HomepageTranslationOptions)
translator.register(models.PageSection, PageSectionTranslationOptions)
translator.register(models.TextItem, TextItemTranslationOptions)
translator.register(models.IconTextItem, IconTextItemTranslationOptions)
translator.register(models.Question, QuestionTranslationOptions)
translator.register(models.Post, PostTranslationOptions)
translator.register(models.File, FileTranslationOptions)
translator.register(models.PaymentDetail, PaymentDetailTranslationOptions)
translator.register(models.Legal, LegalTranslationOptions)
