# from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views import View

from core.utils import view_timer


class HelloWorldView(View):
    @view_timer
    def get(self, request):
        return HttpResponse("Hello, World!", status=201)
