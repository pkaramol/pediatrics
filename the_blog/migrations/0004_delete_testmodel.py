# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_blog', '0003_testmodel_random'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestModel',
        ),
    ]
