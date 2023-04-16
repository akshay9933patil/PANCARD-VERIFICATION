from django.shortcuts import render
from .forms import VerificationForm
from django.http import HttpResponse

def verification_view(request):
    form = VerificationForm()
    if request.method == 'POST':
        form = VerificationForm(request.POST)
        if form.is_valid():
            pan_no = form.cleaned_data.get("pan")
            return HttpResponse("<h1>This Valid Adhar number</h1>")
    return render(request, template_name="Verification/verification_form.html", context={"form":form})
