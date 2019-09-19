from app import db
from geoalchemy2.types import Geometry


class Incident(db.Model):
    """
    This model schema is taken directly from CSV available
    at SF Open Data SODA API for SFPD crime incident records
    and reports from 2018 to present. The point model attribute
    is set to a database column of type Geometry, available
    through the Postgis extension for PostgreSQL.
    """
    id = db.Column(db.Integer, primary_key=True)
    incident_datetime = db.Column(db.DateTime)
    incident_date = db.Column(db.Date)
    incident_time = db.Column(db.Time)
    incident_year = db.Column(db.Integer)
    incident_day_of_the_week = db.Column(db.String(12), unique=False)
    report_datetime = db.Column(db.DateTime)
    row_id = db.Column(db.BigInteger)
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
    point = db.Column(Geometry(geometry_type='Point'))

    # Take model instance and serialize as a JSON object.
    # This allows for data to be easily exchanged while
    # also easily convertable to its original type.
    # For unserializable objects use str()
    @property
    def serialize(self):
        return {
            'id': self.id,
            'incident_datetime': self.incident_datetime,
            'incident_date': self.incident_date,
            'incident_time': str(self.incident_time),
            'incident_year': self.incident_year,
            'incident_day_of_the_week': self.incident_day_of_the_week,
            'report_datetime': self.report_type_code,
            'row_id': self.row_id,
            'incident_id': self.incident_id,
            'incident_number': self.incident_number,
            'cad_number': self.cad_number,
            'report_type_code': self.report_type_code,
            'report_type_description': self.report_type_description,
            'filed_online': self.filed_online,
            'incident_code': self.incident_code,
            'incident_category': self.incident_subcategory,
            'incident_subcategory': self.incident_subcategory,
            'incident_description': self.incident_description,
            'resolution': self.resolution,
            'intersection': self.intersection,
            'cnn': self.cnn,
            'police_district': self.police_district,
            'analysis_neighborhood': self.analysis_neighborhood,
            'supervisor_district': self.supervisor_district,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'point': str(self.point),
        }
    
    def __repr__(self):
        return '<Incident ID %r>' % self.incident_id
