from django import forms

"""Define Django form class"""


class ReviewForm(forms.Form):
    user_name = forms.CharField(label="You name", max_length=50, error_messages={
        "required": "Your name must not be empty!",
        "max_length": "Please enter a shorter name!"
    })
