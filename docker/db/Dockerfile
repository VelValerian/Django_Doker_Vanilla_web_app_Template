# 🐳 STACK INFRASTRUCTURE (V2.0) - DB
FROM postgres:16-alpine

# 🌐 HEALTH CHECK (V2.0)
HEALTHCHECK --interval=5s --timeout=5s --retries=5 \
    CMD pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}
