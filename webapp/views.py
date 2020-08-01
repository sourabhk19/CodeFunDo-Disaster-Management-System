from django.shortcuts import render
from  django.http import HttpResponseRedirect
# Create your views here.
def home_view(request,*args,**kwargs):
    return render(request,"index.html")



def statistics_view(request):

    # ... your python code/script
    return render(request,"worldmap.html")
    #return HttpResponseRedirect('## your redirect template url ##') 

def disaster_data_view(request):

    # ... your python code/script
    return render(request,"disaster_data.html")
    #return HttpResponseRedirect('## your redirect template url ##') 
