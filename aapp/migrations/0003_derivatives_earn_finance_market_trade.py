# Generated by Django 3.1.6 on 2022-02-17 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aapp', '0002_nft'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Trade')),
                ('serial_date', models.DateTimeField(verbose_name='Date')),
                ('description', models.TextField(blank=True)),
                ('approved', models.BooleanField(default=False, verbose_name='Aprroved')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aapp.user')),
                ('serial', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aapp.serial')),
            ],
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Market')),
                ('serial_date', models.DateTimeField(verbose_name='Date')),
                ('description', models.TextField(blank=True)),
                ('approved', models.BooleanField(default=False, verbose_name='Aprroved')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aapp.user')),
                ('serial', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aapp.serial')),
            ],
        ),
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Finance')),
                ('serial_date', models.DateTimeField(verbose_name='Date')),
                ('description', models.TextField(blank=True)),
                ('approved', models.BooleanField(default=False, verbose_name='Aprroved')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aapp.user')),
                ('serial', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aapp.serial')),
            ],
        ),
        migrations.CreateModel(
            name='Earn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Earn')),
                ('serial_date', models.DateTimeField(verbose_name='Date')),
                ('description', models.TextField(blank=True)),
                ('approved', models.BooleanField(default=False, verbose_name='Aprroved')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aapp.user')),
                ('serial', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aapp.serial')),
            ],
        ),
        migrations.CreateModel(
            name='Derivatives',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Derivatives')),
                ('serial_date', models.DateTimeField(verbose_name='Date')),
                ('description', models.TextField(blank=True)),
                ('approved', models.BooleanField(default=False, verbose_name='Aprroved')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aapp.user')),
                ('serial', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aapp.serial')),
            ],
        ),
    ]
