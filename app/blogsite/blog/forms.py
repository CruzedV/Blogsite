from django import forms
from django.core.exceptions import ValidationError

from blog.models import Tag
from blog.models import Post
from blog.models import User
#from blog.models import News


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }
    def clean_slug(self):
        new_slug = self.cleaned_data['slug']

        if new_slug == 'create':
            raise ValidationError('Slug may not be "create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(
                    'Slug must be unique.'
                    'We have "{}" slug already'.format(new_slug)
                    )

        return new_slug

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'title', 'slug', 'body', 'tags']
        widgets = {
            'image': forms.ClearableFileInput(),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'] 
#or self.cleaned_data.get('slug')
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create"')
        return new_slug

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nickname', 'slug']
        widgets = {
            'nickname': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug']

        if new_slug == 'create':
            raise ValidationError('Slug may not be "create"')
            
        if User.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(
                    'Slug must be unique.'
                    'We have "{}" slug already'.format(new_slug)
                    )
        return new_slug

#Если класс Form
#def save(self):    
#    new_tag = Tag.objects.create(
#        title=self.cleaned_data['title'],
#        slug=self.cleaned_data['slug']
#    )
#    return new_tag

