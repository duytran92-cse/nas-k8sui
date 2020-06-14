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
            html += '<a class="btn btn-xs btn-primary" href="javascript:showPopup(\'/nodes/view/%s\')">View</a>' % (row['name'])
            html += '</div>'
            return html
        def render_cell_capacity(self, table, row):
            return '%s / %s / %s pods' % (row['capacity']['cpu'], row['capacity']['memory'], row['capacity']['pods'])
        def render_cell_address(self, table, row):
            html = ''
            for addr in row['addresses']:
                html += '<text>%s (%s)</text><br/>' % (addr['address'], addr['type'])
            return html
    def create_table(self):
        table = widgets.table.DataTable()
        table.is_hide_paginator = True
        table.set_title('Nodes')
        table.set_subtitle('List of nodes')
        table.create_column('name', 'Name', '15%')
        table.create_column('capacity', 'Capacity', '20%')
        table.create_column('address', 'Address', '20%')
        table.create_column('info', 'Info', '30%')
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
        nodes = kubeapi.list_nodes()

        records = []
        for item in nodes['items']:
            records.append({
                'id':                item['metadata']['uid'],
                'timestamp':         item['metadata']['creationTimestamp'],
                'name':              item['metadata']['name'],
                'capacity': {
                    'pods':              item['status']['capacity']['pods'],
                    'cpu':               item['status']['capacity']['cpu'],
                    'memory':            item['status']['capacity']['memory'],
                },
                'addresses':         item['status']['addresses']
            })

        data['records'] = records
        data['total_matched'] = len(records)
        return data



class View(common_actions.ViewAction):
    def build_view_widget(self, widget, params):
        kubeapi = common_components.KubernetesAPI()

        widget.title = 'Nodes'
        widget.content = kubeapi.get_node(params['name'])
