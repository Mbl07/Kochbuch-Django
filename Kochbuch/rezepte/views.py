from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from . import models


# Create your views here.
class ImageForm(forms.ModelForm):
    class Meta:
        model = models.Image
        exclude = []


def overview(request):
    all_images = models.Image.objects.all()
    return render(request, 'index.html', dict(images=all_images))


def rezept_upload(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():  # Formular überprüfen
            form.save()
            return HttpResponseRedirect('/')  # Umleitung

    else:
        form = ImageForm()
    return render(request, 'rezept_upload.html', dict(form=form))
