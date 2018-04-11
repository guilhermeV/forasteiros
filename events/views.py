try:
    from urllib import quote_plus #python 2
except:
    pass

from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import EventForm
from .models import Event

def event_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
		
	form = EventForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		# message success
		messages.success(request, "Successfully Created")
		return render(request, "event_form.html", {"form": form})
	context = {
		"form": form,
	}
	return render(request, "event_form.html", context)

