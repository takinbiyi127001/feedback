from django import forms

"""Define Django form class"""


class ReviewForm(forms.Form):
    user_name = forms.CharField()
