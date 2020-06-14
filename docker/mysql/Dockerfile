FROM mysql:5.5

## Default password
ENV MYSQL_ROOT_PASSWORD 123456

## Configuration MySQL Server
ADD config/mysql.cnf /etc/mysql/conf.d/mysql.cnf
RUN chmod a-w /etc/mysql/conf.d/mysql.cnf
