from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name='index'),
    # path("thank-you", views.thank_you, name='thank_you'),
    path("", views.ReviewView.as_view()),
    path("thank-you", views.ThankYouView.as_view()),
    path("reviews", views.ReviewsListView.as_view()),
    path("reviews/<int:id>", views.SingleReviewView.as_view())
]
