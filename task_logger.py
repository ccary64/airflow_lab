import sys
import logging

from functools import partial
from pythonjsonlogger.jsonlogger import JsonFormatter, RESERVED_ATTRS
from airflow.utils.log.timezone_aware import TimezoneAware


def get_handlers(logger):
    c = logger
    handlers = []
    while c:
        if c.handlers:
            for handler in c.handlers:
                if isinstance(handler, HandlerWithJSON):
                    handlers.append(handler)
        if not c.propagate:
            break
        else:
            c = c.parent
    return handlers


def add_static_fields(self, extras):
    handlers = get_handlers(self)
    for handler in handlers:
        handler.add_static_fields(extras)


def get_logger():
    logger = logging.getLogger("airflow.task")
    logger.add_static_fields = partial(add_static_fields, logger)
    return logger


class HandlerWithJSON(logging.StreamHandler):
    def __init__(self, *_):
        super().__init__(stream=sys.stdout)
        self.setLevel(logging.INFO)
        self.setFormatter(
            JsonFormatter(
                "[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s",
                static_fields={"app_name": "airflow"},
                datefmt="%Y-%m-%dT%H:%M:%S",
            )
        )

    def add_static_fields(self, static_fields):
        self.formatter.static_fields.update(static_fields)

    def set_context(self, ti):
        if not isinstance(ti, str) and not ti.raw:
            self.add_static_fields(
                {
                    "dag_id": str(ti.dag_id),
                    "task_id": str(ti.task_id),
                    "try_number": str(ti.try_number),
                }
            )


class ExtraFormatter(TimezoneAware):
    def format(self, record):
        extra = "\t"
        for key, value in record.__dict__.items():
            # this allows to have numeric keys
            if key not in RESERVED_ATTRS and not (
                hasattr(key, "startswith") and key.startswith("_")
            ):
                extra += f"| {key}={value} "
        return super().format(record) + extra
