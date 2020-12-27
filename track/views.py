from io import BytesIO
from xhtml2pdf import pisa

from django.shortcuts import render, HttpResponseRedirect, HttpResponse, get_object_or_404
from django.template.loader import get_template
from django.urls import reverse

from .models import Package, PackageInfo
from django.db.models import Q
import smtplib
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
        tracking_code = request.POST["tracking_code"].strip()
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
        package = Package.objects.filter(package_id=tracking_code)
        if package.exists():
            return HttpResponseRedirect(reverse('tracking_information', args=(tracking_code,)))
        else:
            return HttpResponseRedirect(reverse('tracking_not_found'))


def tracking_information(request, tracking_code):
    template_name = "tracking_information.html"
    package = get_object_or_404(Package, pk=tracking_code)
    try:
        package_info = PackageInfo.objects.get(package=package)
        package_on_hold = PackageInfo.objects.get(Q(package=package) & Q(on_hold=True))
    except PackageInfo.DoesNotExist:
        package_info = None
        package_on_hold = None

    return render(request, template_name,
                  {'package': package, 'active': 'track',
                   'package_info': package_info, 'package_on_hold': package_on_hold})


def newsfeed(request):
    template_name = "newsfeed.html"
    return render(request, template_name, {'active': 'newsfeed'})


def contact(request):
    template_name = "contact.html"
    return render(request, template_name, {'active': 'contact'})


def article(request):
    template_name = "article.html"
    return render(request, template_name, {'active': 'article'})


def search_package(request):
    # return HttpResponseRedirect(reverse('site_suspended'))
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('login'))
    if request.method == "GET":
        template_name = "search-package.html"
        return render(request, template_name)
    if request.method == "POST":
        package_id = request.POST["tracking_code"]
        print(request.POST)
        qs = Package.objects.filter(package_id=package_id)
        if qs.exists():
            return HttpResponse(package_id)
            # return HttpResponseRedirect(reverse('update_package_destination', args=(package_id,)))
        else:
            return HttpResponse("", status=404)


def update_package_destination(request, tracking_code):
    # return HttpResponseRedirect(reverse('site_suspended'))
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('login'))
    qs1 = Package.objects.filter(package_id=tracking_code)
    if request.method == "GET":
        template_name = "update-package-destination.html"
        qs2 = PackageInfo.objects.filter(package=qs1[0])

        return render(request, template_name, {'package': qs1[0], 'package_info': qs2})
    if request.method == "POST":
        date = request.POST["date"]
        time = request.POST["time"]
        activity = request.POST["activity"]
        location = request.POST["location"]
        details = request.POST["details"]
        on_hold = request.POST.get("onhold", None)

        if not on_hold:
            on_hold = False
        else:
            on_hold = True
        PackageInfo(
            package = qs1[0],
            date = date,
            time = time,
            activity = activity,
            location = location,
            details = details,
            on_hold = on_hold
        ).save()
        return HttpResponseRedirect(reverse('update_package_destination', args=(tracking_code,)))


def send_message(request):
    destination_email = "delivery@speedyglobecourier.com"
    gmail_user = "ask.speedyglobecourier@gmail.com"
    gmail_password = "mesogek1995"

    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    service = request.POST['service']
    message = request.POST['message']

    email_text = """
        Name: %s
        Email: %s
        Subject: %s

        Service: %s

        Message: %s
    """ % (name, email, subject, service, message)
    if name and email and subject and service and message:
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(gmail_user, destination_email, email_text)
            server.close()
            return HttpResponse("")
        except:
            return HttpResponse("", status=404)
    else:
        return HttpResponse("", status=404)


def site_suspended(request):
    template_name = "site-suspended.html"
    return render(request, template_name)


def receipt(request, package_id):
    template_name = "receipt.html"
    package = Package.objects.get(package_id=package_id)
    return render(request, template_name, {"package": package})


def render_to_image(template_src, context_dict={}):
    import imgkit
    template = get_template(template_src)
    html = template.render(context_dict)
    image = imgkit.from_string(html, False)
    return HttpResponse(image, content_type='application/jpg')


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if pdf.err == 0:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
