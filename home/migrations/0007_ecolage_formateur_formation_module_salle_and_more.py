# Generated by Django 4.2.6 on 2023-10-30 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_delete_ecolage_delete_eleve_delete_formateur_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ecolage',
            fields=[
                ('id_ecolage', models.AutoField(db_column='Id_Ecolage', primary_key=True, serialize=False)),
                ('valeur', models.BigIntegerField(db_column='Valeur')),
                ('id_module', models.IntegerField(db_column='Id_Module', unique=True)),
            ],
            options={
                'db_table': 'ecolage',
            },
        ),
        migrations.CreateModel(
            name='Formateur',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(db_column='Nom', max_length=25)),
                ('prenom', models.CharField(db_column='Prenom', max_length=25)),
                ('contact', models.CharField(db_column='Contact', max_length=10)),
                ('specialite', models.CharField(db_column='Specialite', max_length=20)),
            ],
            options={
                'db_table': 'formateur',
            },
        ),
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(db_column='Nom', max_length=25)),
                ('nbrdemodule', models.IntegerField(db_column='NbrDeModule')),
                ('duree', models.CharField(db_column='Duree', max_length=10)),
                ('formateur', models.CharField(db_column='Formateur', max_length=25)),
            ],
            options={
                'db_table': 'formation',
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id_module', models.AutoField(db_column='Id_Module', primary_key=True, serialize=False)),
                ('nom', models.CharField(blank=True, db_column='Nom', max_length=50, null=True)),
                ('id_formation', models.IntegerField(db_column='Id_Formation')),
            ],
            options={
                'db_table': '_module',
            },
        ),
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id_salle', models.AutoField(db_column='Id_Salle', primary_key=True, serialize=False)),
                ('nom', models.CharField(blank=True, db_column='Nom', max_length=25, null=True)),
                ('occupation', models.CharField(db_column='Occupation', max_length=5)),
                ('id_formateur', models.IntegerField(blank=True, db_column='Id_Formateur', null=True)),
            ],
            options={
                'db_table': 'salle',
            },
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id_eleve', models.IntegerField(db_column='Id_Eleve', primary_key=True, serialize=False)),
                ('photo', models.CharField(db_column='Photo', max_length=50)),
                ('id_formation', models.IntegerField(db_column='Id_Formation')),
                ('heure', models.TimeField(blank=True, db_column='Heure', null=True)),
                ('date_debut', models.DateField(db_column='Date_debut')),
                ('date_fin', models.DateField(db_column='Date_fin')),
            ],
            options={
                'db_table': 'participation',
                'unique_together': {('id_eleve', 'photo', 'id_formation')},
            },
        ),
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('id_eleve', models.IntegerField(db_column='Id_Eleve', primary_key=True, serialize=False)),
                ('photo', models.CharField(db_column='Photo', max_length=50)),
                ('id_ecolage', models.IntegerField(db_column='Id_Ecolage')),
                ('montant', models.BigIntegerField(blank=True, db_column='Montant', null=True)),
            ],
            options={
                'db_table': 'paiement',
                'unique_together': {('id_eleve', 'photo', 'id_ecolage')},
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id_eleve', models.IntegerField(db_column='Id_Eleve', primary_key=True, serialize=False)),
                ('photo', models.CharField(db_column='Photo', max_length=50)),
                ('id_formateur', models.IntegerField(db_column='Id_Formateur')),
                ('note', models.CharField(db_column='Note', max_length=50)),
            ],
            options={
                'db_table': 'note',
                'unique_together': {('id_eleve', 'photo', 'id_formateur')},
            },
        ),
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('id_eleve', models.AutoField(db_column='Id_Eleve', primary_key=True, serialize=False)),
                ('photo', models.CharField(db_column='Photo', max_length=50)),
                ('nom', models.CharField(blank=True, db_column='Nom', max_length=50, null=True)),
                ('prenom', models.CharField(blank=True, db_column='Prenom', max_length=50, null=True)),
                ('datedenaissance', models.DateField(blank=True, db_column='DateDeNaissance', null=True)),
                ('lieudenaissance', models.CharField(blank=True, db_column='LieuDeNaissance', max_length=50, null=True)),
                ('adresse', models.CharField(blank=True, db_column='Adresse', max_length=50, null=True)),
                ('numerodetelephone', models.IntegerField(blank=True, db_column='NumeroDeTelephone', null=True)),
                ('e_mail', models.CharField(blank=True, db_column='E_mail', max_length=50, null=True)),
                ('niveau', models.CharField(blank=True, db_column='Niveau', max_length=25, null=True)),
            ],
            options={
                'db_table': 'eleve',
                'unique_together': {('id_eleve', 'photo')},
            },
        ),
    ]
