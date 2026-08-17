FROM nginxinc/nginx-unprivileged:stable

COPY public/ /usr/share/nginx/html
