from django.shortcuts import render
from django.views.generic import View,ListView,TemplateView
from .models import Video
from .forms import VideoForm

# Create your views here.

    
class Index(TemplateView):
    template_name = 'app/index.html'
    
class Tratamiento(TemplateView):
        template_name = 'app/tratamientos.html'
     

class SobreMi(TemplateView):
    template_name = 'app/SobreMi.html'
    
    def get_context_data(self,**kwargs):
        context=super(SobreMi, self).get_context_data(**kwargs)
        context_object_name = 'videofile'
        #context['videofile']=Video.objects.all()
        lastvideo= Video.objects.all()[0]
        context['videofile']= lastvideo.videofile
        return context
    
    