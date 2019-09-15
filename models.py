from app import db
from geoalchemy2.types import Geometry


class Incident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    incident_datetime = db.Column(db.DateTime)
    incident_date = db.Column(db.Date)
    incident_time = db.Column(db.Time)
    incident_year = db.Column(db.Integer)
    incident_day_of_the_week = db.Column(db.String(12), unique=False)
    report_datetime = db.Column(db.DateTime)
    row_id = db.Column(db.Numeric)
    incident_id = db.Column(db.Integer)
    incident_number = db.Column(db.Integer)
    cad_number = db.Column(db.String(12))
    report_type_code = db.Column(db.String(12), unique=False)
    report_type_description = db.Column(db.Text)
    filed_online = db.Column(db.String(12))
    incident_code = db.Column(db.String(12), unique=False)
    incident_category = db.Column(db.Text)
    incident_subcategory = db.Column(db.Text)
    incident_description = db.Column(db.Text)
    resolution = db.Column(db.Text)
    intersection = db.Column(db.Text)
    cnn = db.Column(db.String(12))
    police_district = db.Column(db.String(30), unique=False)
    analysis_neighborhood = db.Column(db.String(30), unique=False)
    supervisor_district = db.Column(db.String(12))
    latitude = db.Column(db.Float, None)
    longitude = db.Column(db.Float, None)
    point = db.Column(Geometry('Point'))

    def __repr__(self):
        return '<Incident ID %r>' % self.incident_id
