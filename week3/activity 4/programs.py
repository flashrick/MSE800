from database import Database


class Programs:
    """Table helper that builds and fills the programs table."""

    def __init__(self, db: Database) -> None:
        # Share the connection so we can run SQL commands
        self.db = db

    def create_table(self) -> None:
        # Build the programs table if it does not exist yet
        self.db.cursor().execute(
            """
            CREATE TABLE IF NOT EXISTS programs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                year INTEGER NOT NULL,
                start_date TEXT NOT NULL,
                end_date TEXT NOT NULL
            )
            """
        )

    def add(self, name: str, year: int, start_date: str, end_date: str) -> int:
        # Insert one program and return its database id
        cursor = self.db.cursor()
        cursor.execute(
            "INSERT INTO programs(name, year, start_date, end_date) VALUES (?, ?, ?, ?)",
            (name, year, start_date, end_date),
        )
        self.db.commit()
        return cursor.lastrowid

    def get_id_by_name(self, name: str) -> int:
        # Look up the id so other tables can point to the program
        cursor = self.db.cursor()
        cursor.execute("SELECT id FROM programs WHERE name = ?", (name,))
        row = cursor.fetchone()
        if row is None:
            raise ValueError("Program not found")
        return row[0]
