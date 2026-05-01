import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.
    """
    # Create a new column with Temperature in Fahrenheit
    if not data.empty:
        data['temperature_fahrenheit'] = data['temperature'] * 9/5 + 32
        
        # Format the time column to a simple date string
        data['date'] = pd.to_datetime(data['time']).dt.strftime('%Y-%m-%d')
        
        # Select and reorder columns
        data = data[['city', 'date', 'temperature', 'temperature_fahrenheit', 'windspeed']]
        
    return data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    assert 'temperature_fahrenheit' in output.columns, 'Fahrenheit column is missing'
