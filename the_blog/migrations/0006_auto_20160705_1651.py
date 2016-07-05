# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_blog', '0005_auto_20160705_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.FileField(upload_to='', null=True, default='settings.MEDIA_ROOT/default.jpg', blank=True),
        ),
    ]
