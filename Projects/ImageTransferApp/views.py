from email.mime import image
from django.shortcuts import render
from .models import Image

def image_upload(request):
    if request.method == 'POST':
        image = Image(image=request.FILES['image'])
        image.save()

    return render(request, 'upload.html')

def image_view(request):
    images = Image.objects.all()
    recent = images[len(images)-1]
    return render(request, 'view.html', {'images': [recent]})

def all_images(request):
    images = Image.objects.all()
    return render(request, 'all_images.html', {'images': images})

