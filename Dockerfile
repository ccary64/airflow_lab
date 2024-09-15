FROM apache/airflow:2.10.1-python3.10

USER root

# Install OpenJDK for PySpark
RUN apt-get update && apt-get install -y openjdk-17-jdk && apt-get clean

# Set JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-amd64
ENV PATH $JAVA_HOME/bin:$PATH

USER airflow
RUN pip install python-json-logger apache-airflow[apache-spark]==$AIRFLOW_VERSION