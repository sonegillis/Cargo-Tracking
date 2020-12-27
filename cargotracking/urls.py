"""cargotracking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from track.views import (
    home, services, ground_transport, cargo, ware_housing, logistic_service,
    truck_service, storage, about, tracking, newsfeed, contact, article,
    tracking_information, tracking_not_found, send_message, search_package,
    update_package_destination, site_suspended, receipt
                        )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^services/$', services, name='services'),
    url(r'^services/ground-transport/$', ground_transport, name='services_ground_transport'),
    url(r'^services/cargo/$', cargo, name='services_cargo'),
    url(r'^services/ware-housing/$', ware_housing, name='services_ware_housing'),
    url(r'^services/logistic-service/$', logistic_service, name='services_logistic_service'),
    url(r'^services/truck-service/$', truck_service, name='services_truck_service'),
    url(r'^services/storage/$', storage, name='services_storage'),
    url(r'^about/$', about, name='about'),
    url(r'^tracking/$', tracking, name='tracking'),
    url(r'^tracking/not-found/$', tracking_not_found, name='tracking_not_found'),
    url(r'^tracking/(?P<tracking_code>SK\d{2}\d{3}\d{3}UK)/$', tracking_information, name='tracking_information'),
    url(r'^newsfeed/$', newsfeed, name='newsfeed'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^article/$', article, name='article'),
    url(r'^send-message/$', send_message, name="send_message"),
    url(r'^search-package/$', search_package, name="search-package"),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^update-package-destination/(?P<tracking_code>SK\d{2}\d{3}\d{3}UK)/$', update_package_destination, name="update_package_destination"),
    url(r'^suspend/$', site_suspended, name="site_suspended"),
    url(r'^receipt/(?P<package_id>\w+)/$', receipt, name="receipt"),
]

admin.site.site_header = "Speedy Globe Courier Admin"
admin.site.site_title = "Speedy Globe Courier Admin"
admin.site.index_title = "Speedy Globe Courier Admin"
