from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
	body = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), required=False)

	class Meta:
		model = Review
		fields = ('body',)
                   
 