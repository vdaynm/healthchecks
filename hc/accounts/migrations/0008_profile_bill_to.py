# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("accounts", "0007_profile_check_limit")]

    operations = [
        migrations.AddField(
            model_name="profile", name="bill_to", field=models.TextField(blank=True)
        )
    ]
