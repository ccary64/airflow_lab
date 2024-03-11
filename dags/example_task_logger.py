from airflow.decorators import dag, task
import pendulum
from task_logger import get_logger


logger = get_logger()


@dag(
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
)
def example_task_logger():

    @task
    def log_to_both():
        logger.add_static_fields({"test": 123})
        logger.info("test", extra={"this": "worked", "yup": "here too"})

    log_to_both()


example_task_logger()
