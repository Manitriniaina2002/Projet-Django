import os
from sys import modules
import uuid
import csv
from django.shortcuts import *
from django.conf import settings
from home.models import *
from home.forms import *
from django.http import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models import Q
# Create your views here.

def index(request):   
    return render(request, 'pages/dashboard.html')

def search_formation(request):
    query = request.GET.get('q', '')
    page = request.GET.get('page', 1)
    formations = Formation.objects.filter(
        Q(id_formation__icontains=query) |
        Q(nom__icontains=query) |
        Q(nbrdemodule__icontains=query) |
        Q(duree__icontains=query) 
        # Q(id_formateur__icontains=query)
    )
    paginator = Paginator(formations, 4)  # 4 formations par page
    page_obj = paginator.get_page(page)
    formations_list = list(page_obj.object_list.values('id_formation', 'nom', 'nbrdemodule', 'duree', 'id_formateur'))
    return JsonResponse({
        'formations': formations_list,
        'has_previous': page_obj.has_previous(),
        'has_next': page_obj.has_next(),
        'previous_page_number': page_obj.previous_page_number() if page_obj.has_previous() else None,
        'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None,
    })

def formation_view(request):
    resultat_list = Formation.objects.all()

    paginator = Paginator(resultat_list, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'pages/wallet.html', {'page_obj': page_obj})

def Ajout_Formation(request):
    if request.method == 'POST':
        print(request.POST)  
        fm = AjoutFormationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Ajout effectue avec success !")
            return redirect('wallet')
        else:
            return render(request,'pages/Ajout_Formation.html', {'form':fm})
    else:
        fm = AjoutFormationForm()
        return render(request,'pages/Ajout_Formation.html', {'form':fm})
    
def Modif_Formation(request,id_formation):
    if request.method == 'POST':
        # Modifier les données de la base de données
        formation = Formation.objects.get(id_formation=id_formation)
        formation.nom = request.POST['nom']
        formation.nbrdemodule = request.POST['nbrdemodule']
        formation.duree = request.POST['duree']
        
        id_formateur = request.POST['id_formateur']  # Notez que c'est 'formateur', pas 'id_formateur'
        formateur = Formateur.objects.get(id_formateur=id_formateur)
        formation.id_formateur = formateur  # Assigner l'instance du formateur, pas l'ID
        
        formation.save()
        messages.success(request,"Modification effectue avec success !")
        return redirect('wallet')
    else:
        formation = Formation.objects.get(id_formation=id_formation)
        fm = AjoutFormationForm(instance=formation)
        return render(request,'pages/Modif_Formation.html', {'form':fm}) 

def Supp_Formation(request,id_formation):
    FormationData = Formation.objects.get(id_formation=id_formation)
    if request.method == 'POST':
        FormationData.delete()
        return redirect('wallet')
    else:
        return render(request,'pages/wallet.html',{
            'message': 'Êtes-vous sûr de vouloir supprimer la formation "{}" ?'.format(
                FormationData.nom,
            ),
        },)   
def search_modules(request):
    query = request.GET.get('q', '')
    page = request.GET.get('page', 1)
    modules = Module.objects.filter(
        Q(id_module__icontains=query) |
        Q(nom__icontains=query) |
        Q(id_formation__icontains=query) 
    )
    paginator = Paginator(modules, 4)  # 4 formations par page
    page_obj = paginator.get_page(page)
    modules_list = list(page_obj.object_list.values('id_module', 'nom', 'id_formation'))
    return JsonResponse({
        'modules': modules_list,
        'has_previous': page_obj.has_previous(),
        'has_next': page_obj.has_next(),
        'previous_page_number': page_obj.previous_page_number() if page_obj.has_previous() else None,
        'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None,
    })


def Modules_view(request):
    resultat_list = Module.objects.all()

    paginator = Paginator(resultat_list, 4) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'pages/Module.html', {'page_obj': page_obj})

def Ajout_Module(request):
    fm = ModuleForm
    if request.method == 'POST':
        fm = ModuleForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('Modules')
        else:
            return render(request,'pages/Ajout_Module.html', {'form':fm})
    else:
        return render(request,'pages/Ajout_Module.html', {'form':fm})

