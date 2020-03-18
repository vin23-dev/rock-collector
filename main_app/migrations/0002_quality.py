# Generated by Django 3.0.4 on 2020-03-18 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('quality', models.CharField(choices=[('R', 'Rough'), ('F', 'Fair'), ('P', 'Pristine')], default='R', max_length=1)),
                ('rock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Rock')),
            ],
        ),
    ]
