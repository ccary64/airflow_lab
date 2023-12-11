```bash
mkdir -p ./volumes/loki
sudo chown 10001:10001 ./volumes/loki

mkdir -p ./volumes/grafana
sudo chown 472:472 ./volumes/grafana
```

https://github.com/sarahmk125/airflow-docker-metrics/blob/master/docker-compose.yml
https://github.com/astronomer/ap-vendor/blob/main/statsd-exporter/include/mappings-gen2.yml
https://github.com/astronomer/ap-vendor/blob/main/grafana/include/airflow-containers.json
https://docs.open-metadata.org/v1.2.x/connectors/pipeline/airflow/lineage-backend
https://github.com/luatnc87/modern-data-warehouse-modeling-and-data-quality-with-dbt-openmetadata
https://github.com/MarquezProject/marquez/blob/main/examples/airflow/docker-compose.yml