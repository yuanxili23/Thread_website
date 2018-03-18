import os
from website.lib.database_config import DatabaseConfig


# Statement for enabling the development environment
DEBUG = True

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

APPLICATION_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "website"))

HOST = '0.0.0.0'

PORT = 5000

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s/%s' % ('root', 'love0906',
                                                   'localhost', 'sys')

#########################


# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"
