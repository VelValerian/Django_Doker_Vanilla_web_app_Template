# 🐳 STACK INFRASTRUCTURE (V2.0) - STYLES
FROM node:20-slim

# 🏗️ ENVIRONMENT SETUP
WORKDIR /src
RUN npm install -g sass

# 🌀 WATCHER SERVICE
CMD ["sass", "--watch", "web/asset/scss/styles.scss:web/static/css/styles.css"]
