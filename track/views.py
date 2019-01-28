from django.shortcuts import render, HttpResponseRedirect
from .models import Package
from django.core.urlresolvers import reverse
# Create your views here.

def home(request):
    template_name = "home.html"
    return render(request, template_name, {'active': 'home'})

def services(request):
    template_name = "services.html"
    return render(request, template_name, {'active': 'services'})

def ground_transport(request):
    template_name = "services/ground_transport.html"
    return render(request, template_name)

def cargo(request):
    template_name = "services/cargo.html"
    return render(request, template_name)

def ware_housing(request):
    template_name = "services/warehousing.html"
    return render(request, template_name)

def logistic_service(request):
    template_name = "services/logistic_service.html"
    return render(request, template_name)

def truck_service(request):
    template_name = "services/trucking_service.html"
    return render(request, template_name)

def storage(request):
    template_name = "services/storage.html"
    return render(request, template_name)

def about(request):
    template_name = "about.html"
    return render(request, template_name, {'active': 'about'})

def tracking(request):
    template_name = "tracking.html"
    if request.method == "GET":
        return render(request, template_name, {'invalid_tracking_code': False, 'active': 'track'})
    if request.method == "POST":
        tracking_code = request.POST["tracking_code"]
        package = Package.objects.filter(package_id=tracking_code)
        if package.exists():
            return HttpResponseRedirect(reverse('tracking_information', args=(tracking_code,)))
        else:
            return HttpResponseRedirect(reverse('tracking_not_found'))

def tracking_not_found(request):
    template_name = "tracking.html"
    if request.method == "GET":
        return render(request, template_name, {'invalid_tracking_code': True, 'active': 'track'})
    if request.method == "POST":
        tracking_code = request.POST["tracking_code"]
        print(tracking_code)
        package = Package.objects.filter(package_id=tracking_code)
        if package.exists():
            return HttpResponseRedirect(reverse('tracking_information', args=(tracking_code,)))
        else:
            return HttpResponseRedirect(reverse('tracking_not_found'))

def tracking_information(request, tracking_code):
    template_name = "tracking_information.html"
    package = Package.objects.filter(package_id=tracking_code)
    return render(request, template_name, {'package': package[0], 'active': 'track', 'package': package[0]})


def newsfeed(request):
    template_name = "newsfeed.html"
    return render(request, template_name, {'active': 'newsfeed'})

def contact(request):
    template_name = "contact.html"
    return render(request, template_name, {'active': 'contact'})

def article(request):
    template_name = "article.html"
    return render(request, template_name, {'active': 'article'})