from django.conf import settings
from application.modules.common import page_contexts

class PageFullPageContext(page_contexts.FullPageContext):
    def __init__(self, params, container):
        super(PageFullPageContext, self).__init__()

        self.submenu.create_menu_group('dashboard',     'Dashboard',         '/namespaces/dashboard',                                  'zmdi-border-all')
        self.submenu.create_menu_group('pods',          'Pods',              '/namespaces/detail/%s/pods/list' % (params['namespace']),       'zmdi-border-all')
        self.submenu.create_menu_group('services',      'Services',          '/namespaces/detail/%s/services/list' % (params['namespace']),   'zmdi-border-all')
	self.submenu.create_menu_group('deployments',   'Deployment',        '/namespaces/detail/%s/deployments/list' % (params['namespace']),  'zmdi-border-all')
        self.submenu.create_menu_group('replicasets',   'Replica Sets',      '/namespaces/detail/%s/replicasets/list' % (params['namespace']),  'zmdi-border-all')
        self.submenu.create_menu_group('replicationcontroller','Replication Controller','/namespaces/detail/%s/replicationcontroller/list' % (params['namespace']),'zmdi-border-all')
        self.submenu.create_menu_group('daemonsets',    'Daemon Set',        '/namespaces/detail/%s/daemonsets/list' % (params['namespace']),   'zmdi-border-all')
        self.submenu.create_menu_group('statefulsets',  'Stateful Sets',     '/namespaces/detail/%s/statefulsets/list' % (params['namespace']),  'zmdi-border-all')
        self.submenu.create_menu_group('Ingress',       'Ingress',     	     '/namespaces/detail/%s/ingress/list' % (params['namespace']),  'zmdi-border-all') 
