# Generated by Django 3.0.3 on 2020-03-05 11:45

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfBirth', models.DateField(blank=True, null=True)),
                ('profilePhoto', models.ImageField(blank=True, null=True, upload_to='static')),
                ('sex', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=1, null=True)),
                ('sport_preference', models.CharField(choices=[('HIKE', 'Hiking'), ('FB', 'Football'), ('BB', 'Basketball'), ('CYC', 'CYCLING')], max_length=4)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField()),
                ('ratedUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratedUser', to='connect.UserProfile')),
                ('ratingUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratingUser', to='connect.UserProfile')),
            ],
            options={
                'unique_together': {('ratingUser', 'ratedUser')},
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1', to='connect.UserProfile')),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user2', to='connect.UserProfile')),
            ],
            options={
                'unique_together': {('user2', 'user1')},
            },
        ),
    ]
