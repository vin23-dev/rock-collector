# Generated by Django 3.0.4 on 2020-03-18 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_quality'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rarity', models.CharField(choices=[('R', 'Rough'), ('F', 'Fair'), ('P', 'Pristine')], default='R', max_length=1)),
            ],
        ),
        migrations.AlterModelOptions(
            name='quality',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='quality',
            name='date',
            field=models.DateField(verbose_name='date found'),
        ),
        migrations.AddField(
            model_name='rock',
            name='region',
            field=models.ManyToManyField(to='main_app.Region'),
        ),
    ]
