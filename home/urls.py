from django.urls import path, re_path

from . import views

urlpatterns = [
    path('search_formation/', views.search_formation, name='search_formation'),
    path('search_modules/', views.search_modules, name='search_modules'),
    # path('search_ecolage/', views.search_ecolage, name='search_ecolage'),
    path('search_formateur/', views.search_formateur, name='search_formateur'),
    path('search_salle/', views.search_salle, name='search_salle'),
    path('search_presence/', views.search_presence, name='search_presence'),
    path('search_note/', views.search_note, name='search_note'),
    path('search_Eleve/', views.search_Eleve, name='search_Eleve'),
    
    
    path('', views.index, name='index'),
    path('file-manager/', views.file_manager, name='file-manager'),
    re_path(r'^file-manager/(?P<directory>.*)?/$', views.file_manager, name='file_manager'),
    path('delete-file/<str:file_path>/', views.delete_file, name='delete_file'),
    path('download-file/<str:file_path>/', views.download_file, name='download_file'),
    path('upload-file/', views.upload_file, name='upload_file'),
    path('save-info/<str:file_path>/', views.save_info, name='save_info'),
    path("wallet/",views.formation_view, name="wallet"),
    path("Modules/",views.Modules_view, name="Modules"),
    # path("Ecolage/",views.Ecolage_view, name="Ecolage"),
    # path("Paiement/",views.Paiement_view, name="Paiement"),
    path("Salle/",views.salle_view, name="Salle"),
    path("Presence/",views.Presence_view, name="Presence"),
    path("Notes/",views.Note_view, name="Notes"),
    path("rtl/",views.Eleve_view, name="rtl"),
    path("Certification/",views.Certification_view, name="Certification"),
    
    #Ajout
    path("Ajout_Formation/",views.Ajout_Formation, name="Ajout_Formation"),
    path("Ajout_Formateur/",views.Ajout_Formateur, name="Ajout_Formateur"),
    path("Ajout_Module/",views.Ajout_Module, name="Ajout_Module"),
    # path("Ajout_Ecolage/",views.Ajout_Ecolage, name="Ajout_Ecolage"),
    # path("Ajout_paiement/",views.Ajout_paiement, name="Ajout_paiement"),
    path("Ajout_Salle/",views.Ajout_Salle, name="Ajout_Salle"),
    path("Ajout_Presence/",views.Ajout_Presence, name="Ajout_Presence"),
    path("Ajout_Note/",views.Ajout_Note, name="Ajout_Note"),
    path("Ajout_Eleve/",views.Ajout_Eleve, name="Ajout_Eleve"),
    path("tables/",views.Inscription, name="tables"),
    
    #Suppression
    path('Supp_Formation/<int:id_formation>/', views.Supp_Formation, name='Supp_Formation'),
    path('Supp_Formateur/<int:id_formateur>/', views.Supp_Formateur, name='Supp_Formateur'),
    path('Supp_Module/<int:id_module>/', views.Supp_Module, name='Supp_Module'),
    # path('Supp_Ecolage/<int:id_ecolage>/', views.Supp_Ecolage, name='Supp_Ecolage'),
    # path('Supp_paiement/<int:id_paiement>/', views.Supp_paiement, name='Supp_paiement'),
    path('Supp_Salle/<int:id_salle>/', views.Supp_Salle, name='Supp_Salle'),
    path('Supp_Presence/<int:id_eleve>/', views.Supp_Presence, name='Supp_Presence'),
    path('Supp_Note/<int:id_eleve>/', views.Supp_Note, name='Supp_Note'),
    path('Supp_Eleve/<int:id_eleve>/', views.Supp_Eleve, name='Supp_Eleve'),
    
    ##Modification
    path("Modif_Formation/<int:id_formation>/", views.Modif_Formation, name="Modif_Formation"),
    path("Modif_Formateur/<int:id_formateur>/", views.Modif_Formateur, name="Modif_Formateur"),
    path("Modif_Module/<int:id_module>/", views.Modif_Module, name="Modif_Module"),
    # path("Modif_Ecolage/<int:id_ecolage>/", views.Modif_Ecolage, name="Modif_Ecolage"),
    # path("Modif_paiement/<int:id_paiement>/", views.Modif_paiement, name="Modif_paiement"),
    path("Modif_Salle/<int:id_salle>/", views.Modif_Salle, name="Modif_Salle"),
    path("Modif_Presence/<int:id_eleve>/", views.Modif_Presence, name="Modif_Presence"),
    path("Modif_Note/<int:id_eleve>/", views.Modif_Note, name="Modif_Note"),
    path("Modif_Eleve/<int:id_eleve>/", views.Modif_Eleve, name="Modif_Eleve"),
    
]