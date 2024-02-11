#!/usr/bin/python3

"""
Initialize the package to generate a distinct FileStorage instance tailored for the application's needs.
"""
from models.engine.file_storage import FileStorage

# Create a FileStorage instance
storage = FileStorage()
# Reload data
storage.reload()

