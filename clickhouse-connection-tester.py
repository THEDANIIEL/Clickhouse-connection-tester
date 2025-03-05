import argparse
from clickhouse_connect import get_client
from clickhouse_connect.driver.exceptions import ClickHouseError

def test_clickhouse_connection(host, port, username, password, database, verbose=False):
    try:
        client = get_client(host=host, port=port, username=username, password=password, database=database)
        
        result = client.query('SELECT 1').result_rows
        if verbose:
            print("Test 1 (Simple query) passed. Result:", result)

        version = client.query('SELECT version()').result_rows
        if verbose:
            print("Test 2 (System query) passed. ClickHouse version:", version[0][0])

        databases = client.query('SHOW DATABASES').result_rows
        if database in [db[0] for db in databases]:
            if verbose:
                print(f"Test 3 (Database existence) passed. Database '{database}' exists.")
        else:
            raise Exception(f"Database '{database}' does not exist.")

        client.query('CREATE TABLE IF NOT EXISTS test_table (id UInt32, name String) ENGINE = Memory')
        if verbose:
            print("Test 4 (Table creation) passed.")
        
        client.query('DROP TABLE IF EXISTS test_table')
        if verbose:
            print("Test 4 (Table deletion) passed.")

        print("All tests passed. ClickHouse is up and running.")
    except ClickHouseError as e:
        print("Failed to connect to ClickHouse:", e)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test ClickHouse connection and functionality")
    parser.add_argument("--host", default="localhost", help="ClickHouse host")
    parser.add_argument("--port", type=int, default=8123, help="ClickHouse HTTP port")
    parser.add_argument("--username", default="default", help="ClickHouse username")
    parser.add_argument("--password", default="pass", help="ClickHouse password")
    parser.add_argument("--database", default="default", help="ClickHouse database")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

    args = parser.parse_args()

    test_clickhouse_connection(args.host, args.port, args.username, args.password, args.database, args.verbose)
