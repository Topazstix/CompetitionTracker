# General Dev Notes

## Requirements For Sprint 1

>NOTE: Project will NOT implement login feature

- [ ] Display list of all items on page if any exist
- [ ] Display detailed information about each item individually
- [ ] Items should have at least 3 attributes with at least two required
- [ ] Should allow items to be:
  - [ ] Created
  - [ ] Updated
  - [ ] Deleted

## Environment Configuration

~~> Note: Docker is still a *WORK IN PROGRESS*. All environment commands shown to run in docker apply to local environment post-installation of miniconda3.~~

> **^ This shouldnt be required considering there is no necessary requirement for miniconda? Just use the default python3.11 install?**

- Utilizing docker (continuumio/miniconda3)
    1. `docker pull continuumio/miniconda3`
    2. *Commands run in docker:*
    3. Note: the following should be run as standard user
        - `conda create --name application`
        - `conda activate application`
        - `conda install python=3.11`
        - `pip install django`
        - `django-admin startproject main`
        - `cd main`
        - `django-admin startapp competition_tracker`
        - *at this step we start editing the settings.py file*
- For local vscode development, adjusting the default file extension for django-templates to be specific for django and exclude traditional HTML for linting/syntax assistance
  - Add the [json code](#vscode-settings-conf) to the project's `settings.json` file:
  <!-- - *Just remember to be cognizant of the file extension differentiation for local project settings* -->

## Django Configuration

After following the steps above, proceed with the following:

1. Add `competition_tracker` & `bootstrap5` to `INSTALLED_APPS` in `settings.py`
2. Amend root `urls.py` with a path to `competition_tracker.urls`
3. Update the `competition_tracker/views.py` file to define the index view
4. Create `competition_tracker/urls.py` file and define the index path
5. Update `competition_tracker/views.py` file to define the index view
6. Create folder recursively in `competition_tracker folder` named `templates/competition_tracker`
7. Add file `base_template.html` to `templates/competition_tracker` folder
8. Edit the `base_template.html` file to incoroporate requirements from above.
   1. Using a template designed sometime before.
9. Create `index.html` file in `templates/competition_tracker` folder
10. Create a `competition_tracker/static` folder with corresponding folders for images, css, html, etc
11. Add the [python code](#django-static-conf) to the `settings.py` file for the project
12. Create a `models.py` file in the apps root directory and then see subection [models](#models) for designing our database models for python
13. Run the following commands:
    1. `python manage.py makemigrations`
    2. `python manage.py migrate`
14. Run `python manage.py createsuperuser` and follow the instructions when prompted to create an admin account for managing the backend database
15. Add the code in the [admin site](#admin-site) section to the `admin.py` file in the app's root directory


## Views, Templates, Forms

With everything configured in our environment and project, we now need to create views for our data and templates for our views.

1. Amend the `models.py` file to allow each model to redirect to specific template pages we'll create in the next few steps. Code seen in the [get_absolute_url](#get-absolute-url) section
2. Add `club_member = models.ManyToManyField('ClubMember', help_text='Select a club member for this competition')` as an attribute to the `Competition` model in `models.py`
3. Repeat step 13 from the [Django Configuration](#django-configuration) section to migrate the new changes
4. Create a `forms.py` file and add the code shown in the [forms](#forms) section
5. Add the the [paths shown in urls section](#urls) to the `urls.py` file in the app's root directory
6. Add the [code shown in the views section](#views) to the `views.py` file in the app's root directory
7. Finally, create several template html files to view, create, and list the various models. You can reference the [templates](../competition_tracker/templates/competition_tracker/) folder for examples.

---

### Code Snippets

#### Django Static Conf

```python
## Add the following to the settings.py file
## Under BASE_DIR var
APP_DIR = BASE_DIR / 'competition_tracker'

## Rest of code...

## Under STATIC_URL var
STATICFILES_DIRS = [
    APP_DIR / "static",
]
MEDIA_URL = '/images/'
```

#### Vscode Settings Conf

```json
// Create a settings.json file in the .vscode folder and add the following:
{
  "emmet.includeLanguages": { "django-html": "html" },
  "files.associations": {
    "**/*.html": "html",
    "**/templates/**/*.html": "django-html",
    "**/templates/**/*.djt.txt": "django-txt"
  },
  "[django-html]": {
    "editor.defaultFormatter": "batisteo.vscode-django",
    "editor.insertSpaces": false,
    "editor.tabSize": 2
  }
}
```

#### Models

```python
## Add the following to the models.py file
from typing import Any
from django.db import models
from django.urls import reverse

# Create your models here.
class Competition(models.Model):
    """Model representing a competition."""
    name = models.CharField(max_length=200, help_text='Enter a competition name')
    description = models.TextField(max_length=1000, help_text='Enter a description of the competition')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    

class ClubMember(models.Model):
    
    SKILL_LEVEL_CHOICES = (
        ("Beginner", "New to cybersecurity and/or competitions"),
        ("Intermediate", "Some experience with cybersecurity and/or competitions"),
        ("Advanced", "Experienced with cybersecurity and/or competitions"),
    )
    
    name = models.CharField(max_length=200, help_text='Enter a club member name')
    username = models.CharField(max_length=100, help_text='Enter a username')
    email = models.EmailField(max_length=100, help_text='Enter an email address')
    
    ## Create competitions model link: one club member can participate in many competitions
```

#### Admin Site

```python
## Add the following to the admin.py file
from django.contrib import admin
from .models import Competition, ClubMember

# Register your models here.
admin.site.register(Competition)
admin.site.register(ClubMember)
```

#### Get Absolute URL

```python
## ADD TO COMPETITIONS MODEL:
    def __str__(self: Any) -> str:
        """String for representing the Model object."""
        return self.name
    
    def get_absolute_url(self: Any) -> str:
        """Returns the url to access a particular competition instance."""
        return reverse('competition-detail', args=[str(self.id)])

## ADD TO CLUBMEMBER MODEL:
    def __str__(self: Any) -> str:
        """String for representing the Model object."""
        return self.name
    
    def get_absolute_url(self: Any) -> str:
        """Returns the url to access a particular club member instance."""
        return reverse('club-member-detail', args=[str(self.id)])
```

#### Forms

```python
from django import forms
from .models import Competition, ClubMember

class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ['name', 'description', 'start_date', 'end_date', 'club_member']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }
        help_texts = {
            'name': 'Enter the name of the competition.',
            'description': 'Enter a detailed description of the competition.',
        }

class ClubMemberForm(forms.ModelForm):
    class Meta:
        model = ClubMember
        fields = ['name', 'username', 'email']
        help_texts = {
            'name': 'Enter the full name of the club member.',
            'username': 'Enter the preferred username for the club member.',
            'email': 'Enter the email address of the club member.',
        }
```

#### URLs

```python
path('competitions/', views.CompetitionListView.as_view(), name='competitions'),
path('competition/<int:pk>', views.CompetitionDetailView.as_view(), name='competition-detail'),
path('competition/create/', views.CompetitionCreateView.as_view(), name='competition-create'),
path('competition/<int:pk>/delete/', views.CompetitionDeleteView.as_view(), name='competition-delete'),
path('club-members/', views.ClubMemberListView.as_view(), name='club-members'),
path('club-member/<int:pk>', views.ClubMemberDetailView.as_view(), name='club-member-detail'),
path('club-member/create/', views.ClubMemberCreateView.as_view(), name='club-member-create'),
path('club-member/<int:pk>/delete/', views.ClubMemberDeleteView.as_view(), name='club-member-delete'),
```

#### Views

```python
from .models import Competition, ClubMember
from django.views import generic
from .forms import CompetitionForm, ClubMemberForm  

# List view for Competitions
class CompetitionListView(generic.ListView):
    model = Competition
    # template_name = "competition_list.html"
    # paginate_by = 10  # Display 10 competitions per page
    
    # def get_queryset(self):
    #     # Return the queryset of competitions ordered by 'start_date'
    #     return Competition.objects.all().order_by('start_date')

# Detail view for a Competition
class CompetitionDetailView(generic.DetailView):
    model = Competition

# Create view for a Competition
class CompetitionCreateView(generic.CreateView):
    model = Competition
    form_class = CompetitionForm
    # template_name = 'competition_form.html'  # Replace with your actual template

# Delete view for a Competition
class CompetitionDeleteView(generic.DeleteView):
    model = Competition
    success_url = '/competitions/'  # Redirect to the competition list after delete

# List view for ClubMembers
class ClubMemberListView(generic.ListView):
    model = ClubMember
    paginate_by = 10

# Detail view for a ClubMember
class ClubMemberDetailView(generic.DetailView):
    model = ClubMember

# Create view for a ClubMember
class ClubMemberCreateView(generic.CreateView):
    model = ClubMember
    form_class = ClubMemberForm
    # template_name = 'clubmember_form.html'  # Replace with your actual template

# Delete view for a ClubMember
class ClubMemberDeleteView(generic.DeleteView):
    model = ClubMember
    success_url = '/club-members/'  # Redirect to the club member list after delete
```
