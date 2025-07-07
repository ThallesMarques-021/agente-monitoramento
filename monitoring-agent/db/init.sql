CREATE TABLE network_monitor (
  id SERIAL PRIMARY KEY,
  host TEXT,
  latency FLOAT,
  load_time FLOAT,
  status_code INTEGER,
  packet_loss INTEGER,
  timestamp TIMESTAMP
);