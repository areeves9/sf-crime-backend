import csv
from sqlalchemy.exc import SQLAlchemyError as e
from app import db
from models import Incident

# creates a model instance for the db table Incident
def create_incident_instance(row):
    i = Incident(
        incident_datetime=row['Incident Datetime'],
        incident_date=row['Incident Date'],
        incident_time=row['Incident Time'],
        incident_year=row['Incident Year'],
        incident_day_of_the_week=row['Incident Day of Week'],
        report_datetime=row['Report Datetime'],
        row_id=row['Row ID'],
        incident_id=row['Incident ID'],
        incident_number=row['Incident Number'],
        cad_number=row['CAD Number'],
        report_type_code=row['Report Type Code'],
        report_type_description=row['Report Type Description'],
        filed_online=row['Filed Online'],
        incident_code=row['Incident Code'],
        incident_category=row['Incident Category'],
        incident_subcategory=row['Incident Subcategory'],
        incident_description=row['Incident Description'],
        resolution=row['Resolution'],
        intersection=row['Intersection'],
        cnn=row['CNN'],
        police_district=row['Police District'],
        analysis_neighborhood=row['Analysis Neighborhood'],
        supervisor_district=row['Supervisor District'],
        latitude=row['Latitude'],
        longitude=row['Longitude'],
        point=row['point'],
        )
    print("...adding Incident #%s, Row ID: %s" % (i.incident_id, i.row_id))    
    db.session.add(i)
    print("...adding Incident #%s, Row ID: %s" % (i.incident_id, i.row_id))


def seed_db():
    try:
        print("Seeding database, this will take several minutes...")
        
        with open('sf_crime_2018.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if not row['point'] and not row['Intersection']:
                    pass
                else:
                    create_incident_instance(row)
            db.session.commit()
            print("Database seeded!")
    except e:
        print("Database error. Update aborted.")
        db.session.rollback()
