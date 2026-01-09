from flask import Flask
from app.config import Config
import torch
import os

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Import routes after app is created to avoid circular imports
from app import routes
