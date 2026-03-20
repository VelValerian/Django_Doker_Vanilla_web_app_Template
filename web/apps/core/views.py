from django.http import JsonResponse
from django.db import connections
from django.db.utils import OperationalError
from django_redis import get_redis_connection


def health_check_view(request):
    """
    🌀 HEALTH CHECK V2.0
    Проверка состояния БД и Redis для мониторинга контейнеров.
    """
    health_status = {
        "status": "ok",
        "services": {
            "database": "down",
            "redis": "down"
        }
    }

    # 1. Проверка Базы Данных
    try:
        db_conn = connections['default']
        db_conn.cursor()
        health_status["services"]["database"] = "up"
    except OperationalError:
        health_status["status"] = "error"

    # 2. Проверка Redis
    try:
        get_redis_connection("default").ping()
        health_status["services"]["redis"] = "up"
    except Exception:
        health_status["status"] = "error"

    return JsonResponse(health_status, status=200 if health_status["status"] == "ok" else 503)
