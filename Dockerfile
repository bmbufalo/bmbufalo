FROM nginxinc/nginx-unprivileged:stable

COPY site/ /usr/share/nginx/html