# Generated by Django 5.0.7 on 2024-08-09 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Cancelled', 'Cancelled'), ('Accepted', 'Accepted'), ('Completed', 'Completed'), ('New', 'New')], default='New', max_length=10),
        ),
    ]
