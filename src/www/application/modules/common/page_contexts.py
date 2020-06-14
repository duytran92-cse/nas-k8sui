from notasquare.urad_web.page_contexts import standard
from notasquare.urad_web_material import renderers

class FullPageContext(standard.FullPageContext):
    def __init__(self):
        super(FullPageContext, self).__init__()
        self.app_title = 'Kubernetes Web UI'
        self.page_title = 'Kubernetes Web UI'
        self.breadcrumb.add_entry('home', 'Dashboard', '/')
        self.menu.create_menu_group('node', 'Nodes', '/nodes/list', 'zmdi-format-subject')
        self.menu.create_menu_group('namespaces', 'Namespaces', '/namespaces/list', 'zmdi-format-subject')
        self.renderer = renderers.page_contexts.FullPageContextRenderer()

class PopupPageContext(standard.PopupPageContext):
    def __init__(self, params, container):
        super(PopupPageContext, self).__init__()
        self.renderer = renderers.page_contexts.PopupPageContextRenderer()
