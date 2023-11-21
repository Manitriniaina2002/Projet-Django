# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Module(models.Model):
    id_module = models.AutoField(db_column='Id_Module', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_formation = models.IntegerField(db_column='Id_Formation')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = '_module'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = True
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class Ecolage(models.Model):
    id_ecolage = models.AutoField(db_column='Id_Ecolage', primary_key=True)  # Field name made lowercase.
    valeur = models.BigIntegerField(db_column='Valeur')  # Field name made lowercase.
    id_module = models.IntegerField(db_column='Id_Module', unique=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ecolage'


class Eleve(models.Model):
    id_eleve = models.AutoField(db_column='Id_Eleve', primary_key=True)  # Field name made lowercase. The composite primary key (Id_Eleve, Photo) found, that is not supported. The first column is selected.
    photo = models.CharField(db_column='Photo', max_length=50)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prenom = models.CharField(db_column='Prenom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datedenaissance = models.DateField(db_column='DateDeNaissance', blank=True, null=True)  # Field name made lowercase.
    lieudenaissance = models.CharField(db_column='LieuDeNaissance', max_length=50, blank=True, null=True)  # Field name made lowercase.
    adresse = models.CharField(db_column='Adresse', max_length=50, blank=True, null=True)  # Field name made lowercase.
    numerodetelephone = models.IntegerField(db_column='NumeroDeTelephone', blank=True, null=True)  # Field name made lowercase.
    e_mail = models.CharField(db_column='E_mail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    niveau = models.CharField(db_column='Niveau', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'eleve'
        unique_together = (('id_eleve', 'photo'),)


class Formateur(models.Model):
    id_formateur = models.AutoField(db_column='Id_Formateur', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prenom = models.CharField(db_column='Prenom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=50, blank=True, null=True)  # Field name made lowercase.
    specialite = models.CharField(db_column='Specialite', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'formateur'


class Formation(models.Model):
    id_formation = models.AutoField(db_column='Id_Formation', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nbrdemodule = models.IntegerField(db_column='NbrDeModule', blank=True, null=True)  # Field name made lowercase.
    duree = models.CharField(db_column='Duree', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_formateur = models.IntegerField(db_column='Id_Formateur')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'formation'


class Note(models.Model):
    id_eleve = models.IntegerField(db_column='Id_Eleve', primary_key=True)  # Field name made lowercase. The composite primary key (Id_Eleve, Photo, Id_Formateur) found, that is not supported. The first column is selected.
    photo = models.CharField(db_column='Photo', max_length=50)  # Field name made lowercase.
    id_formateur = models.IntegerField(db_column='Id_Formateur')  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'note'
        unique_together = (('id_eleve', 'photo', 'id_formateur'),)


class Paiement(models.Model):
    id_eleve = models.IntegerField(db_column='Id_Eleve', primary_key=True)  # Field name made lowercase. The composite primary key (Id_Eleve, Photo, Id_Ecolage) found, that is not supported. The first column is selected.
    photo = models.CharField(db_column='Photo', max_length=50)  # Field name made lowercase.
    id_ecolage = models.IntegerField(db_column='Id_Ecolage')  # Field name made lowercase.
    montant = models.BigIntegerField(db_column='Montant', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'paiement'
        unique_together = (('id_eleve', 'photo', 'id_ecolage'),)


class Participation(models.Model):
    id_eleve = models.IntegerField(db_column='Id_Eleve', primary_key=True)  # Field name made lowercase. The composite primary key (Id_Eleve, Photo, Id_Formation) found, that is not supported. The first column is selected.
    photo = models.CharField(db_column='Photo', max_length=50)  # Field name made lowercase.
    id_formation = models.IntegerField(db_column='Id_Formation')  # Field name made lowercase.
    heure = models.TimeField(db_column='Heure', blank=True, null=True)  # Field name made lowercase.
    date_debut = models.DateField(db_column='Date_debut')  # Field name made lowercase.
    date_fin = models.DateField(db_column='Date_fin')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'participation'
        unique_together = (('id_eleve', 'photo', 'id_formation'),)


class Salle(models.Model):
    id_salle = models.AutoField(db_column='Id_Salle', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=25, blank=True, null=True)  # Field name made lowercase.
    occupation = models.CharField(db_column='Occupation', max_length=5)  # Field name made lowercase.
    id_formateur = models.IntegerField(db_column='Id_Formateur', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'salle'
