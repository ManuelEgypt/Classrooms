# Generated by Django 2.1.5 on 2019-08-28 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_classroom_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other'), ('alien', 'alien')], default='alien', max_length=120)),
                ('exam_grade', models.FloatField()),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Classroom')),
            ],
        ),
    ]
