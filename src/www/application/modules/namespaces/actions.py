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

class List(actions.crud.ListAction):
    class TableRenderer(renderers.widgets.table.DataTableRenderer):
        def render_cell_actions(self, table, row):
            html  = '<div class="btn-group btn-group">'
            html += '<a class="btn btn-xs btn-primary" href="javascript:showPopup(\'/namespaces/view/%s\')">View</a>' % (row['name'])
            html += '<a class="btn btn-xs btn-success" href="/namespaces/detail/%s/pods/list">Detail</a>' % (row['name'])
            html += '</div>'
            return html
    def create_table(self):
        table = widgets.table.DataTable()
        table.is_hide_paginator = True
        table.set_title('Namespaces')
        table.set_subtitle('List of namespaces')
        table.create_column('name', 'Name', '85%')
        table.create_column('actions', '', '15%')
        table.add_field(widgets.field.Textbox('text'))
        table.renderer = self.TableRenderer()
        table.renderer.table_form_renderer = renderers.widgets.form.TableFormRenderer()
        table.renderer.table_form_renderer.add_field('text', 'Text', colspan=12)
        table.renderer.table_form_renderer.set_field_renderer('textbox', renderers.widgets.field.TextboxRenderer())
        return table
    def load_table_data(self, table_form_data, sortkey, sortdir, page_number):
        data = {}
        kubeapi = common_components.KubernetesAPI()
        namespaces = kubeapi.list_namespaces()

        records = []
        for item in namespaces['items']:
            records.append({
                'id':                item['metadata']['uid'],
                'timestamp':         item['metadata']['creationTimestamp'],
                'name':              item['metadata']['name'],
            })

        data['records'] = records
        data['total_matched'] = len(records)
        return data


class View(common_actions.ViewAction):
    def build_view_widget(self, widget, params):
        kubeapi = common_components.KubernetesAPI()

        widget.title = 'Namespace'
        widget.content = kubeapi.get_namespace(params['name'])
