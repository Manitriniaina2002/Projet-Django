from django import forms
from .models import *

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ("nom", "id_formation")
        widgets = {
            'nom': forms.TextInput(attrs={'class':'form-control'}),
            'id_formation': forms.NumberInput(attrs={'class':'form-control'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        for field in self.fields:
            if not cleaned_data.get(field):
                self.add_error(field, "Ce champ est obligatoire !")
        
class EcolageForm(forms.ModelForm):
    class Meta:
       model = Ecolage
       fields = ("valeur", "id_module")
       widgets = {
           'valeur': forms.NumberInput(attrs={'class':'form-control'}),
           'id_module': forms.NumberInput(attrs={'class':'form-control'}),
       }
    def clean(self):
        cleaned_data = super().clean()
        for field in self.fields:
            if not cleaned_data.get(field):
                self.add_error(field, "Ce champ est obligatoire !")
       
# class PaiementForm(forms.ModelForm):
#     class Meta:
#         model = Paiement
#         fields = ("id_eleve", "photo", "id_ecolage", "montant")
#         widgets = {
#             'id_eleve': forms.NumberInput(attrs={'class':'form-control'}),
#             # Utilisation du widget par défaut pour le champ photo
#             # ou aucun widget spécifié pour laisser Django utiliser le widget par défaut
#             'photo': forms.FileInput(attrs={'class':'form-control'}),
#             # 'photo': forms.ImageField(),  # Essayez de supprimer cette ligne ou la commenter
#             'id_ecolage': forms.NumberInput(attrs={'class':'form-control'}),
#             'montant': forms.NumberInput(attrs={'class':'form-control'}),
#         }
    #   def clean(self):
    #     cleaned_data = super().clean()
    #     for field in self.fields:
    #         if not cleaned_data.get(field):
    #             self.add_error(field, "Ce champ est obligatoire !")

#     def clean_photo(self):
#         photo = self.cleaned_data['photo']
#         if photo is None:
#             raise forms.ValidationError("Veuillez sélectionner une image.")
#         return photo



class AjoutFormationForm(forms.ModelForm):
    # formateur = forms.ModelChoiceField(queryset=Formateur.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    
    class Meta:
        model = Formation
        fields = ("nom", "nbrdemodule", "duree", "id_formateur")
        widgets = {
            'nom': forms.TextInput(attrs={'class':'form-control'}),
            'nbrdemodule': forms.NumberInput(attrs={'class':'form-control'}),
            'duree': forms.TextInput(attrs={'class':'form-control'}),
            'id_formateur': forms.NumberInput(attrs={'class':'form-control'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        for field in self.fields:
            if not cleaned_data.get(field):
                self.add_error(field, "Ce champ est obligatoire !")



class FormateurForm(forms.ModelForm):
    class Meta:
        model = Formateur
        fields = ("nom", "prenom", "contact", "specialite")
        widgets = {
            'nom': forms.TextInput(attrs={'class':'form-control'}),
            'prenom': forms.TextInput(attrs={'class':'form-control'}),
            'contact': forms.TextInput(attrs={'class':'form-control'}),
            'specialite': forms.TextInput(attrs={'class':'form-control'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        for field in self.fields:
            if not cleaned_data.get(field):
                self.add_error(field, "Ce champ est obligatoire !")

class SalleForm(forms.ModelForm):
    class Meta:
        model = Salle
        fields = ("nom", "occupation", "id_formateur")
        widgets = {
            'nom': forms.TextInput(attrs={'class':'form-control'}),
            'occupation': forms.TextInput(attrs={'class':'form-control'}),
            'id_formateur': forms.NumberInput(attrs={'class':'form-control'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        for field in self.fields:
            if not cleaned_data.get(field):
                self.add_error(field, "Ce champ est obligatoire !")       

class ParticipationForm(forms.ModelForm):
    class Meta:
        model = Participation
        fields = ("id_eleve", "id_formation", "heure", "date_debut", "date_fin")
        widgets = {
            'id_eleve': forms.NumberInput(attrs={'class':'form-control'}),
            'id_formation': forms.NumberInput(attrs={'class':'form-control'}),
            'heure': forms.TimeInput(attrs={'class':'form-control', 'type': 'time'}),
            'date_debut': forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        for field in self.fields:
            if not cleaned_data.get(field):
                self.add_error(field, "Ce champ est obligatoire !")        

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ("id_eleve", "id_formateur", "note")
        widgets = {
            'id_eleve': forms.NumberInput(attrs={'class':'form-control'}),
            'id_formateur': forms.NumberInput(attrs={'class':'form-control'}),
            'note': forms.TextInput(attrs={'class':'form-control'}),
        }  
    def clean(self):
        cleaned_data = super().clean()
        for field in self.fields:
            if not cleaned_data.get(field):
                self.add_error(field, "Ce champ est obligatoire !")


from django import forms
from .models import Eleve

class EleveForm(forms.ModelForm):
    class Meta:
        model = Eleve
        fields = ['nom', 'prenom', 'datedenaissance', 'lieudenaissance', 'adresse', 'numerodetelephone', 'e_mail', 'niveau']
        widgets = {
            'nom': forms.TextInput(attrs={'class':'form-control'}),
            'prenom': forms.TextInput(attrs={'class':'form-control'}),
            'datedenaissance': forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
            'lieudenaissance': forms.TextInput(attrs={'class':'form-control'}),
            'adresse': forms.TextInput(attrs={'class':'form-control'}),
            'numerodetelephone': forms.TextInput(attrs={'class':'form-control'}),
            'e_mail': forms.EmailInput(attrs={'class':'form-control'}),
            'niveau': forms.TextInput(attrs={'class':'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        for field in self.fields:
            if not cleaned_data.get(field):
                self.add_error(field, "Ce champ est obligatoire !")