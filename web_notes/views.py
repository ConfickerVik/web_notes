from django.shortcuts import render


class MainPage:
    def show(request):
        return render(request, template_name="logo_page/logo.html")
