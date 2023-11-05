from django.shortcuts import render
from django.http import HttpResponse


## Index view
def index(request: HttpResponse) -> HttpResponse:
    
    return render(request, 'competition_tracker/index.html')