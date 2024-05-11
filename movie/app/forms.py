from django import forms
from app.models import movie


class movieform(forms.ModelForm):
    class Meta:
        model=movie
        fields='__all__'

        # or
        #     fields=['title','author']
        # or
        #     exclude=['price']

# first create forms.py in app then write the code to create form
#                         class Bookform(forms.ModelForm):
#                             class Meta:
#                                 model=Book
#                                 fields='__all__'
# then goes to views.py then write the code there
#         from Book.forms import Bookform # importing the Bookform
#         def addbook(request):
#             form=Bookform()
#             return render (request,'add1.html',{'form':form})
# after that display in the html file
#                 {{ form }}