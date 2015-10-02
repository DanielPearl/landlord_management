from django.conf.urls import include, url
from buildings import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'landlord_mgmt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.buildings, name="buildings"),
    url(r'^building_form', views.building_form, name="building_form")
]
