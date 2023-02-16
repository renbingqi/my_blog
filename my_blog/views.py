from django.shortcuts import render
from django.views import View


class Index(View):
    def get(self,req):
        return render(req,'index.html')