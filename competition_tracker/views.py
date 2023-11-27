from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .models import Competition, ClubMember
from django.views import generic
from .forms import CompetitionForm, ClubMemberForm, UserRegistrationForm

# List view for Competitions
class CompetitionListView(generic.ListView):
    model = Competition


# Detail view for a Competition
class CompetitionDetailView(generic.DetailView):
    model = Competition
    

# Create view for a Competition
class CompetitionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Competition
    form_class = CompetitionForm


# Delete view for a Competition
class CompetitionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Competition
    success_url = '/competitions/'

# List view for ClubMembers
class ClubMemberListView(LoginRequiredMixin, generic.ListView):
    model = ClubMember
    paginate_by = 10

# Detail view for a ClubMember
class ClubMemberDetailView(LoginRequiredMixin, generic.DetailView):
    model = ClubMember

# Create view for a ClubMember
class ClubMemberCreateView(LoginRequiredMixin, generic.CreateView):
    model = ClubMember
    form_class = ClubMemberForm

# Delete view for a ClubMember
class ClubMemberDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = ClubMember
    success_url = '/club-members/'



## Index view
def index(request: HttpResponse) -> HttpResponse:
    
    competitions_active = Competition.objects.filter(end_date__isnull=True).order_by('start_date')
    
    context = {
        'competitions_active': competitions_active,
    }
    
    return render(request, 'competition_tracker/index.html', context=context)

def register(request: HttpResponse) -> HttpResponse:
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'competition_tracker/register.html', {'form': form})

@login_required
def competition_create(request):
    if request.method == 'POST':
        form = CompetitionForm(request.POST)
        if form.is_valid():
            competition = form.save(commit=False)
            competition.organizer = request.user  # Assuming a field for the organizer
            competition.save()
            return redirect('competitions')  # Redirect to the list of competitions
    else:
        form = CompetitionForm()
    return render(request, 'competition_tracker/competition_form.html', {'form': form})
