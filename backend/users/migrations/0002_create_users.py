# Generated by Django 4.2.5 on 2023-09-15 22:04

from django.db import migrations


def create_users(apps, schema_editor):
    User = apps.get_model("users", "User")
    User.objects.create(name="Emma", age=25, address="testaddress1", points=0)
    User.objects.create(name="Noah", age=30, address="testaddress2", points=0)
    User.objects.create(name="James", age=35, address="testaddress3", points=0)
    User.objects.create(name="William", age=40,
                        address="testaddress4", points=0)
    User.objects.create(name="Olivia", age=45,
                        address="testaddress5", points=0)


def delete_users(apps, schema_editor):
    User = apps.get_model("users", "User")
    User.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_users, delete_users),
    ]