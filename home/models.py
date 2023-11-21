from django.db import models

# Create your models here.

class FileInfo(models.Model):
    path = models.URLField()
    info = models.CharField(max_length=255)

    def __str__(self):
        return self.path
    
class Formateur(models.Model):
    id_formateur = models.AutoField(db_column='Id_Formateur', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prenom = models.CharField(db_column='Prenom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=50, blank=True, null=True)  # Field name made lowercase.
    specialite = models.CharField(db_column='Specialite', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'formateur'

    def __str__(self):
        return str(self.id_formateur)

class Module(models.Model):
    id_module = models.AutoField(db_column='Id_Module', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_formation = models.IntegerField(db_column='Id_Formation')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = '_module'

class Ecolage(models.Model):
    id_ecolage = models.AutoField(db_column='Id_Ecolage', primary_key=True)  # Field name made lowercase.
    valeur = models.BigIntegerField(db_column='Valeur')  # Field name made lowercase.
    id_module = models.IntegerField(db_column='Id_Module', unique=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ecolage'
        
# class Paiement(models.Model):
#     id_paiement = models.AutoField(primary_key=True)
#     id_eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
#     photo = models.ImageField(upload_to='media/Photo_Eleve')
#     id_ecolage = models.ForeignKey(Ecolage, on_delete=models.CASCADE)
#     montant = models.BigIntegerField(blank=True, null=True) 

#     class Meta:
#         managed = True
#         db_table = 'paiement'
#         unique_together = (('id_eleve', 'photo', 'id_ecolage'),)


class Eleve(models.Model):
    id_eleve = models.AutoField(db_column='Id_Eleve', primary_key=True)  # Field name made lowercase. The composite primary key (Id_Eleve, Photo) found, that is not supported. The first column is selected.
    photo = models.CharField(db_column='Photo', max_length=255)  # Field name made lowercase.
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



class Formation(models.Model):
    id_formation = models.AutoField(db_column='Id_Formation', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nbrdemodule = models.IntegerField(db_column='NbrDeModule', blank=True, null=True)  # Field name made lowercase.
    duree = models.CharField(db_column='Duree', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_formateur = models.ForeignKey(Formateur, on_delete=models.CASCADE, db_column='Id_Formateur')

    class Meta:
        managed = True
        db_table = 'formation'


class Note(models.Model):
    id_eleve = models.IntegerField(db_column='Id_Eleve', primary_key=True)  # Field name made lowercase. The composite primary key (Id_Eleve, Photo, Id_Formateur) found, that is not supported. The first column is selected.
    photo = models.CharField(db_column='Photo', max_length=255)  # Field name made lowercase.
    id_formateur = models.IntegerField(db_column='Id_Formateur')  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'note'
        unique_together = (('id_eleve', 'photo', 'id_formateur'),)





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