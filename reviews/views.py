from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm


# Create your views here.

def index(request):
    # check request method if it's a 'GET' or 'POST'
    # if request.method == 'POST':
    #     entered_username = request.POST['username']
    #     """Validate the user input"""
    #     if entered_username == "":
    #         context = {
    #             "has_error": True
    #         }
    #         return render(request, "index.html", context=context)
    #     print(entered_username)
    #     return HttpResponseRedirect("/thank-you")

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect("/thank-you")
    form = ReviewForm()

    context = {
        "form": form
    }

    return render(request, "index.html", context=context)


def thank_you(request):
    return render(request, "thank_you.html")
