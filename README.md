# ClickHouse Connection Tester

This project tests the connection and basic functionality of a ClickHouse database server.

## Features

- Tests connection to ClickHouse server
- Performs simple query test
- Checks ClickHouse version
- Verifies database existence
- Tests table creation and deletion
- Supports command-line arguments for flexible usage

## Requirements

- clickhouse/clickhouse-server
- clickhouse-connect library


```bash
docker pull clickhouse/clickhouse-server
```

```bash
docker run -d -p 8123:8123 -p 9000:9000 -e CLICKHOUSE_PASSWORD={YOUR_PASSWORD} --name clickhouse-server --ulimit nofile=262144:262144 clickhouse/clickhouse-server
```

```bash
pip install clickhouse_connect
```

## Installation


### Options:

- `--host`: ClickHouse host (default: localhost)
- `--port`: ClickHouse HTTP port (default: 8123)
- `--username`: ClickHouse username (default: default)
- `--password`: ClickHouse password (default: empty)
- `--database`: ClickHouse database (default: default)
- `--verbose`: Enable verbose output

