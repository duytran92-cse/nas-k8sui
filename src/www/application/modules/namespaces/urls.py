
from django.conf.urls import include, url
from . import actions

urlpatterns = [
    url(r'^list$',                                         actions.List.as_view(),     name='namespaces_list'),
    url(r'^view/(?P<name>([A-Za-z0-9\-\_]+))',             actions.View.as_view(),     name='namespaces_view'),
    # Pods
    url(r'^detail/(?P<namespace>([A-Za-z0-9\-\_]+))/pods/',          include('application.modules.namespaces.pods.urls')),
    # Services
    url(r'^detail/(?P<namespace>([A-Za-z0-9\-\_]+))/services/',      include('application.modules.namespaces.services.urls')),
    # Replication Controller
    url(r'^detail/(?P<namespace>([A-Za-z0-9\-\_]+))/replicationcontroller/', include('application.modules.namespaces.replicationcontroller.urls')),
    # Daemon Sets
    url(r'^detail/(?P<namespace>([A-Za-z0-9\-\_]+))/daemonsets/',  include('application.modules.namespaces.daemonsets.urls')),
    # Deployments
    url(r'^detail/(?P<namespace>([A-Za-z0-9\-\_]+))/deployments/',  include('application.modules.namespaces.deployments.urls')),
    # Replica Sets
    url(r'^detail/(?P<namespace>([A-Za-z0-9\-\_]+))/replicasets/',  include('application.modules.namespaces.replicasets.urls')),
    # Stateful Sets
    url(r'^detail/(?P<namespace>([A-Za-z0-9\-\_]+))/statefulsets/', include('application.modules.namespaces.statefulsets.urls')),
    # Cron Jobs
    url(r'^detail/(?P<namespace>([A-Za-z0-9\-\_]+))/cronjobs/', include('application.modules.namespaces.cronjobs.urls')),
    # Ingress
    url(r'^detail/(?P<namespace>([A-Za-z0-9\-\_]+))/ingress/', include('application.modules.namespaces.ingress.urls')),
    # Create pod
    url(r'^detail/(?P<namespace>([A-Za-z0-9\-\_]+))/create/', include('application.modules.namespaces.create.urls')),
]
