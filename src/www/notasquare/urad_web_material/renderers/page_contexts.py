from django.template import loader
from notasquare.urad_web.renderers import BaseRenderer

class FullPageContextRenderer(BaseRenderer):
    def __init__(self):
        super(FullPageContextRenderer, self).__init__()
        self.template = 'material/page_contexts/full.html'
    def render(self, full_page_context):
        template = loader.get_template(self.template)
        context = {
            'app_title':      full_page_context.app_title,
            'page_title':     full_page_context.page_title,
            'menu':           full_page_context.menu,
            'submenu':        full_page_context.submenu,
            'breadcrumb':     full_page_context.breadcrumb
        }

        widget_html = ''
        for widget in full_page_context.widgets:
            widget_html += widget.render()
        context['widget_html'] = widget_html

        return template.render(context)

class PopupPageContextRenderer(BaseRenderer):
    def __init__(self):
        super(PopupPageContextRenderer, self).__init__()
        self.template = 'material/page_contexts/popup.html'
    def render(self, popup_page_context):
        template = loader.get_template(self.template)
        context = {}

        widget_html = ''
        for widget in popup_page_context.widgets:
            widget_html += widget.render()
        context['widget_html'] = widget_html

        return template.render(context)
