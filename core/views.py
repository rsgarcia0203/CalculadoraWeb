from django.views.generic import View
from django.shortcuts import render, redirect

class HomeView(View):
    def get(self, request, *args, **kwargs):	# *args, **kwargs
        context = {

        }
        return render(request, 'index.html', context)

    def post(self, request):
        return render(request, 'home.html')