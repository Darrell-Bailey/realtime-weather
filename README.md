# Real-Time Weather

## Data Source
We use Open-Meteo (https://open-meteo.com/) — free, no API key required, supports current & forecast data and historical. We will poll the API and model responses as sensor events.

Example endpoint:
https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&current_weather=true

