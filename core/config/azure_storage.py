from core.env import config


DEFAULT_FILE_STORAGE = "storages.backends.azure_storage.AzureStorage"
STATICFILES_STORAGE = "storages.backends.azure_storage.AzureStorage"
AZURE_CONTAINER = config("AZURE_CONTAINER")
AZURE_ACCOUNT_NAME = config("AZURE_ACCOUNT_NAME")
AZURE_ACCOUNT_KEY = config("AZURE_ACCOUNT_KEY")
