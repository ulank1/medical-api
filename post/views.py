from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template.loader import render_to_string

from post.models import Post, Appointment


def home(request):
    doctors = Post.objects.all()
    context = {
        'title': 'cvcvxcvxcv',
        'doctors': doctors
    }
    return HttpResponse(render_to_string('home.html', context))


def appointment(request, doctor):
    try:
        doctor1 = Post.objects.get(id=doctor)
        appointments = Appointment.objects.filter(doctor=doctor1)
        dd=appointments.filter(ison='yes')
        cc=dd.order_by('-data', 'time')
    except:
        return Http404
    context={
        "appointments": cc
    }
    return HttpResponse(render_to_response('appointment.html', context))