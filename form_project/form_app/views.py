

from django.shortcuts import render
from django.http import JsonResponse
from .forms import UploadForm

def upload_form(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = form.cleaned_data.get('pdf_file')
            linkedin_link = form.cleaned_data.get('linkedin_link')
            # Process the form data (PDF parsing or web scraping) here
            # Fill the form using the extracted information
            # Save the form data to the database
            return JsonResponse({'message': 'Form submitted successfully!'})
    else:
        form = UploadForm()
    return render(request, 'form_app/form.html', {'form': form})

