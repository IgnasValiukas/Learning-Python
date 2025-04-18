# Generated by Django 5.2 on 2025-04-15 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0007_remove_orderline_status_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'Administered'), ('c', 'Closed'), ('r', 'Ready'), ('b', 'Booked')], default='a', help_text='Status', max_length=1),
        ),
    ]
