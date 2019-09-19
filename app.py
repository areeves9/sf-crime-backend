import datetime
from sqlalchemy import cast
from geoalchemy2 import Geography
import geoalchemy2.functions as geoalchemy2
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(
    __name__,
    instance_relative_config=True,
    template_folder="templates"
    )
# secret environment variables
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Incident


def get_thirty_days_vehicle_incidents(lng, lat, radius):
    d = datetime.date.today() - datetime.timedelta(days=100)
    incidents = Incident.query.filter(Incident.incident_datetime.between(
        d, datetime.date.today())).filter(geoalchemy2.ST_DWithin(
            Incident.point, 
            (cast(geoalchemy2.ST_MakePoint(lng, lat), Geography)), radius), 
            Incident.incident_subcategory.like('%Vehicle%')).all()
    return jsonify(
        results=len(incidents), 
        incidents=[incident.serialize for incident in incidents])


@app.route(
    # use werkzeug bulit-in float converter (signed=True)
    '/vehicles/<float(signed=True):longitude>/<float(signed=True):latitude>/<int:radius>',
    methods=['GET']
    )
def vehicle_incidents(longitude, latitude, radius):
    if request.method == 'GET':
        return get_thirty_days_vehicle_incidents(longitude, latitude, radius)


if __name__ == '__main__':
    app.run()
