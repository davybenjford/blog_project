from django import forms
from blog.models import Post,Comment

#Forms determine how models can be interacted with using user input entries and what attributes these
#entry forms can have through setting tiles, texts and widgets


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        #Determines which fields that can be edited
        fields=('author','title','text',)

        #widgets take forms and give them detailed charecteristics
        widgets = {
            #here you are able to assign those charecteristics and assign them classes in order to style them
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
