from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
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



## Index view
def index(request: HttpResponse) -> HttpResponse:
    
    competitions_active = Competition.objects.filter(end_date__isnull=True).order_by('start_date')
    
    context = {
        'competitions_active': competitions_active,
    }
    
    return render(request, 'competition_tracker/index.html', context=context)