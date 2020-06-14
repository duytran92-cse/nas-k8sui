from __future__ import unicode_literals
import os, sys
from django.core.management.base import BaseCommand
from django.contrib.staticfiles import finders
from django.conf import settings
from application.modules.common import components as common_components

class Command(BaseCommand):
    def handle(self, *args, **options):
    	kubeapi = common_components.KubernetesAPI()

    	result = kubeapi.create_deployment('', {
    		'kind': 'Deployment',
    		'metadata': {
    			'name': 'test-my-deployment'
    		},
    		'spec': {
    			'replicas': 1,
    			'template': {
    				'metadata': {
    					'labels': {
    						'app': 'test-my-deployment'
    					}
    				},
    				'spec': {
    					'containers': [
    						{
    							'name': 'echoheaders-server-container',
    							'image': 'gcr.io/google_containers/echoserver:1.4',
    							'ports': [
    								{
    									'containerPort': 80,
    									'hostPort': 80
    								}
    							]
    						}
    					]
    				}
    			}
    		}
    	})

    	print result


                    
