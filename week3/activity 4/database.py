import sqlite3
from pathlib import Path


class Database:
    """Simple wrapper that handles the SQLite connection lifecycle."""

    def __init__(self, db_path: str) -> None:
        # Store the file path so it can be reused by other helpers
        self.db_path = Path(db_path)
        # Connect to the SQLite database file
        self.connection = sqlite3.connect(self.db_path)

    def cursor(self):
        # Return a cursor so callers can run SQL commands
        return self.connection.cursor()

    def commit(self) -> None:
        # Make sure all pending SQL statements are saved to disk
        self.connection.commit()

    def close(self) -> None:
        # Close the database connection when everything is done
        self.connection.close()
