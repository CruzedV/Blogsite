from django import forms
from django.core.exceptions import ValidationError

from blog_homepage.models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'slug', 'text', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug']

        if new_slug == 'create':
            raise ValidationError('Slug may not be "create"')
            
        if News.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(
                    'Slug must be unique.'
                    'We have "{}" slug already'.format(new_slug)
                    )
        return new_slug