from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_xp', models.IntegerField(default=0)),
                ('streak_days', models.IntegerField(default=0)),
                ('last_completed_date', models.DateField(blank=True, null=True)),
                ('language', models.CharField(choices=[('ar', 'Arabic'), ('en', 'English')], default='ar', max_length=2)),
                ('quran_daily_target', models.IntegerField(default=5)),
                ('sleep_target', models.FloatField(default=7.0)),
                ('water_target', models.IntegerField(default=8)),
                ('reading_target', models.IntegerField(default=30)),
                ('coding_target', models.IntegerField(default=60)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DailyProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('fajr', models.BooleanField(default=False)),
                ('dhuhr', models.BooleanField(default=False)),
                ('asr', models.BooleanField(default=False)),
                ('maghrib', models.BooleanField(default=False)),
                ('isha', models.BooleanField(default=False)),
                ('quran_pages', models.IntegerField(default=0)),
                ('morning_adhkar', models.BooleanField(default=False)),
                ('evening_adhkar', models.BooleanField(default=False)),
                ('workout_done', models.BooleanField(default=False)),
                ('workout_type', models.CharField(blank=True, default='', max_length=100)),
                ('sleep_hours', models.FloatField(default=0.0)),
                ('water_glasses', models.IntegerField(default=0)),
                ('reading_minutes', models.IntegerField(default=0)),
                ('books_pages', models.IntegerField(default=0)),
                ('english_minutes', models.IntegerField(default=0)),
                ('coding_minutes', models.IntegerField(default=0)),
                ('pomodoros_done', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daily_progress', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
                'unique_together': {('user', 'date')},
            },
        ),
        migrations.CreateModel(
            name='CustomTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('label', models.CharField(max_length=200)),
                ('done', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_tasks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
