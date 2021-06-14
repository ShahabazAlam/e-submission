# Generated by Django 3.2 on 2021-04-24 04:59

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8')], default='')),
                ('name', models.CharField(max_length=200)),
                ('questions', models.TextField(max_length=1000)),
                ('num', models.IntegerField(default=1)),
                ('created', models.DateField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('deadline', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Computer', 'Computer'), ('IT', 'IT'), ('Civil', 'Civil'), ('Mechanical', 'Mechanical'), ('Electrical', 'Electrical')], default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity', models.CharField(choices=[('faculty', 'Faculty'), ('student', 'Student')], default='', max_length=100)),
                ('department', models.CharField(choices=[('Computer', 'Computer'), ('IT', 'IT'), ('Civil', 'Civil'), ('Mechanical', 'Mechanical'), ('Electrical', 'Electrical')], default='', max_length=100)),
                ('full_name', models.CharField(max_length=100)),
                ('semester', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8')], default='')),
                ('enrollment', models.CharField(max_length=8, unique=True)),
                ('created', models.DateField(editable=False, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_date', models.DateField()),
                ('title', models.CharField(default='', max_length=200)),
                ('body', models.TextField(default='', max_length=10000)),
                ('points', models.FloatField(default=0.0)),
                ('comments', models.CharField(default='', max_length=1000)),
                ('uploadfile', models.FileField(default='', upload_to='media/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'doc'])])),
                ('worked', models.BooleanField(default=False)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.assignment')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='application.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='department',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='application.course'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='faculty',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='application.userprofile'),
        ),
    ]