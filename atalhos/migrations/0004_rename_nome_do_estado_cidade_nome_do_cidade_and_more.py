# Generated by Django 4.2.7 on 2023-11-10 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("atalhos", "0003_estado_cidade_do_estado"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cidade",
            old_name="nome_do_estado",
            new_name="nome_do_cidade",
        ),
        migrations.AddField(
            model_name="bairro",
            name="nome_da_rua",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.PROTECT, to="atalhos.rua"
            ),
        ),
    ]