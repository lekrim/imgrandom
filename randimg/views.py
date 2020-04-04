from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User

from .forms import ImgSetForm
from . import services

# Create your views here.
@login_required
def create_imgset(request):
    not_fixed_footer = False
    if request.method == 'POST':
        form = ImgSetForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            resolution = cd['img_resolution'].replace('×', '/')
            amount = cd['amount']
            user = request.user
            imgs_src = services.generate_img_src(user, resolution, amount)

            if not imgs_src:
                no_src = True
            else:
                no_src = False

            if int(amount) > 3 and len(imgs_src) > 3:
                not_fixed_footer = True
    else:
        form = ImgSetForm()
        imgs_src = []
        no_src = False
    return render(request ,'imgrandom/imgset.html', {'form':form, 'imgs_src':imgs_src, 
                                                     'not_fixed_footer':not_fixed_footer,
                                                     'no_src':no_src})

@login_required
def show_album(request):
    not_fixed_footer = False
    imgs_src = services.get_profile_imgs_src(request.user)
    if len(imgs_src) > 3:
        not_fixed_footer = True
    return render(request ,'imgrandom/album.html', {'imgs_src':imgs_src, 
                                                    'not_fixed_footer':not_fixed_footer})

def save_img(request, img_name):
    img = services.get_img_from_db(img_name)
    profile = services.get_profile(request.user)
    profile.album.add(img)
    return HttpResponse('saved')

def delete_img(request, img_name):
    img = services.get_img_from_db(img_name)
    profile = services.get_profile(request.user)
    profile.album.remove(img)
    return HttpResponse('deleted')
