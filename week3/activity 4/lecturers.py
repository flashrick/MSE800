from database import Database


class Lecturers:
    """Table helper that builds and fills the lecturers table."""

    def __init__(self, db: Database) -> None:
        # Hold the database so the class can reuse the connection
        self.db = db

    def create_table(self) -> None:
        # Create the lecturers table which stores teacher details
        self.db.cursor().execute(
            """
            CREATE TABLE IF NOT EXISTS lecturers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                birth_date TEXT NOT NULL,
                gender TEXT NOT NULL
            )
            """
        )

    def add(self, name: str, birth_date: str, gender: str) -> int:
        # Insert one lecturer row and return the id
        cursor = self.db.cursor()
        cursor.execute(
            "INSERT INTO lecturers(name, birth_date, gender) VALUES (?, ?, ?)",
            (name, birth_date, gender),
        )
        self.db.commit()
        return cursor.lastrowid
