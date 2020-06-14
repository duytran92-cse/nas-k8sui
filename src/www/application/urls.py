from django.conf.urls import include, url

urlpatterns = [
    url(r'^nodes/',                   include('application.modules.nodes.urls')),
    url(r'^namespaces/',              include('application.modules.namespaces.urls')),
]
