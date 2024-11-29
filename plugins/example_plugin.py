from airflow.plugins_manager import AirflowPlugin
from flask import Blueprint

from views.example_view import ExampleView

bp = Blueprint(
    "example_plugin",
    __name__,
    template_folder="views/templates",
    static_folder="views/static",
    static_url_path="/example_plugin/static",
)


v_appbuilder_package = {
    "name": "Example View",
    "category": "Example Plugin",
    "view": ExampleView(),
}


# Defining the plugin class
class AirflowExamplePlugin(AirflowPlugin):
    name = "example_plugin"
    flask_blueprints = [bp]
    appbuilder_views = [v_appbuilder_package]
