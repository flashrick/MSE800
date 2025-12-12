from database import Database


class Students:
    """Table helper that builds and fills the students table."""

    def __init__(self, db: Database) -> None:
        # Keep database connection ready for insert and query work
        self.db = db

    def create_table(self) -> None:
        # Create the students table with a link to programs
        self.db.cursor().execute(
            """
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                birth_date TEXT NOT NULL,
                gender TEXT NOT NULL,
                program_id INTEGER NOT NULL,
                FOREIGN KEY (program_id) REFERENCES programs(id)
            )
            """
        )

    def add(self, name: str, birth_date: str, gender: str, program_id: int) -> int:
        # Insert one student record and return the id
        cursor = self.db.cursor()
        cursor.execute(
            "INSERT INTO students(name, birth_date, gender, program_id) VALUES (?, ?, ?, ?)",
            (name, birth_date, gender, program_id),
        )
        self.db.commit()
        return cursor.lastrowid

    def count_by_course_code(self, code: str) -> int:
        # Count how many students belong to the program of the course
        cursor = self.db.cursor()
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM students s
            JOIN programs p ON s.program_id = p.id
            JOIN courses c ON c.program_id = p.id
            WHERE c.code = ?
            """,
            (code,),
        )
        (count,) = cursor.fetchone()
        return count