def Modif_Module(request,id_module):
    if request.method == 'POST':
        # Modifier les données de la base de données
        data = Module.objects.get(id_module=id_module)
        data.nom = request.POST['nom']
        data.id_formation= request.POST['id_formation']
        data.save()
        return redirect('Modules')
    else:
        data = Module.objects.get(id_module=id_module)
        fm = ModuleForm(instance=data)
        return render(request,'pages/Modif_Module.html', {'form':fm}) 


def Supp_Module(request,id_module):
    if request.method == 'POST':
        ModuleData= Module.objects.get(id_module=id_module)
        ModuleData.delete()
        return redirect('Modules')
    else:
       return render(request,'pages/Module.html')  

# def search_ecolage(request):
#     query = request.GET.get('q', '')
#     page = request.GET.get('page', 1)
#     ecolages = Ecolage.objects.filter(
#         Q(id_ecolage__icontains=query) |
#         Q(valeur__icontains=query) |
#         Q(id_module__icontains=query) 
#     )
#     paginator = Paginator(ecolages, 4)  # 4 formations par page
#     page_obj = paginator.get_page(page)
#     ecolages_list = list(page_obj.object_list.values('id_ecolage', 'valeur', 'id_module'))
#     return JsonResponse({
#         'ecolages': ecolages_list,
#         'has_previous': page_obj.has_previous(),
#         'has_next': page_obj.has_next(),
#         'previous_page_number': page_obj.previous_page_number() if page_obj.has_previous() else None,
#         'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None,
#     })

# def Ecolage_view(request):
#     resultat_list = Ecolage.objects.all()

#     paginator = Paginator(resultat_list, 4) 
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
       
#     return render(request, 'pages/Ecolage.html', {'page_obj': page_obj})

# def Ajout_Ecolage(request):
#     fm = EcolageForm
#     if request.method == 'POST':
#         fm = EcolageForm(request.POST)
#         if fm.is_valid():
#             fm.save()
#             return redirect('Ecolage')
#         else:
#             return render(request,'pages/Ajout_Ecolage.html', {'form':fm})
#     else:
#         return render(request,'pages/Ajout_Ecolage.html', {'form':fm})
    
# def Modif_Ecolage(request,id_ecolage):
#     if request.method == 'POST':
#         # Modifier les données de la base de données
#         data = Ecolage.objects.get(id_ecolage=id_ecolage)
#         data.valeur = request.POST['valeur']
#         data.id_module= request.POST['id_module']
#         data.save()
#         return redirect('Ecolage')
#     else:
#         data = Ecolage.objects.get(id_ecolage=id_ecolage)
#         fm = EcolageForm(instance=data)
#         return render(request,'pages/Modif_Ecolage.html', {'form':fm}) 


# def Supp_Ecolage(request, id_ecolage):
#     """Supprime un ecolage."""

#     # Contrôle d'accès
#     if not request.user.is_authenticated:
#         return redirect('login')

#     # Validation
#     if request.method == 'POST':
#         if not request.POST.get('confirmation'):
#             return render(request, 'pages/Ecolage.html', {'message': 'Vous devez confirmer la suppression'})

#     # Affichage de la page de confirmation
#     return render(request, 'pages/supp_confirm_ecolage.html', {'id_ecolage': id_ecolage})


   
# # def supp_confirm_ecolage(request, id_ecolage):
# #     ecolage = Ecolage.objects.get(pk=id_ecolage)

# #     if request.method == "POST":
# #         ecolage.delete()
# #         return redirect("Ecolage")

#     return render(request, "supp_confirm_ecolage.html", {"ecolage": ecolage})


# def Paiement_view(request):
    
#     return render(request, 'pages/Paiement.html')

# def Ajout_paiement(request):
#     fm = PaiementForm
#     if request.method == 'POST':
#         fm = PaiementForm(request.POST, request.FILES)
#         if fm.is_valid():
#             fm.save()
#             return redirect('Paiement')
#         else:
#             return render(request,'pages/Ajout_paiement.html', {'form':fm})
#     else:
#         return render(request,'pages/Ajout_paiement.html', {'form':fm})
    
