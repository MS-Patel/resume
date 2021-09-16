
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from app.forms import ResumeForm
from django.shortcuts import redirect, render
from .models import Resume


# Create your views here.


def home(request):
    return render(request, "home.html")


@login_required
def create_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            data = Resume()
            data.username = request.user
            data.full_name = form.cleaned_data['full_name']
            data.address = form.cleaned_data['address']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.about_you = form.cleaned_data['about_you']
            data.education = form.cleaned_data['education']
            data.career = form.cleaned_data['career']
            data.job_1_start = form.cleaned_data['job_1_start']
            data.job_1_end = form.cleaned_data['job_1_end']
            data.job_1_details = form.cleaned_data['job_1_details']
            data.job_2_start = form.cleaned_data['job_2_start']
            data.job_2_end = form.cleaned_data['job_2_end']
            data.job_2_details = form.cleaned_data['job_2_details']
            data.job_3_start = form.cleaned_data['job_3_start']
            data.job_3_end = form.cleaned_data['job_3_end']
            data.job_3_details = form.cleaned_data['job_3_details']
            data.references = form.cleaned_data['references']
            data.image = form.cleaned_data['image']
            data.save()
            return HttpResponse("Resume create:")
    else:
        form = ResumeForm()
    return render(request, "create-resume.html", {'form': form})


def resume(request):
    return render(request, "resume.html")
    try:
        resume_info = client.query(q.get(
            q.match(q.index("resume_index"), request.session["user"]["username"])))["data"]
        context = {"resume_info": resume_info}
        return render(request, "resume.html", context)
    except:
        return render(request, "resume.html")
