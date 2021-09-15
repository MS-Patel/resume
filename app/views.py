
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseNotFound
import pytz
from .models import Resume
import hashlib
import datetime


# Create your views here.


def home(request):
    return render(request, "home.html")


def create_resume(request):
    if request.method == "POST":
        username = Resume.objects.create()
        full_name = request.POST.get("name")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        about_you = request.POST.get("about")
        education = request.POST.get("education")
        career = request.POST.get("career")
        job_1__start = request.POST.get("job-1_start")
        job_1__end = request.POST.get("job-1_end")
        job_1__details = request.POST.get("job-1_details")
        job_2__start = request.POST.get("job-2_start")
        job_2__end = request.POST.get("job-2_end")
        job_2__details = request.POST.get("job-2_details")
        job_3__start = request.POST.get("job-3_start")
        job_3__end = request.POST.get("job-3_end")
        job_3__details = request.POST.get("job-3_details")
        references = request.POST.get("references")
    #     try:
    #         resume = client.query(
    #             q.get(q.match(q.index("resume_index"), username)))
    #         quiz = client.query(q.update(q.ref(q.collection("Resume_Info"), resume["ref"].id()), {
    #             "data": {
    #                 "user": username,
    #                 "full_name": full_name,
    #                 "address": address,
    #                 "phone": phone,
    #                 "email": email,
    #                 "about_you": about_you,
    #                 "education": education,
    #                 "career": career,
    #                 "job_1__start": job_1__start,
    #                 "job_1__end": job_1__end,
    #                 "job_1__details": job_1__details,
    #                 "job_2__start": job_2__start,
    #                 "job_2__end": job_2__end,
    #                 "job_2__details": job_2__details,
    #                 "job_3__start": job_3__start,
    #                 "job_3__end": job_3__end,
    #                 "job_3__details": job_3__details,
    #             }
    #         }))
    #         messages.add_message(
    #             request, messages.INFO, 'Resume Info Edited Successfully. Download Resume Now')
    #         return redirect("App:create-resume")
    #     except:
    #         quiz = client.query(q.create(q.collection("Resume_Info"), {
    #             "data": {
    #                 "user": username,
    #                 "full_name": full_name,
    #                 "address": address,
    #                 "phone": phone,
    #                 "email": email,
    #                 "about_you": about_you,
    #                 "education": education,
    #                 "job_1__start": job_1__start,
    #                 "job_1__end": job_1__end,
    #                 "job_1__details": job_1__details,
    #                 "job_2__start": job_2__start,
    #                 "job_2__end": job_2__end,
    #                 "job_2__details": job_2__details,
    #                 "job_3__start": job_3__start,
    #                 "job_3__end": job_3__end,
    #                 "job_3__details": job_3__details,
    #             }
    #         }))
    #         messages.add_message(
    #             request, messages.INFO, 'Resume Info Saved Successfully. Download Resume Now')
    #         return redirect("App:resume")
    # else:
    #     try:
    #         resume_info = client.query(q.get(
    #             q.match(q.index("resume_index"), request.session["user"]["username"])))["data"]
    #         context = {"resume_info": resume_info}
    #         return render(request, "create-resume.html", context)
    #     except:
    #
    return render(request, "create-resume.html")


def resume(request):
    return render(request, "resume.html")
    try:
        resume_info = client.query(q.get(
            q.match(q.index("resume_index"), request.session["user"]["username"])))["data"]
        context = {"resume_info": resume_info}
        return render(request, "resume.html", context)
    except:
        return render(request, "resume.html")
