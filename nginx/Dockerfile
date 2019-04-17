FROM nginx:latest

COPY nginx.conf /etc/nginx/nginx.conf
COPY my_nginx.conf /etc/nginx/site-available/

RUN mkdir -p /etc/nginx/site-enabled/ \
    && ln -s /etc/nginx/site-available/my_nginx.conf /etc/nginx/site-enabled/

CMD ["nginx", "-g", "daemon off;"]