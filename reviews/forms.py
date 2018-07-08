from django.forms import ModelForm, ModelChoiceField
from django import forms
from reviews.models import Rating


class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ('review', 'chapter')
        blank = True