# def Modif_paiement(request,id_paiement):
#     if request.method == 'POST':
#         # Modifier les données de la base de données
#         data = Paiement.objects.get(id_paiement=id_paiement)
#         data.id_eleve = request.POST['id_eleve']
#         data.id_ecolage= request.POST['id_ecolage']
#         data.photo = request.POST['photo']
#         data.montant= request.POST['montant']
#         data.save()
#         return redirect('Paiement')
#     else:
#         data = Paiement.objects.get(id_paiement=id_paiement)
#         fm = PaiementForm(instance=data)
#         return render(request,'pages/Modif_paiement.html', {'form':fm}) 


# def Supp_paiement(request,id_paiement):
#     if request.method == 'POST':
#         ModuleData= Paiement.objects.get(id_paiement=id_paiement)
#         ModuleData.delete()
#         return redirect('Paiement')
#     else:
#        return render(request,'pages/Paiement.html') 

def search_salle(request):
    query = request.GET.get('q', '')
    page = request.GET.get('page', 1)
    salles = Salle.objects.filter(
        Q(id_salle__icontains=query) |
        Q(nom__icontains=query) |
        Q(occupation__icontains=query) |
        Q(id_formateur__icontains=query)
    )
    paginator = Paginator(salles, 4) 
    page_obj = paginator.get_page(page)
    salles_list = list(page_obj.object_list.values('id_salle', 'nom', 'occupation', 'id_formateur'))
    return JsonResponse({
        'salles': salles_list,
        'has_previous': page_obj.has_previous(),
        'has_next': page_obj.has_next(),
        'previous_page_number': page_obj.previous_page_number() if page_obj.has_previous() else None,
        'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None,
    })

def salle_view(request):
    resultat_list = Salle.objects.all()

    paginator = Paginator(resultat_list, 4) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 
    return render(request, 'pages/Salle.html', {'page_obj':page_obj})

def Ajout_Salle(request):
    fm = SalleForm
    if request.method == 'POST':
        fm = SalleForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('Salle')
        else:
            return render(request,'pages/Ajout_Salle.html', {'form':fm})
    else:
        return render(request,'pages/Ajout_Salle.html', {'form':fm})
    
def Modif_Salle(request,id_salle):
    if request.method == 'POST':
        # Modifier les données de la base de données
        data = Salle.objects.get(id_salle=id_salle)
        data.nom = request.POST['nom']
        data.occupation= request.POST['occupation']
        data.id_formateur = request.POST['id_formateur']
        data.save()
        return redirect('Salle')
    else:
        data = Salle.objects.get(id_salle=id_salle)
        fm = SalleForm(instance=data)
        return render(request,'pages/Modif_Salle.html', {'form':fm}) 


def Supp_Salle(request,id_salle):
    if request.method == 'POST':
        ModuleData= Salle.objects.get(id_salle=id_salle)
        ModuleData.delete()
        return redirect('Salle')
    else:
       return render(request,'pages/Salle.html') 

def search_presence(request):
    query = request.GET.get('q', '')
    page = request.GET.get('page', 1)
    presences = Participation.objects.filter(
        Q(id_eleve__icontains=query) |
        Q(photo__icontains=query) |
        Q(id_formation__icontains=query) |
        Q(heure__icontains=query) |
        Q(date_debut__icontains=query) |
        Q(date_fin__icontains=query)
    )
    paginator = Paginator(presences, 4) 
    page_obj = paginator.get_page(page)
    presences_list = list(page_obj.object_list.values('id_eleve', 'photo', 'id_formation', 'heure', 'date_debut', 'date_fin'))
    return JsonResponse({
        'presences': presences_list,
        'has_previous': page_obj.has_previous(),
        'has_next': page_obj.has_next(),
        'previous_page_number': page_obj.previous_page_number() if page_obj.has_previous() else None,
        'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None,
    })

