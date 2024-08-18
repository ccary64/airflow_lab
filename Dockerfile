FROM apache/airflow:2.6.3-python3.8

RUN pip install python-json-logger \
    apache-airflow-providers-databricks \
    opentelemetry-api \
    opentelemetry-sdk \
    airflow-provider-kafka \
    --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.6.3/constraints-3.8.txt"
