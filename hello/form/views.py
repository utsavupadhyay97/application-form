from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.
def contact(request):

    if request.method == "POST":
        form = ContactForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
        else:
            form = ContactForm()    
    form = ContactForm()
    return render(request, 'form.html', {'form':form})
