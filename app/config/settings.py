# Non-sensitive settings
from typing import List

# Required Environment Variables (app/config/.env file)
REQUIRED_ENV_VARS: List[str] = ['WEBEX_ADMIN_UID', 'CLIENT_ID', 'CLIENT_SECRET', 'SQLALCHEMY_DATABASE_URL']

# Required Settings
REQUIRED_SETTINGS: List[str] = ['LAT_MIN', 'LAT_MAX', 'LON_MIN', 'LON_MAX', 'GEOLOCATION_TIMEOUT']

# FastAPI Settings
APP_NAME: str = 'Webex Call Blocking by Geolocation'
APP_VERSION: str = 'POC v1.0'
UVICORN_LOG_LEVEL: str = 'WARNING'

# Webex Integration URLs
AUTHORIZATION_BASE_URL = 'https://api.ciscospark.com/v1/authorize'
TOKEN_URL = 'https://api.ciscospark.com/v1/access_token'
WEBEX_BASE_URL = 'https://webexapis.com/v1/'
SCOPE: List[str] = ['spark:all', 'spark-admin:xsi', 'spark:xsi', 'spark-admin:locations_read', 'spark-admin:people_read', 'spark-admin:licenses_read']
PUBLIC_URL: str = 'https://webexlab.techniclabs.app'

# Geolocation bounding boxes &
LAT_MIN: float = 3.166766
LAT_MAX: float = 8.620204
LON_MIN: float = -76.248241
LON_MAX: float = -70.051952
GEOLOCATION_TIMEOUT: int = 30

