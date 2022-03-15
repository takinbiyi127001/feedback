from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from  .forms import ProfileForm


# Create your views here.

def store_file(file):
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        context = {
            "form": form
        }
        return render(request, "profiles/create_profile.html", context=context)

    # Search django upload files for reference
    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            store_file(request.FILES['image'])
            return HttpResponseRedirect("/profiles")

        context = {
            "form": submitted_form
        }
        return render(request, "profiles/create_profile.html", context=context)

