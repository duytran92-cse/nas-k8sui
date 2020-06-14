import json
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.template import loader
from notasquare.urad_web import actions, page_contexts, widgets
from notasquare.urad_web.renderers import BaseRenderer
from notasquare.urad_web_material import renderers
from application import constants
from application.modules.common import page_contexts as common_page_contexts
from . import components

class ViewAction(actions.BaseAction):
    def create_page_context(self):
        return common_page_contexts.PopupPageContext(self.params, self.get_container())
    class ViewWidget(widgets.BaseWidget):
        class ViewRenderer(BaseRenderer):
            def render(self, widget):
                template = loader.get_template('material/common/view.html')
                context = {}
                context['title'] = widget.title
                context['content'] = json.dumps(widget.content, indent=4)
                return template.render(context)
        def build(self, params):
            self.set_renderer(self.ViewRenderer())
    def create_view_widget(self, params):
        widget = self.ViewWidget()
        widget.container = self.get_container()
        widget.build(params)
        self.build_view_widget(widget, params)
        return widget
    def GET(self):
        self.page_context = self.create_page_context()
        self.page_context.add_widget(self.create_view_widget(self.params))
        return HttpResponse(self.page_context.render())
