# Generated by Django 5.1.2 on 2024-12-12 14:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neurodivergentes', '0007_alter_anamnese_neurodivergente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdi',
            name='neurodivergente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pdis', to='neurodivergentes.neurodivergente', verbose_name='Aluno/Paciente'),
        ),
    ]
