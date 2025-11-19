import duckdb
from pathlib import Path

DB_PATH = Path("data/realtime.duckdb")

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS weather_clean (
    event_id TEXT PRIMARY KEY,
    sensor_id TEXT,
    timestamp TIMESTAMP,
    temperature_c DOUBLE,
    humidity DOUBLE,
    wind_speed_ms DOUBLE,
    wind_direction_deg DOUBLE,
    weather_code INTEGER,
    source TEXT,
    lat DOUBLE,
    lon DOUBLE,
    dew_point_c DOUBLE,
    ingested_at TIMESTAMP
);
"""

def init_db(db_path: str = str(DB_PATH)):
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = duckdb.connect(db_path)
    conn.execute(CREATE_TABLE_SQL)
    conn.close()
    print(f"DuckDB initialized at {db_path}")
    
if __name__ == "__main__":
    init_db()