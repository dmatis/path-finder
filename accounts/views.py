from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from accounts.forms import EditProfileForm
from accounts.forms import UserRegistrationForm
from registration.signals import user_registered
from accounts.models import user_registered_callback


# def user_registered_callback(sender, user, request, **kwargs):
#     form = UserRegistrationForm(request.POST)
#     user.first_name = form.data['first_name']
#     user.last_name = form.data['last_name']
#     user.save()


def show_profile(request):

    user_registered.connect(user_registered_callback)

    user = request.user
    form = EditProfileForm(initial={'first_name': user.first_name,
                                    'last_name': user.last_name,
                                    'email': user.email})
    context = {
        "form": form
    }
    return render(request, 'accounts/profile.html', context)

def edit_profile(request):

    user = request.user
    form = EditProfileForm(request.POST or None, initial={'first_name': user.first_name,
                                                          'last_name': user.last_name,
                                                          'email': user.email})
    if request.method == 'POST':
        if form.is_valid():
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
            return HttpResponseRedirect('%s'%(reverse('profile')))

    context = {
        "form": form
    }

    return render(request, "accounts/edit_profile.html", context)


