import pandas as pd
from datetime import datetime
from airflow.decorators import task
from airflow.models import DAG
from pyspark.sql import SparkSession
from pyspark import SparkContext


@task.pyspark()
def spark_task(spark: SparkSession, sc: SparkContext) -> pd.DataFrame:
    df = spark.createDataFrame(
        [
            (1, "John Doe", 21),
            (2, "Jane Doe", 22),
            (3, "Joe Bloggs", 23),
        ],
        ["id", "name", "age"],
    )
    df.show()

    return df.toPandas()

with DAG(
    dag_id="pyspark_demo",
    schedule_interval=None,
    start_date=datetime(2024,9,10),
) as dag:
    spark_task()