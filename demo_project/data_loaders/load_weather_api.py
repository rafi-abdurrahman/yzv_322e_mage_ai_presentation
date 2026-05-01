import pandas as pd
import requests

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://api.open-meteo.com/v1/forecast?latitude=52.52,48.85,51.51&longitude=13.41,2.35,-0.13&current_weather=true'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # The API returns a list when multiple locations are requested
        if isinstance(data, list):
            weather_data = []
            cities = ['Berlin', 'Paris', 'London']
            for i, result in enumerate(data):
                current = result.get('current_weather', {})
                weather_data.append({
                    'city': cities[i],
                    'temperature': current.get('temperature'),
                    'windspeed': current.get('windspeed'),
                    'time': current.get('time')
                })
            return pd.DataFrame(weather_data)
        
    return pd.DataFrame()
