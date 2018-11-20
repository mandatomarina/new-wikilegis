# Generated by Django 2.1.3 on 2018-11-20 12:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('slug', models.SlugField()),
                ('description', models.TextField(verbose_name='description')),
                ('number', models.IntegerField(blank=True, null=True, verbose_name='number')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='year')),
            ],
            options={
                'verbose_name': 'document',
                'verbose_name_plural': 'documents',
            },
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('initials', models.CharField(max_length=200, verbose_name='initials')),
            ],
            options={
                'verbose_name': 'document type',
                'verbose_name_plural': 'document types',
            },
        ),
        migrations.CreateModel(
            name='Excerpt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='order')),
                ('excerpt_type', models.CharField(blank=True, choices=[('book', 'Book'), ('chapter', 'Chapter'), ('title', 'Title'), ('section', 'Section'), ('subsection', 'Subsection'), ('article', 'Article'), ('paragraph', 'Paragraph'), ('item', 'Item'), ('line', 'Line'), ('point', 'Point'), ('quote', 'Quote')], max_length=200, null=True, verbose_name='excerpt type')),
                ('number', models.PositiveIntegerField(blank=True, null=True, verbose_name='number')),
                ('content', models.TextField(verbose_name='content')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='excerpts', to='projects.Document', verbose_name='document')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='projects.Excerpt', verbose_name='parent')),
            ],
            options={
                'verbose_name': 'excerpt',
                'verbose_name_plural': 'excerpts',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'theme',
                'verbose_name_plural': 'themes',
            },
        ),
        migrations.AddField(
            model_name='document',
            name='document_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.DocumentType', verbose_name='document type'),
        ),
        migrations.AddField(
            model_name='document',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AddField(
            model_name='document',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Theme', verbose_name='theme'),
        ),
    ]
