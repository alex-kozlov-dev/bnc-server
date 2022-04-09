# Generated by Django 4.0.3 on 2022-04-09 19:15

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_remove_icontextitem_details_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='icontextitem',
            name='details',
            field=django_quill.fields.QuillField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='icontextitem',
            name='details_en',
            field=django_quill.fields.QuillField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='icontextitem',
            name='details_uk',
            field=django_quill.fields.QuillField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='icontextitem',
            name='summary',
            field=django_quill.fields.QuillField(default=''),
        ),
        migrations.AddField(
            model_name='icontextitem',
            name='summary_en',
            field=django_quill.fields.QuillField(default='', null=True),
        ),
        migrations.AddField(
            model_name='icontextitem',
            name='summary_uk',
            field=django_quill.fields.QuillField(default='', null=True),
        ),
        migrations.AddField(
            model_name='pagesection',
            name='text',
            field=django_quill.fields.QuillField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pagesection',
            name='text_en',
            field=django_quill.fields.QuillField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pagesection',
            name='text_uk',
            field=django_quill.fields.QuillField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='paymentdetail',
            name='text',
            field=django_quill.fields.QuillField(default=''),
        ),
        migrations.AddField(
            model_name='paymentdetail',
            name='text_en',
            field=django_quill.fields.QuillField(default='', null=True),
        ),
        migrations.AddField(
            model_name='paymentdetail',
            name='text_uk',
            field=django_quill.fields.QuillField(default='', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='text',
            field=django_quill.fields.QuillField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='text_en',
            field=django_quill.fields.QuillField(default='', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='text_uk',
            field=django_quill.fields.QuillField(default='', null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=django_quill.fields.QuillField(default=''),
        ),
        migrations.AddField(
            model_name='question',
            name='answer_en',
            field=django_quill.fields.QuillField(default='', null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='answer_uk',
            field=django_quill.fields.QuillField(default='', null=True),
        ),
        migrations.AddField(
            model_name='textitem',
            name='text',
            field=django_quill.fields.QuillField(default=''),
        ),
        migrations.AddField(
            model_name='textitem',
            name='text_en',
            field=django_quill.fields.QuillField(default='', null=True),
        ),
        migrations.AddField(
            model_name='textitem',
            name='text_uk',
            field=django_quill.fields.QuillField(default='', null=True),
        ),
        migrations.AddField(
            model_name='websitemeta',
            name='address',
            field=django_quill.fields.QuillField(default=''),
        ),
        migrations.AddField(
            model_name='websitemeta',
            name='address_en',
            field=django_quill.fields.QuillField(default='', null=True),
        ),
        migrations.AddField(
            model_name='websitemeta',
            name='address_uk',
            field=django_quill.fields.QuillField(default='', null=True),
        ),
    ]