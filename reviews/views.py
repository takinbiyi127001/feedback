from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm
from .models import Review
# from .models import Review


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
        # existing_data = Review.objects.get(pk=1)  # Only required for an existing data field but not for a new one
        # form = ReviewForm(request.POST, instance=existing_data)
        form = ReviewForm(request.POST)
        if form.is_valid():
            """Using modelform we can skip the next four steps"""
            # review = Review(user_name=form.cleaned_data['user_name'],
            #                 review_text=form.cleaned_data['review_text'],
            #                 rating=form.cleaned_data['rating'])
            # review.save()  # Save data to the database
            # print(form.cleaned_data)
            form.save()  # Convenient for using the modelform
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()

    context = {
        "form": form
    }

    return render(request, "index.html", context=context)


def thank_you(request):
    return render(request, "thank_you.html")