def Presence_view(request):
    resultat_list = Participation.objects.all()

    paginator = Paginator(resultat_list, 4) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pages/Presence.html', {'page_obj': page_obj})

def Ajout_Presence(request):
    fm = ParticipationForm
    if request.method == 'POST':
        fm = ParticipationForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('Presence')
        else:
            return render(request,'pages/Ajout_Presence.html', {'form':fm})
    else:
        return render(request,'pages/Ajout_Presence.html', {'form':fm})
    
def Modif_Presence(request,id_eleve):
    if request.method == 'POST':
        # Modifier les données de la base de données
        data = Participation.objects.get(id_eleve=id_eleve)
        data.id_eleve = request.POST['id_eleve']
        # data.photo= request.POST['photo']
        data.id_formation = request.POST['id_formation']
        data.heure = request.POST['heure']
        data.date_debut = request.POST['date_debut']
        data.date_fin = request.POST['date_fin']
        data.save()
        return redirect('Presence')
    else:
        data = Participation.objects.get(id_eleve=id_eleve)
        fm = ParticipationForm(instance=data)
        return render(request,'pages/Modif_Presence.html', {'form':fm}) 


def Supp_Presence(request,id_eleve):
    if request.method == 'POST':
        ModuleData= Participation.objects.get(id_eleve=id_eleve)
        ModuleData.delete()
        return redirect('Presence')
    else:
       return render(request,'pages/Presence.html') 

def search_note(request):
    query = request.GET.get('q', '')
    page = request.GET.get('page', 1)
    notes = Note.objects.filter(
        Q(id_eleve__icontains=query) |
        Q(photo__icontains=query) |
        Q(id_formateur__icontains=query) |
        Q(note__icontains=query) 
    )
    paginator = Paginator(notes, 4) 
    page_obj = paginator.get_page(page)
    notes_list = list(page_obj.object_list.values('id_eleve', 'photo', 'id_formateur', 'note'))
    return JsonResponse({
        'notes': notes_list,
        'has_previous': page_obj.has_previous(),
        'has_next': page_obj.has_next(),
        'previous_page_number': page_obj.previous_page_number() if page_obj.has_previous() else None,
        'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None,
    })


def Note_view(request):
    resultat_list = Note.objects.all()

    paginator = Paginator(resultat_list, 4) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pages/Note.html', {'page_obj': page_obj})

def Ajout_Note(request):
    fm = NoteForm
    if request.method == 'POST':
        fm = NoteForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('Notes')
        else:
            return render(request,'pages/Ajout_Note.html', {'form':fm})
    else:
        return render(request,'pages/Ajout_Note.html', {'form':fm})
    
def Modif_Note(request,id_eleve):
    if request.method == 'POST':
        # Modifier les données de la base de données
        data = Note.objects.get(id_eleve=id_eleve)
        data.id_eleve = request.POST['id_eleve']
        data.id_formateur = request.POST['id_formateur']
        data.note = request.POST['note']
        data.save()
        return redirect('Notes')
    else:
        data = Note.objects.get(id_eleve=id_eleve)
        fm = NoteForm(instance=data)
        return render(request,'pages/Modif_Note.html', {'form':fm}) 


def Supp_Note(request,id_eleve):
    if request.method == 'POST':
        ModuleData= Note.objects.get(id_eleve=id_eleve)
        ModuleData.delete()
        return redirect('Notes')
    else:
       return render(request,'pages/Note.html') 


def Certification_view(request):
    eleves = Eleve.objects.all()
    return render(request, 'pages/Certification.html', {'eleves': eleves})

