# Generated by Django 4.2.7 on 2023-11-10 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("atalhos", "0007_alter_endereco_endereço_delete_pais"),
    ]

    operations = [
        migrations.AddField(
            model_name="endereco",
            name="rua",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.PROTECT, to="atalhos.rua"
            ),
        ),
    ]