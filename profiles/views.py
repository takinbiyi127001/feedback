from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView

# from .forms import ProfileForm
from .models import UserProfile


# Create your views here.

def store_file(file):
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"  # Used for redirecting


""" Using the CreateView class to simplify the code below"""
# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         context = {
#             "form": form
#         }
#         return render(request, "profiles/create_profile.html", context=context)
#
#     # Search django upload files for reference
#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)
#
#         if submitted_form.is_valid():
#             # store_file(request.FILES['image'])
#             profile = UserProfile(image=request.FILES["user_image"])
#             profile.save()
#             return HttpResponseRedirect("/profiles")
#
#         context = {
#             "form": submitted_form
#         }
#         return render(request, "profiles/create_profile.html", context=context)
