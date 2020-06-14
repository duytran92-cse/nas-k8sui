#test_ingress.py
from __future__ import unicode_literals
import os, sys
from django.core.management.base import BaseCommand
from django.contrib.staticfiles import finders
from django.conf import settings
from application.modules.common import components as common_components

class Command(BaseCommand):
    def handle(self, *args, **options):
        kubeapi = common_components.KubernetesAPI()

        result = kubeapi.list_ingress('', {
        	'apiVersion': 'extensions/v1beta1',
        	'kind': 'Ingress',
        	'metadata':{
        		'name': 'test-ingress-aloha'
        	},
        	'spec':{
                'rules':{
        		    'backend':{
        			    'serviceName': 'echoheaders-service',
        			    'servicePort': 80
        		}
        	}
        }})
        print result                  
