from dataclasses import field
from django import forms
from .models import CategoryReview

# Review Add Form
class ReviewAdd(forms.ModelForm):
         class Meta:
                   model=CategoryReview
                   fields=('review_text','review_rating')
                   
 