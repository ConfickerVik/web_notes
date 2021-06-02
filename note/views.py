from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.


class NotesView:
    def start_page(request):
        return render(request, template_name="note/main_page.html")
