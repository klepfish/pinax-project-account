# import the django settings
from django.conf import settings
# for generating json
from django.utils import simplejson
# for loading template
from django.template import RequestContext, Context, loader
# for csrf
from django.core.context_processors import csrf
# for HTTP response
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
# for os manipulations
import os
from uuid import uuid4
from zencoder import Zencoder
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, get_object_or_404, redirect
from videos.models import Video, PurchaseCode, Access, Sale, Job, Series
from django.http import HttpRequest
from videos.forms import ContactForm, SignupForm
from django.template.defaultfilters import slugify
from swiftype import swiftype
from tasks import *
import smtplib
from email.mime.text import MIMEText
import urllib
import urllib2
import pycurl
import base64
import datetime
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from paypal.standard.ipn.signals import payment_was_successful

def list_videos(request):
video_list = Video.objects.exclude(slug=None).filter(status='A').order_by('created').reverse()

paginator = Paginator(video_list, 10)

page = request.GET.get('page')

if page is not None:
try:
videos = paginator.page(page)
except PageNotAnInteger:
# If page is not an integer, deliver first page.
videos = paginator.page(1)
except EmptyPage:
# If page is out of range (e.g. 9999), deliver last page of results.
videos = paginator.page(paginator.num_pages)
else:
videos = paginator.page(1)

t = loader.get_template("list_videos.html")
c = RequestContext(request, {
"videos": videos,
})

return HttpResponse(t.render(c))
