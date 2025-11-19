[Open-Meteo API]  --->  [Ingestion Producer (Python)]  --> Kafka (weather_raw)
                                    |
                                    v
                           [Consumer & Transformer] --> Kafka (weather_cleaned)
                                    |
                                    v
                                [DuckDB / Warehouse]
                                    |
             Airflow DAGs <-- [Batch Aggregations / DQ] --> Looker Studio via Google Sheets
                                    |
                                 FastAPI (serving)
