import random
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from account.models import Profile
from .models import Image

def get_profile(user):
    user = User.objects.get(id=user.id)
    return Profile.objects.get(user=user)

def get_profile_imgs_src(user):
    profile = get_profile(user)
    static_path = 'images/'
    return [static_path+img.img_name for img in profile.album.all()]

def get_img_from_db(img_name):
    return get_object_or_404(Image ,img_name=img_name)

def generate_img_src(user, resolution, amount):
    profile = get_profile(user=user)
    # users album
    album = profile.album.all()
    album_needed_res_imgs = list(album.filter(img_size=resolution))
    album_img_names = [img.img_name for img in album_needed_res_imgs]
    # all res imgs
    all_needed_res_imgs = list(Image.objects.all().filter(img_size=resolution))
    # src
    img_names = []
    imgs_src = []
    if len(all_needed_res_imgs) - len(album_needed_res_imgs) >= int(amount):
        attempts = 100
        for _ in range(int(amount)):
            img_name = random.choice(all_needed_res_imgs).img_name
            while ((img_name in img_names) or (img_name in album_img_names)) and attempts:
                img_name = random.choice(all_needed_res_imgs).img_name
                attempts -= 1
            img_names.append(img_name)
    elif len(all_needed_res_imgs) - len(album_needed_res_imgs) > 0:
        for img in all_needed_res_imgs:
            img_name = img.img_name
            if img_name not in album_img_names:
                img_names.append(img_name)
    if img_names:
        static_path = 'images/'
        imgs_src = [static_path+img_name for img_name in img_names]
    return imgs_src