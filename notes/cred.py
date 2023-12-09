import os

def databasessecreatsEnv():
    # Access environment variables
    db_host = os.environ.get('DB_HOST')
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')
    
    
    return db_user, db_password, db_host
