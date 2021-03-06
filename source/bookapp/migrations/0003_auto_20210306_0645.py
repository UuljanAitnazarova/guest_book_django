# Generated by Django 3.1.7 on 2021-03-06 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0002_auto_20210306_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='author',
            field=models.CharField(max_length=120, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='status',
            field=models.CharField(choices=[('active', 'Activr'), ('blocked', 'Blocked')], default=('active', 'Activr'), max_length=10, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='text',
            field=models.TextField(max_length=1000, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
    ]