# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_blog', '0004_delete_testmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.FileField(upload_to='', default='settings.MEDIA_ROOT/default.jpg'),
        ),
    ]
