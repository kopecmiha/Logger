from django.db import connection
from functools import wraps
from logger.models import Logger


def db_sql_logger(f):
    @wraps(f)
    def wrap(*args, **kw):
        result = f(*args, **kw)
        logger_dict = {"gql_query_name": f.__qualname__,
                       "sql_query_count": len(connection.queries),
                       "sql_query_time": sum([float(q["time"]) for q in connection.queries])}
        Logger.objects.create(**logger_dict)
        return result

    return wrap
