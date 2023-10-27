import os 
import random 
from blog.models import Image


def gatcha():
    all_images = Image.objects.all()
    if all_images:
        return random.choice(all_images)
    return None