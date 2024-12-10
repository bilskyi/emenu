from django.shortcuts import render
from rest_framework.views import View
from django.http.response import HttpResponse


class TestAPIView(View):
    def get(self, request):
        return HttpResponse("Hello!")