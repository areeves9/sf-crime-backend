This project is about getting practice working with 
Flask - python microframework similar to Express.js
to serve JSON responses at specific URIs. The intention
is to be RESTful. A front-end JS client consumes these
resources and displays JSON data in HTML.

Note: Env vars are kept in conda env vars: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#saving-environment-variables

Create a database using psql command.
Add POSTGIS extension to databse.
Run flask db init to create the migration directory.
Then flask db migrate to create migration files.
Comment out the 'drop spatial databse' line in the migration file.
Import geoalchemy2 in the migration file.


Run import download_csv.py from flask shell to fetch the CSV file from the 
SF Open Crime Data project. This also populates the db.

Must be in flask shell otherwise conda env vars won't be recognized.

Push local db to remote db on heroku.
