from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData
import os

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)

database_url =os.getenv('DATABASE_URL')

# database_url ='postgres://u8o7lasmharbq1:p671fb6b9ee7752b360f06d7b5cdc0c781427b938d1e3601862a2aeb6a3ea9b2f@cb4l59cdg4fg1k.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d99nb7lr00tna7'

# database_url='postgresql://jvkhatepulwmsq:4db6729008abc739d7bfdeefd19c6a6459e38f9b7dbd1b3bda2e95de5eb3d01c@ec2-54-83-138-228.compute-1.amazonaws.com:5432/d33ktsaohkqdr'
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
db = SQLAlchemy(app)

# Function to fetch and write schema
def write_schema_to_file():
    # Create a database engine
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    
    # Reflect the database schema
    metadata = MetaData()
    metadata.reflect(bind=engine)
    
    # Write schema to a text file
    with open('database_schema.txt', 'w') as file:
        for table in metadata.sorted_tables:
            file.write(f"Table: rawdata\n")
            for column in table.columns:
                file.write(f"  Column: {column.name} - Type: {column.type}\n")
            file.write("\n")

# Run the function to write schema
with app.app_context():
    write_schema_to_file()
