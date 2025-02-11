import os

# Default to development configuration
env = os.environ.get("MATHOPT_ENV", "dev")

if env == "prod":
    from .prod import *
else:
    from .dev import * 


def get_api_endpoint():
    return API_ENDPOINT
