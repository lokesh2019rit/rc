# Generated by Django 2.2.9 on 2020-07-20 06:10

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="bill",
            name="billdetails",
            field=jsonfield.fields.JSONField(default={"no_order": "1"}),
            preserve_default=False,
        ),
    ]
