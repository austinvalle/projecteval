# Enable development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database
DB_USERNAME = 'evaldba'
DB_PASSWORD = 'hello911'
SQLALCHEMY_DATABASE_URI = 'postgresql://' + DB_USERNAME + ':' + DB_PASSWORD + '@localhost/evaldb'
DATABASE_CONNECT_OPTIONS = {}

# Application threads
THREADS_PER_PAGE = 2

# Enable protection against CSRF
CSRF_ENABLED = True

# Secret key for signing data
CSRF_SESSION_KEY = "skooma"

# Secret key for signing cookies
SECRET_KEY = "moonsugar"