def convert_csv_to_text(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    text = ''
    for row in rows:
        text += ','.join(row) + '\n'

    return text

def get_files_from_directory(directory_path):
    files = []
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            try:
                print( ' > file_path ' + file_path)
                _, extension = os.path.splitext(filename)
                if extension.lower() == '.csv':
                    csv_text = convert_csv_to_text(file_path)
                else:
                    csv_text = ''

                files.append({
                    'file': file_path.split(os.sep + 'media' + os.sep)[1],
                    'filename': filename,
                    'file_path': file_path,
                    'csv_text': csv_text
                })
            except Exception as e:
                print( ' > ' +  str( e ) )    
    return files

def save_info(request, file_path):
    path = file_path.replace('%slash%', '/')
    if request.method == 'POST':
        FileInfo.objects.update_or_create(
            path=path,
            defaults={
                'info': request.POST.get('info')
            }
        )
    
    return redirect(request.META.get('HTTP_REFERER'))

def get_breadcrumbs(request):
    path_components = [component for component in request.path.split("/") if component]
    breadcrumbs = []
    url = ''

    for component in path_components:
        url += f'/{component}'
        if component == "file-manager":
            component = "media"
        breadcrumbs.append({'name': component, 'url': url})

    return breadcrumbs

def search_formateur(request):
    query = request.GET.get('q', '')
    page = request.GET.get('page', 1)
    formateurs = Formateur.objects.filter(
        Q(id_formateur__icontains=query) |
        Q(nom__icontains=query) |
        Q(prenom__icontains=query) |
        Q(contact__icontains=query) |
        Q(specialite__icontains=query)
    )
    paginator = Paginator(formateurs, 4)  # 4 formations par page
    page_obj = paginator.get_page(page)
    formateurs_list = list(page_obj.object_list.values('id_formateur', 'nom', 'prenom', 'contact', 'specialite'))
    return JsonResponse({
        'formateurs': formateurs_list,
        'has_previous': page_obj.has_previous(),
        'has_next': page_obj.has_next(),
        'previous_page_number': page_obj.previous_page_number() if page_obj.has_previous() else None,
        'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None,
    })

def file_manager(request, directory=''):
    resultat_list = Formateur.objects.all()

    paginator = Paginator(resultat_list, 4) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pages/file-manager.html',{'page_obj': page_obj})

def Ajout_Formateur(request):
    fm = FormateurForm
    if request.method == 'POST':
        fm = FormateurForm(request.POST)
        if fm.is_valid():
            fm.save()
            resultat= Formateur.objects.all()
            return render(request, 'pages/file-manager.html',{'Formateur': resultat})
        else:
            return render(request,'pages/Ajout_Formateur.html', {'form':fm})
    else:
        return render(request,'pages/Ajout_Formateur.html', {'form':fm})

def Modif_Formateur(request,id_formateur):
    if request.method == 'POST':
        # Modifier les données de la base de données
        formation = Formateur.objects.get(id_formateur=id_formateur)
        formation.nom = request.POST['nom']
        formation.prenom = request.POST['prenom']
        formation.contact = request.POST['contact']
        formation.specialite= request.POST['specialite']
        formation.save()
        messages.success(request,"Modification effectue avec success !")
        resultat= Formateur.objects.all()
        return render(request, 'pages/file-manager.html',{'Formateur': resultat})
    else:
        formation = Formateur.objects.get(id_formateur=id_formateur)
        fm = FormateurForm(instance=formation)
        return render(request,'pages/Modif_Formateur.html', {'form':fm}) 

def Supp_Formateur(request,id_formateur):
    if request.method == 'POST':
        FormationData= Formateur.objects.get(id_formateur =id_formateur )
        FormationData.delete()
        resultat= Formateur.objects.all()
        return render(request, 'pages/file-manager.html',{'Formateur': resultat})



def generate_nested_directory(root_path, current_path):
    directories = []
    for name in os.listdir(current_path):
        if os.path.isdir(os.path.join(current_path, name)):
            unique_id = str(uuid.uuid4())
            nested_path = os.path.join(current_path, name)
            nested_directories = generate_nested_directory(root_path, nested_path)
            directories.append({'id': unique_id, 'name': name, 'path': os.path.relpath(nested_path, root_path), 'directories': nested_directories})
    return directories


def delete_file(request, file_path):
    path = file_path.replace('%slash%', '/')
    absolute_file_path = os.path.join(settings.MEDIA_ROOT, path)
    os.remove(absolute_file_path)
    print("File deleted", absolute_file_path)
    return redirect(request.META.get('HTTP_REFERER'))

    
def download_file(request, file_path):
    path = file_path.replace('%slash%', '/')
    absolute_file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(absolute_file_path):
        with open(absolute_file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(absolute_file_path)
            return response
    raise Http404

def upload_file(request):
    media_path = os.path.join(settings.MEDIA_ROOT)
    selected_directory = request.POST.get('directory', '') 
    selected_directory_path = os.path.join(media_path, selected_directory)
    if request.method == 'POST':
        file = request.FILES.get('file')
        file_path = os.path.join(selected_directory_path, file.name)
        with open(file_path, 'wb') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

    return redirect(request.META.get('HTTP_REFERER'))

def search_Eleve(request):
    query = request.GET.get('q', '')
    page = request.GET.get('page', 1)
    eleves = Eleve.objects.filter(
        Q(id_eleve__icontains=query) |
        Q(nom__icontains=query) |
        Q(prenom__icontains=query) |
        Q(datedenaissance__icontains=query) |
        Q(lieudenaissance__icontains=query) |
        Q(adresse__icontains=query) |
        Q(numerodetelephone__icontains=query) |
        Q(e_mail__icontains=query) |
        Q(niveau__icontains=query)
    )
    paginator = Paginator(eleves, 4)  
    page_obj = paginator.get_page(page)
    eleves_list = list(page_obj.object_list.values('id_eleve','photo', 'nom', 'prenom', 'datedenaissance', 'lieudenaissance', 'adresse', 'numerodetelephone', 'e_mail', 'niveau'))
    return JsonResponse({
        'eleves': eleves_list,
        'has_previous': page_obj.has_previous(),
        'has_next': page_obj.has_next(),
        'previous_page_number': page_obj.previous_page_number() if page_obj.has_previous() else None,
        'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None,
    })

def Eleve_view(request):
    resultat_list = Eleve.objects.all()

    paginator = Paginator(resultat_list, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'pages/rtl.html', {'page_obj': page_obj})

def Ajout_Eleve(request):
    if request.method == 'POST':
        print(request.POST)  
        fm = EleveForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Ajout effectue avec success !")
            return redirect('rtl')
        else:
            return render(request,'pages/Ajout_Eleve.html', {'form':fm})
    else:
        fm = EleveForm()
        return render(request,'pages/Ajout_Eleve.html', {'form':fm})
    
def Modif_Eleve(request,id_eleve):
    if request.method == 'POST':
        # Modifier les données de la base de données
        eleve = Eleve.objects.get(id_eleve=id_eleve)
        eleve.nom = request.POST['nom']
        eleve.prenom = request.POST['prenom']
        eleve.datedenaissance = request.POST['datedenaissance']
        eleve.lieudenaissance = request.POST['lieudenaissance']
        eleve.adresse = request.POST['adresse']
        eleve.numerodetelephone = request.POST['numerodetelephone']
        eleve.e_mail = request.POST['e_mail']
        eleve.niveau = request.POST['niveau']
        
        eleve.save()
        messages.success(request,"Modification effectue avec success !")
        return redirect('rtl')
    else:
        eleve = Eleve.objects.get(id_eleve=id_eleve)
        fm = EleveForm(instance=eleve)
        return render(request,'pages/Modif_Eleve.html', {'form':fm}) 

def Supp_Eleve(request,id_eleve):
    EleveData = Eleve.objects.get(id_eleve=id_eleve)
    if request.method == 'POST':
        EleveData.delete()
        return redirect('rtl')
    else:
        return render(request,'pages/rtl.html',{
            'message': 'Êtes-vous sûr de vouloir supprimer l\'eleve "{}" ?'.format(
                EleveData.nom,
            ),
        },)
        
def Inscription(request):
    if request.method == 'POST':
        print(request.POST)  
        fm = EleveForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Ajout effectue avec success !")
            return redirect('rtl')
        else:
            return render(request,'pages/tables.html', {'form':fm})
    else:
        fm = EleveForm()
        return render(request,'pages/tables.html', {'form':fm})