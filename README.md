## SQL Logger Readme

### Модуль для django logger включает в себя:

- Модель "Logger" для сохранения статистики в базу данных

Параметр gql_query_name - Имя вызываемого класса и функции

Параметр sql_query_count - Колличество sql запросов

Параметр sql_query_time - Общее время выполнения sql запросов

- Декоратор "db_sql_logger"

### Пример использования для функций query и mutation

```
@classmethod
@db_sql_logger
@login_required
@Permission(
    instance=Folder,
    allow_permission={"is_editor": True},
    # role_permission={"root_locked": True}, # TODO: Task frontend is not completed
)
def mutate(cls, root, info, **kwargs):  # NOQA

    parent = kwargs.get("container_folder")
    user = info.context.user
```

```
@db_sql_logger
@login_required
@Permission(
    instance=Lesson,
    allow_permission={"is_viewer": True},
    # is_published=False,
)
def resolve_lesson_by_id(root, info, **kwargs):
    requested_instance = kwargs["requested_instance"]
    return requested_instance
```
