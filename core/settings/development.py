from core.env import config
from core.settings.base import *


DEBUG = config("DEBUG")
"""
Static files storage configuration for production.
"""
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
