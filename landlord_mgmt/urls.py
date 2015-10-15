from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'landlord_mgmt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^buildings/', include('buildings.urls', namespace="buildings")),
    # url(r'^$', include('buildings.urls', namespace="none")),
    url(r'^$', 'buildings.views.login_user', name='login'),
    url(r'^logout/', 'buildings.views.logout_user', name='logout'),
    url(r'^buildings/', include('buildings.urls', namespace="buildings"))

]
