FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY natoolbox.conf /etc/nginx/conf.d/

RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf
