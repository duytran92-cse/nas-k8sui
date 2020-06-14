FROM debian:jessie

ENV DEBIAN_FRONTEND noninteractive

# Install php nginx mysql supervisor wget
RUN apt-get update && \
    apt-get install -y apt-utils python python-dev python-pip libssl-dev build-essential nginx supervisor nano wget unzip python-mysqldb git-core && \
    rm -rf /var/lib/apt/lists/*

# Install uWSGI
RUN pip install uwsgi
RUN pip install Django==1.9.11

# Config uWSGI
ADD uwsgi/uwsgi.ini /opt/uwsgi.ini

# Config nginx
RUN unlink /etc/nginx/sites-enabled/default
ADD nginx/web /etc/nginx/sites-enabled/web
RUN mkdir /opt/www/
RUN mkdir /opt/web/
RUN mkdir /opt/web/static/

# Kubernetes
RUN mkdir /opt/kubernetes
ADD kubernetes/dev/apiserver-ca.pem /opt/kubernetes/apiserver-ca.pem
ADD kubernetes/dev/apiserver-cert.pem /opt/kubernetes/apiserver-cert.pem
ADD kubernetes/dev/apiserver-key.pem /opt/kubernetes/apiserver-key.pem

# Config supervisor
ADD supervisor/uwsgi.conf /etc/supervisor/conf.d/uwsgi.conf
ADD supervisor/nginx.conf /etc/supervisor/conf.d/nginx.conf

ENV APP_ENV dev

# Export
WORKDIR /opt/www/
VOLUME /opt/www/
EXPOSE 80

CMD ["/usr/bin/supervisord", "--nodaemon", "-c", "/etc/supervisor/supervisord.conf"]
