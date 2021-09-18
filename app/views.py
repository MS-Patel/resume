
from django.db.models.manager import EmptyManager
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.functional import empty
from app.forms import ResumeForm
from django.shortcuts import redirect, render
from .models import Resume


# Create your views here.


def home(request):
    return render(request, "home.html")


@login_required
def create_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            data = Resume()
            # u = Resume.objects.filter(username_id=request.user.id)
            # if u:
            #     Resume.objects.filter(username_id=u).delete()
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
            if form.cleaned_data['image'] is not None:
                data.image = form.cleaned_data['image']
            data.save()
            return render(request, "home")
    else:
        form = ResumeForm()
    return render(request, "create-resume.html", {'form': form})


@login_required
def resume(request):

    resume_info = Resume.objects.get(username_id=request.user.id)

    context = {"resume_info": resume_info}
    return render(request, "resume.html", context)
