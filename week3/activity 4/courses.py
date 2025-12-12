from database import Database


class Courses:
    """Table helper that builds and fills the courses table."""

    def __init__(self, db: Database) -> None:
        # Share the database reference with other table classes
        self.db = db

    def create_table(self) -> None:
        # Create the courses table so each course belongs to a program
        self.db.cursor().execute(
            """
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                program_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                start_date TEXT NOT NULL,
                end_date TEXT NOT NULL,
                code TEXT NOT NULL UNIQUE,
                FOREIGN KEY (program_id) REFERENCES programs(id)
            )
            """
        )

    def add(
        self,
        program_id: int,
        name: str,
        start_date: str,
        end_date: str,
        code: str,
    ) -> int:
        # Insert one course record and return its id
        cursor = self.db.cursor()
        cursor.execute(
            """
            INSERT INTO courses(program_id, name, start_date, end_date, code)
            VALUES (?, ?, ?, ?, ?)
            """,
            (program_id, name, start_date, end_date, code),
        )
        self.db.commit()
        return cursor.lastrowid

    def get_id_by_code(self, code: str) -> int:
        # Fetch the course id so other classes can build links
        cursor = self.db.cursor()
        cursor.execute("SELECT id FROM courses WHERE code = ?", (code,))
        row = cursor.fetchone()
        if row is None:
            raise ValueError("Course not found")
        return row[0]
