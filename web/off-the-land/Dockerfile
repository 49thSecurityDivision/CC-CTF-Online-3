FROM phusion/baseimage:focal-1.1.0

CMD ["/sbin/my_init"]

RUN apt-get update && \
      apt-get install -y apache2 php libapache2-mod-php sudo socat

RUN a2enmod rewrite proxy proxy_http headers ssl php7.4

RUN useradd -ms /bin/bash hacker

COPY user.txt /home/hacker/

RUN chown hacker /home/hacker/user.txt
RUN chmod 400 /home/hacker/user.txt

COPY root.txt /root/
RUN chown root /root/root.txt
RUN chmod 400 /root/root.txt

COPY cmd.php /var/www/html/cmd.php

RUN chown -R www-data:www-data /var/www
RUN chmod -R 0644 /var/www

RUN echo "www-data ALL=(hacker) NOPASSWD: /usr/bin/python3" >> /etc/sudoers.d/vulnerable
RUN echo "hacker ALL=(root) NOPASSWD: /usr/bin/socat" >> /etc/sudoers.d/vulnerable

RUN find /var/www -type d -exec chmod 755 {} \;
RUN find /var/www -type f -exec chmod 644 {} \;

EXPOSE 80

# RUN service apache2 start
