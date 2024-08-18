from copy import deepcopy
from airflow.config_templates.airflow_local_settings import (
    DEFAULT_LOGGING_CONFIG,
    LOG_FORMAT,
)


LOGGING_CONFIG = deepcopy(DEFAULT_LOGGING_CONFIG)

# Log the "extra" attributes to the UI log files
LOGGING_CONFIG["formatters"]["airflow_extra"] = {
    "format": LOG_FORMAT,
    "class": "task_logger.ExtraFormatter",
}
LOGGING_CONFIG["handlers"]["task"]["formatter"] = "airflow_extra"

# Create JSON handler for the stdout
LOGGING_CONFIG["handlers"]["console"] = {
    "class": "task_logger.HandlerWithJSON",
    "filters": ["mask_secrets"],
}
LOGGING_CONFIG["loggers"]["airflow.task"]["handlers"] = ["console", "task"]
LOGGING_CONFIG["loggers"]["airflow.processor"]["handlers"] = ["console", "processor"]
