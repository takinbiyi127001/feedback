from django.urls import path


from . import views

urlpatterns = [
    # path("", views.index, name='index'),
    path("", views.ReviewView.as_view()),
    path("thank-you", views.thank_you, name='thank_you'),
]