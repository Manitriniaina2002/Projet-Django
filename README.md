# [C.O.S.T.M - Formation Management System](https://github.com/Manitriniaina2002/Projet-Django/)

Open-source **Django** project for managing training courses, trainers, students, classrooms, and attendance tracking. Built on **[Corporate Dashboard](https://appseed.us/product/corporate-dashboard/django/)**, an open-source `Bootstrap 5` design from [Creative-Tim](https://www.creative-tim.com/product/corporate-ui-dashboard?AFFILIATE=128200).

C.O.S.T.M - **Centre d'Orientation du Système et Technologie Moderne** - A complete training management solution with modern responsive design, built with Django and Bootstrap 5.

> 👉 **System**: C.O.S.T.M - Formation Management & Attendance Tracking
  
<br />

### Features

- ✅ **Formation Management** - Create and manage training courses with modules
  - Add formateurs (trainers) and manage their specialties
  - Organize students (élèves) into groups
  - Assign classrooms (salles) to formations
  - Track attendance and participation
- ✅ **Responsive Design** - Mobile-first Bootstrap 5 interface
- ✅ Modern **Dashboard** with statistics and quick access
- ✅ **Search & Pagination** - Quick search across all entities
- ✅ **Authentication**: `Django.contrib.AUTH`, User registration

<br /> 

## Formation Management System - Dashboard & Features

The C.O.S.T.M system provides a complete solution for managing training programs with a modern, responsive interface.

<br />

## Manual Build 

> 👉 Download the code  

```bash
$ git clone https://github.com/Manitriniaina2002/Projet-Django.git
$ cd Projet-Django
```

<br />

> 👉 Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> 👉 Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> 👉 Create the Superuser

```bash
$ python manage.py createsuperuser
```

<br />

> 👉 Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

## Codebase structure

The project is coded using a simple and intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- core/                            
   |    |-- settings.py   # Project Configuration  
   |    |-- urls.py       # Project Routing
   |
   |-- home/
   |    |-- views.py      # APP Views 
   |    |-- urls.py       # APP Routing
   |    |-- models.py     # APP Models 
   |    |-- tests.py      # Tests  
   |     
   |-- templates/
   |    |-- includes/     # UI components 
   |    |-- layouts/      # Masterpages
   |    |-- pages/        # Kit pages 
   |
   |-- static/   
   |    |-- css/                                   # CSS Files 
   |    |-- scss/                                  # SCSS Files 
   |         |-- corporate-ui-dashboard/_variables.scss # File Used for Theme Styling
   |
   |-- requirements.txt   # Project Dependencies
   |
   |-- env.sample         # ENV Configuration (default values)
   |-- manage.py          # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

## Recompile SCSS  

The SCSS/CSS files used to style the Ui are saved in the `static` directory. 
In order to update the Ui colors (primary, secondary) this procedure needs to be followed. 

```bash
$ yarn                                                  # install modules
$ vi static/scss/corporate-ui-dashboard/_variables.scss # edit variables 
$ gulp                                                  # SCSS to CSS translation
```

The `_variables.scss` content defines the `primary` and `secondary` colors: 

```scss
$primary:       #774dd3 !default; // EDIT for customization
$secondary:     #64748b !default; // EDIT for customization
$info:          #55a6f8 !default; // EDIT for customization
$success:       #67c23a !default; // EDIT for customization
$warning:       #f19937 !default; // EDIT for customization 
$danger:        #ea4e3d !default; // EDIT for customization
```

<br />

## Deploy on [Render](https://render.com/)

- Create a Blueprint instance
  - Go to https://dashboard.render.com/blueprints this link.
- Click `New Blueprint Instance` button.
- Connect your `repo` which you want to deploy.
- Fill the `Service Group Name` and click on `Update Existing Resources` button.
- After that your deployment will start automatically.

At this point, the product should be LIVE.

<br />

---
[C.O.S.T.M - Formation Management System](https://github.com/Manitriniaina2002/Projet-Django/) - **Django** application for training management
