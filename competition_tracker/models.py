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
    club_member = models.ManyToManyField('ClubMember', help_text='Select a club member for this competition')
    
    def __str__(self: Any) -> str:
        """String for representing the Model object."""
        return self.name
    
    def get_absolute_url(self: Any) -> str:
        """Returns the url to access a particular competition instance."""
        return reverse('competition-detail', args=[str(self.id)])

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
    
    def __str__(self: Any) -> str:
        """String for representing the Model object."""
        return self.name
    
    def get_absolute_url(self: Any) -> str:
        """Returns the url to access a particular club member instance."""
        return reverse('club-member-detail', args=[str(self.id)])