from django.db import models


class Logger(models.Model):
    gql_query_name = models.CharField(
        null=True, blank=True, max_length=100
    )
    sql_query_count = models.IntegerField(null=True)
    sql_query_time = models.FloatField(null=True)
    function_time = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user_pk = models.CharField(null=True, blank=True, max_length=100)
    user_agent = models.CharField(null=True, blank=True, max_length=1000)
    remote_addr = models.CharField(null=True, blank=True, max_length=100)
