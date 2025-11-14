# Real-Time Weather
Real-Time streaming ETL pipeline: Open-Meteo -> Kafka -> Python processors -> DuckDB -> Looker Studio.
See doc/ARCHITECTURE.md for the system diagram and project plan.

## Data Source
We use Open-Meteo (https://open-meteo.com/) — free, no API key required, supports current & forecast data and historical. We will poll the API and model responses as sensor events.

Example endpoint:
https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&current_weather=true

## Quickstart (dev)
1. python -m venv .venv
2. .venv\Scripts\activate
3. pip install -r requirements.txt

## Roadmap
- Day 2: Add Kafka in docker-compose, builde producer to push Open-Meteo messages.
- Day 3: ... etc.