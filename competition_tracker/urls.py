from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('competitions/', views.CompetitionListView.as_view(), name='competitions'),
    path('competition/<int:pk>', views.CompetitionDetailView.as_view(), name='competition-detail'),
    path('competition/create/', views.CompetitionCreateView.as_view(), name='competition-create'),
    path('competition/<int:pk>/delete/', views.CompetitionDeleteView.as_view(), name='competition-delete'),
    path('club-members/', views.ClubMemberListView.as_view(), name='club-members'),
    path('club-member/<int:pk>', views.ClubMemberDetailView.as_view(), name='club-member-detail'),
    path('club-member/create/', views.ClubMemberCreateView.as_view(), name='club-member-create'),
    path('club-member/<int:pk>/delete/', views.ClubMemberDeleteView.as_view(), name='club-member-delete'),
]