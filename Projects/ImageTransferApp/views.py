from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm

from django.http import JsonResponse

from django.core import serializers


def image_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = form.save(commit=False)  # Don't save the model yet
            new_image.name = request.FILES['image'].name  # Get the name of the file
            new_image.save()  # Now save the model
            return redirect('all_images')  # Or 'all' if you want to redirect to the all images page
    else:
        form = ImageForm()

    return render(request, 'upload.html', {'form': form})


def image_view(request):
    images = Image.objects.all()
    if len(images) == 0:
        return render(request, 'upload.html', {'form': ImageForm()})
    recent = images[len(images)-1]
    return render(request, 'view.html', {'images': [recent]})

def all_images(request):
    images = Image.objects.all()
    return render(request, 'all_images.html', {'images': images})

def get_all_images_json(request):
    images = Image.objects.all()
    image_list = [{"name": image.name, "url": request.build_absolute_uri(image.image.url)} for image in images]
    return JsonResponse(image_list, safe=False)