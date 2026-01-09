# Data models for the application

class PotholeData:
    """Model for pothole prediction data"""
    
    def __init__(self, latitude, longitude, image_path=None):
        self.latitude = latitude
        self.longitude = longitude
        self.image_path = image_path
    
    def to_dict(self):
        return {
            'latitude': self.latitude,
            'longitude': self.longitude,
            'image_path': self.image_path
        }
