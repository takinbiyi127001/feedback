from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from .forms import ReviewForm
from .models import Review


# Create your views here.

"""When to use Which View
TemplateView -> When you don't need any database data
View -> To use a post and get method
ListView -> When you have a list of items in the database
DetailView -> When you have a single data to fetch from the database
FormView -> Helps build classBased views that deals with forms
CreateView -> A specialise view that Replaces formView. We can also remove the forms.py
UpdateView -> Updating data in the database
DeleteView -> Deleting data from the database"""


# Create a class Based views instead of a function views

class ReviewView(CreateView):
    # We can remove the get and post methods by inheriting from FormView instead of the View
    # form_class = ReviewForm  # Don't instantiate the class, only points to it

    # We can remove the form valid method by inheriting from CreateView instead of the FormView
    model = Review
    form_class = ReviewForm  # Using the form_class, we can remove the form_valid method
    template_name = "reviews/index.html"
    # For post(submission). Django need to know where to redirect to
    success_url = "/thank-you"

    #  For saving valid form to the database
    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

    # def get(self, request):
    #     form = ReviewForm()
    #
    #     context = {
    #         "form": form
    #     }
    #     return render(request, "reviews/index.html", context=context)

    # def post(self, request):
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         form.save()  # Convenient for using the modelform
    #         return HttpResponseRedirect("/thank-you")
    #
    #     context = {
    #         "form": form
    #     }
    #     return render(request, "reviews/index.html", context=context)


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context


class ReviewsListView(ListView):
    # We can remove the get_context_data by inheriting from ListView instead the TemplateView
    template_name = "reviews/review_list.html"
    model = Review  # You don't have to instantiate the class, just point to it
    context_object_name = "reviews"

    # To render reviews greater than 4
    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     reviews = Review.objects.all()
    #     context["reviews"] = reviews
    #     return context


class SingleReviewView(DetailView):
    # We can remove the get_context_data by inheriting from DetailView instead the TemplateView
    # No need of adding the context_object_name as Django automatically converts Review to lower
    # case and exposes the fetched single piece of data through the model name to our template
    template_name = "reviews/single_review.html"
    model = Review

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs["id"]
    #     selected_review = Review.objects.get(pk=review_id)
    #     context["review"] = selected_review
    #     return context

# def index(request):
#     # check request method if it's a 'GET' or 'POST'
#     # if request.method == 'POST':
#     #     entered_username = request.POST['username']
#     #     """Validate the user input"""
#     #     if entered_username == "":
#     #         context = {
#     #             "has_error": True
#     #         }
#     #         return render(request, "index.html", context=context)
#     #     print(entered_username)
#     #     return HttpResponseRedirect("/thank-you")
#
#     if request.method == 'POST':
#         # existing_data = Review.objects.get(pk=1)  # Only required for an existing data field but not for a new one
#         # form = ReviewForm(request.POST, instance=existing_data)
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             """Using modelform we can skip the next four steps"""
#             # review = Review(user_name=form.cleaned_data['user_name'],
#             #                 review_text=form.cleaned_data['review_text'],
#             #                 rating=form.cleaned_data['rating'])
#             # review.save()  # Save data to the database
#             # print(form.cleaned_data)
#             form.save()  # Convenient for using the modelform
#             return HttpResponseRedirect("/thank-you")
#     else:
#         form = ReviewForm()
#
#     context = {
#         "form": form
#     }
#
#     return render(request, "index.html", context=context)
#
#
# def thank_you(request):
#     return render(request, "thank_you.html")
