from django import forms

class UploadForm(forms.Form):
    pdf_file = forms.FileField(required=False)
    linkedin_link = forms.CharField(max_length=200, required=False)
