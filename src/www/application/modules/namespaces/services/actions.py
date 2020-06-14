import json
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.template import loader
from notasquare.urad_web import actions, page_contexts, widgets
from notasquare.urad_web_material import renderers
from notasquare.urad_web.renderers import BaseRenderer
from application import constants
from application.modules.common import components as common_components
from application.modules.common import actions as common_actions
from application.modules.namespaces import components as namespaces_components

class List(actions.crud.ListAction):
    def create_page_context(self):
        return namespaces_components.PageFullPageContext(self.params, self.get_container())
    class TableRenderer(renderers.widgets.table.DataTableRenderer):
        def render_cell_actions(self, table, row):
            html  = '<div class="btn-group btn-group">'
            html += '<a class="btn btn-xs btn-primary" href="javascript:showPopup(\'/namespaces/detail/%s/services/view/%s\')">View</a>' % (self.params['namespace'], row['name'])
            html += '</div>'
            return html
        def render_cell_labels(self, table, row):
            html = ''
            for k, v in row['labels'].iteritems():
                html += '<text>%s=%s</text><br/>' % (k, v)
            return html
    def create_table(self):
        table = widgets.table.DataTable()
        table.is_hide_paginator = True
        table.set_title('Services')
        table.set_subtitle('List of services')
        table.create_column('name', 'Name', '55%')
        table.create_column('labels', 'Labels', '20%')
        table.create_column('actions', '', '15%')
        table.add_field(widgets.field.Textbox('text'))
        table.renderer = self.TableRenderer()
        table.renderer.params = self.params
        table.renderer.table_form_renderer = renderers.widgets.form.TableFormRenderer()
        table.renderer.table_form_renderer.add_field('text', 'Text', colspan=12)
        table.renderer.table_form_renderer.set_field_renderer('textbox', renderers.widgets.field.TextboxRenderer())
        return table
    def load_table_data(self, table_form_data, sortkey, sortdir, page_number):
        data = {}
        kubeapi = common_components.KubernetesAPI()
        services = kubeapi.list_services(self.params['namespace'])

        records = []
        for item in services['items']:
            records.append({
                'id':                item['metadata']['uid'],
                'timestamp':         item['metadata']['creationTimestamp'],
                'name':              item['metadata']['name'],
                'labels':            item['metadata']['labels']
            })

        data['records'] = records
        data['total_matched'] = len(records)
        return data


class View(common_actions.ViewAction):
    def build_view_widget(self, widget, params):
        kubeapi = common_components.KubernetesAPI()

        widget.title = 'Service'
        widget.content = kubeapi.get_service(params['namespace'], params['name'])
