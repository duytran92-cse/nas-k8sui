import django, urllib, urllib2, json, ssl
from django.conf import settings

class KubernetesAPI(object):
    def __init__(self):
        self.cafile = settings.KUBERNETES_APISERVER_CAFILE
        self.keyfile = settings.KUBERNETES_APISERVER_KEYFILE
        self.crtfile = settings.KUBERNETES_APISERVER_CRTFILE
        self.url = settings.KUBERNETES_APISERVER_URL

    def GET(self, url, params = {}):
        ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_TLSv1_2)
        ctx.load_cert_chain(certfile=self.crtfile, keyfile=self.keyfile)
        ctx.load_verify_locations(cafile=self.cafile)
        res = urllib2.urlopen("https://" + self.url + "/" + url + "?" + urllib.urlencode(params), context=ctx)
        return json.loads(res.read())

    def GET2(self, url, params = {}, post_params = {}):
        ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_TLSv1_2)
        ctx.load_cert_chain(certfile=self.crtfile, keyfile=self.keyfile)
        ctx.load_verify_locations(cafile=self.cafile)
        res = urllib2.Request("https://" + self.url + "/" + urllib2, data=json.dumps(post_params), headers={'Content-Type': 'application/json'})
        res = urllib2.urlopen(res, context=ctx)
        return res.read()

    def POST(self, url, data = {}):
        ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_TLSv1_2)
        ctx.load_cert_chain(certfile=self.crtfile, keyfile=self.keyfile)
        ctx.load_verify_locations(cafile=self.cafile)
        res = urllib2.Request("https://" + self.url + "/" + url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
        res = urllib2.urlopen(res, context=ctx)
        return json.loads(res.read())


    # Nodes
    def list_nodes(self):
        return self.GET('api/v1/nodes')
    def get_node(self, name):
        return self.GET('api/v1/nodes/' + name)

    # Namespaces
    def list_namespaces(self):
        return self.GET('api/v1/namespaces')

    def get_namespace(self, name):
        return self.GET('api/v1/namespaces/' + name)

    # Services
    def list_services(self, namespace=''):
        if namespace == '':
            return self.GET('api/v1/services')
        return self.GET('api/v1/namespaces/%s/services' % (namespace))

    def get_service(self, namespace, name):
        return self.GET('api/v1/namespaces/' + namespace + '/services/' + name)

    # Pods
    def list_pods(self, namespace=''):
        if namespace == '':
            return self.GET('api/v1/pods')
        return self.GET('api/v1/namespaces/%s/pods' % (namespace))

    def get_pod(self, namespace, name):
        return self.GET('api/v1/namespaces/' + namespace + '/pods/' + name)

    # Replication controllers
    def list_replicationcontroller(self, namespace=''):
        if namespace == '':
            return self.GET('api/v1/namespaces/%s/replicationcontrollers')
        return self.GET('api/v1/namespaces/%s/replicationcontrollers' % (namespace))

    def get_replicationcontroller(self, namespace, name):
        return self.GET('api/v1/namespaces/' + namespace + '/replicationcontrollers/' + name)

    # Deployment
    def list_deployment(self, namespace=''):
        if namespace == '':
            return self.GET('apis/extensions/v1beta1/namespaces/default/deployments')
        return self.GET('apis/extensions/v1beta1/namespaces/%s/deployments/' % (namespace))

    def get_deployment(self, namespace, name):
        return self.GET('apis/extensions/v1beta1/namespaces/' + namespace + '/deployments/' + name)

    # create pod via API => POST json
    def create_deployment(self, namespace='', data = {}):
        if namespace == '':
            return self.POST('apis/extensions/v1beta1/namespaces/default/deployments', data)
        return self.POST('apis/extensions/v1beta1/namespaces/%s/deployments/' % (namespace), data)


    # Daemon Set
    def list_daemonset(self, namespace=''):
        if namespace == '':
            return self.GET('apis/extensions/v1beta1/namespaces/%s/daemonsets')
        return self.GET('apis/extensions/v1beta1/namespaces/%s/daemonsets/' % (namespace))

    def get_daemonset(self, namespace, name):
        return self.GET('apis/extensions/v1beta1/namespaces/' + namespace + '/daemonsets/' + name)

    # Stateful Set
    def list_statefulsets(self, namespace=''):
        if namespace == '':
            return self.GET('apis/apps/v1beta1/namespaces/%s/statefulsets')
        return self.GET('apis/apps/v1beta1/namespaces/%s/statefulsets/' % (namespace))

    def get_statefulsets(self, namespace, name):
        return self.GET('apis/apps/v1beta1/namespaces/' + namespace + '/statefulsets/' + name)

    # Replica Set
    def list_replicasets(self, namespace=''):
        if namespace == '':
            return self.GET('apis/extensions/v1beta1/namespaces/%s/replicasets')
        return self.GET('apis/extensions/v1beta1/namespaces/%s/replicasets/' % (namespace))

    def get_replicasets(self, namespace, name):
        return self.GET('apis/extensions/v1beta1/namespaces/' + namespace + '/replicasets/' + name)

    # Cron Jobs -- skip now because v2 is not available now
    def list_cronjobs(self, namespace=''):
        if namespace == '':
            return self.GET('apis/batch/v2alpha1/namespaces/%s/cronjobs')
        return self.GET('apis/batch/v2alpha1/namespaces/%s/cronjobs/' % (namespace))

    def get_cronjobs(self, namespace, name):
        return self.GET('apis/batch/v2alpha1/namespaces/' + namespace + '/cronjobs/' + name)

    # Ingress
    def list_ingress(self, namespace=''):
        if namespace == '':
            return self.GET('apis/extensions/v1beta1/namespaces/%s/ingresses')
        return self.GET('apis/extensions/v1beta1/namespaces/%s/ingresses/' % (namespace))

    def get_ingress(self, namespace, name):
        return self.GET('apis/extensions/v1beta1/namespaces/' + namespace + '/ingresses/' + name)

    # use api
    #def test_api(self, api, params):
    #    return self.GET2(api, {}, params)

    def create_ingress(self, namespace='', data = {}):
        if namespace == '':
            return self.POST('apis/extensions/v1beta1/namespaces/default/ingresses', data)
        return self.POST('apis/extensions/v1beta1/s/namespaces/ingresses/' % (namespace), data)

    # delete ingress        
    def delete_ingress(self, namespace='', data = {}):
        if namespace == '':
            return self.DELETE('apis/extensions/v1beta1/namespaces/default/ingresses', data)
        return self.DELETE('apis/extensions/v1beta1/s/namespaces/ingresses/' % (namespace), data)

    
