import datetime
from sqlalchemy import cast
from geoalchemy2 import Geography
import geoalchemy2.functions as geoalchemy2
from flask import Flask, request, jsonify
from flask_cors import cross_origin
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


def get_timedelta():
    d = datetime.date.today() - datetime.timedelta(days=100)
    return d


def get_thirty_days_vehicle_incidents(lng, lat, radius, page, per_page):
    filtered_incidents = (
        Incident.query.filter(
            Incident.incident_datetime.between(
                get_timedelta(), datetime.date.today())
        ).filter(
            geoalchemy2.ST_DWithin(
                Incident.point, (
                    cast(
                        geoalchemy2.ST_MakePoint(lng, lat), Geography
                        )
                    ), radius
                ), Incident.incident_subcategory.like('%Vehicle%')))

    vehicle_incidents = filtered_incidents.paginate(
        page,
        per_page,
        False
        ).items

    pages = filtered_incidents.paginate(page, per_page, False).pages

    return jsonify(
        meta={
            "total_incidents": filtered_incidents.count(),
            "current_page": request.args.get(
                'page',
                default=1,
                type=int
                ),
            "per_page": request.args.get(
                'limit',
                default=20,
                type=int
                ),
            "pages": pages,
        },
        vehicle_incidents=[incident.serialize for incident in vehicle_incidents],
        )


# send get request to dynamic url: 127.0.0.1:5000/vehicles/lat/<latitude>/lng/<longitude>
@app.route(
    # signed=True allows negative floats
    '/vehicles/lat/<float(signed=True):latitude>/lng/<float(signed=True):longitude>/<int:radius>/',
    methods=['GET']
    )
@cross_origin()
def vehicle_incidents(longitude, latitude, radius):
    if request.method == 'GET':
        page = request.args.get(
            'page',
            default=1,
            type=int
            )
        per_page = request.args.get(
            'limit',
            default=20,
            type=int
            )
        return get_thirty_days_vehicle_incidents(
            longitude,
            latitude,
            radius,
            page,
            per_page
        )

if __name__ == '__main__':
    app.run()
