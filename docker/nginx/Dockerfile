FROM nginx:alpine

# 🏗️ ENVIRONMENT SETUP
COPY docker/nginx/default.conf /etc/nginx/conf.d/default.conf

# 🧹 CLEAN UP
RUN rm -rf /var/cache/apk/*
