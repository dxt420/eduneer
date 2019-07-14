# Generated by Django 2.1.7 on 2019-06-30 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyGenericModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theFile', models.FileField(blank=True, default='aa', upload_to='media/files/')),
                ('firebase_id_token', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
