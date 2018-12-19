# Generated by Django 2.1.4 on 2018-12-19 15:20

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
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('intro', models.TextField(default='')),
                ('url', models.CharField(default='Http://', max_length=50)),
                ('icon', models.ImageField(default='default_icon.png', upload_to='images/')),
                ('image', models.ImageField(default='default_image.png', upload_to='images/')),
                ('votes', models.IntegerField(default=1)),
                ('pub_date', models.DateField()),
                ('hunter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]