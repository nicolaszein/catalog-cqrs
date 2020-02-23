from pathlib import Path
from flask import Blueprint
from autodiscover import AutoDiscover


app = Blueprint('catalog', __name__)

routes_path = Path('catalog/web/api/routes')
autodiscover_routes = AutoDiscover(path=routes_path)
autodiscover_routes()
