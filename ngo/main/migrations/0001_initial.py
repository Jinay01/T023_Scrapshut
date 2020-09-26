# Generated by Django 3.1.1 on 2020-09-26 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0002_donor_name_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='requirements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('medicine', 'medicine'), ('equipment', 'equipment')], max_length=20)),
                ('count', models.IntegerField()),
                ('ngo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.ngo')),
            ],
        ),
    ]
