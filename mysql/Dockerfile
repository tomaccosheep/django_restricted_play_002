FROM mysql/mysql-server:latest
MAINTAINER Al Burns "al.burns.email@gmail.com"
RUN yum install -y vim
EXPOSE 3306
#ENV MYSQL_DATABASE=db
#ENV MYSQL_USER=mysql
#ENV MYSQL_ROOT_PASSWORD=Viapjor5
#VOLUME ["/var/lib/mysql"]
#RUN echo "bind-address = 0.0.0.0" >> /etc/my.cnf
ENTRYPOINT ["/entrypoint.sh"]
CMD ["mysqld"]
