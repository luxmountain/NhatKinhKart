# Generated by Django 5.0.7 on 2024-08-09 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('New', 'New'), ('Accepted', 'Accepted')], default='New', max_length=10),
        ),
    ]
