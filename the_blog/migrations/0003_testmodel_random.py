# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_blog', '0002_testmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='random',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
