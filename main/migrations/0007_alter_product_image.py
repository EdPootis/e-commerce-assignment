# Generated by Django 5.1.1 on 2024-10-06 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='./media/'),
        ),
    ]
