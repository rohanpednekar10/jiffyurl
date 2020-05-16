from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from .forms import UrlSubmitForm, AnalyticsForm
from .models import URL
from analytics.models import ClickEvent
from stats.models import Statistics
# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        obj, created = Statistics.object.get_or_create(pk = 1)
        context = {
            'object': obj,
            'created': created,
        }
        return render(request, 'shortener/home.html', context)

class ShortenerView(View):
    def get(self, request, *args, **kwargs):
        form = UrlSubmitForm()
        context = {
            'form': form,
            'submitted': False,
        }
        return render(request, 'shortener/shortener.html', context)

    def post(self, request, *args, **kwargs):
        form = UrlSubmitForm(request.POST)
        context = {
            'form': form,
            'created': False,
            'submitted': False,
        }
        if form.is_valid():
            url = form.cleaned_data['url']
            obj, created = URL.objects.get_or_create(url = url)
            if created:
                Statistics.object.new_link_shortened(obj)
            context = {
                'form': form,
                'object': obj,
                'created': created,
                'submitted': True,
                'valid': True,
            }
        else:
            form = UrlSubmitForm()
            context = {
                'form': form,
                'submitted': True,
                'valid': False,
            }
        return render(request, 'shortener/shortener.html', context)

class AnalyticsView(View):
    def get(self, request, *args, **kwargs):
        form = AnalyticsForm()
        context = {
            'form': form
        }
        return render(request, 'shortener/analytics.html', context)

    def post(self, request, *args, **kwargs):
        form = AnalyticsForm(request.POST)
        found = False,
        context = {
            'form': form,
            'found': found,
            'submitted': False,
        }
        if form.is_valid():
            shortcode = form.get_shortcode()
            obj = None
            try:
                obj = URL.objects.get(shortcode = shortcode)
                found = True
            except ObjectDoesNotExist:
                found = False
            context = {
                'form': form,
                'object': obj,
                'found': found,
                'submitted': True,
            }
        return render(request, 'shortener/analytics.html', context)

class RedirectView(View):
    def get(self, request, slug=None, *args, **kwargs):
        qs = URL.objects.filter(shortcode__iexact=slug)
        if qs.count() != 1 and not qs.exists():
            raise Http404
        obj = qs.first()
        ClickEvent.objects.create_event(obj)
        Statistics.object.new_redirect(obj)
        return HttpResponseRedirect(obj.url)