import os

from airflow.www.auth import has_access
from airflow.utils.log.logging_mixin import LoggingMixin
from airflow.security import permissions

from flask_appbuilder import expose, BaseView as AppBuilderBaseView


# Creating a flask appbuilder BaseView
class ExampleView(AppBuilderBaseView, LoggingMixin):
    default_view = "index"

    @expose("/")
    @has_access(
        [
            (permissions.ACTION_CAN_READ, permissions.RESOURCE_WEBSITE),
        ]
    )
    def index(self):
        env_vars = [
            {"key": key, "value": value}
            for key, value in sorted(os.environ.items())
            if key.startswith("AIRFLOW_")
        ]
        headers = [{"name": "Key", "value": "key"}, {"name": "Value", "value": "value"}]
        return self.render_template(
            "basic_table.html",
            title="Airflow Env Vars",
            headers=headers,
            rows=env_vars,
        )
