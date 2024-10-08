FROM nginx:latest

RUN apt-get update &&  \
    apt-get upgrade -y && \
    logrotate \
    openssl \
    bash

COPY nginx.conf /etc/nginx/nginx.conf
COPY conf.d/default.conf /etc/nginx/conf.d/default.conf

RUN mkdir -p /nginx-cache/hfs


# Create 'messages' file used from 'logrotate'
RUN touch /var/log/messages

# Copy 'logrotate' config file
COPY logrotate/nginx /etc/logrotate.d/

EXPOSE 80 443
