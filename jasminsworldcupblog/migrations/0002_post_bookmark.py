from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jasminsworldcupblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='bookmark',
            field=models.ManyToManyField(blank=True, related_name='blog_bookmark', to=settings.AUTH_USER_MODEL),
        ),
    ]
