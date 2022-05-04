from django.db import connection
from functools import wraps
from logger.models import Logger
from time import time


class LoggerDecorator:
    def __init__(
        self,
        sql_query_count=True,
        sql_query_time=True,
        function_time=True,
        user_pk=True,
        user_agent=True,
        remote_addr=True
    ):
        self.key_filter = {
            "gql_query_name": True,
            "sql_query_count": sql_query_count,
            "sql_query_time": sql_query_time,
            "function_time": function_time,
            "user_pk": user_pk,
            "user_agent": user_agent,
            "remote_addr": remote_addr
        }

    def __call__(self, f):
        @wraps(f)
        def wrap(*args, **kw):
            if len(args) == 2:
                root, info = args
            else:
                cls, root, info = args
            user_pk = info.context.user.pk
            user_agent = info.context.headers["User-Agent"]
            remote_addr = info.context.META["REMOTE_ADDR"]
            time_before = time()
            result = f(*args, **kw)
            time_after = time()
            function_time = time_after - time_before
            logger_dict = {"gql_query_name": f.__qualname__,
                           "sql_query_count": len(connection.queries),
                           "sql_query_time": sum([float(q["time"]) for q in connection.queries]),
                           "function_time": function_time,
                           "user_pk": user_pk,
                           "user_agent": user_agent,
                           "remote_addr": remote_addr}
            filtered_logs = {key: logger_dict[key] for key in logger_dict.keys() & self.key_filter.keys() if self.key_filter[key]}
            Logger.objects.create(**filtered_logs)
            return result

        return wrap



