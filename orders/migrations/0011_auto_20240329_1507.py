# Generated by Django 3.0.5 on 2024-03-29 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20240328_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Cancelled', 'Cancelled'), ('Completed', 'Completed'), ('Accepted', 'Accepted'), ('New', 'New')], default='New', max_length=10),
        ),
    ]
