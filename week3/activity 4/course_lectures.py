from database import Database


class CourseLectures:
    """Table helper for the link between courses and lecturers."""

    def __init__(self, db: Database) -> None:
        # Use the same connection that other table helpers rely on
        self.db = db

    def create_table(self) -> None:
        # Create the mapping table with a composite primary key
        self.db.cursor().execute(
            """
            CREATE TABLE IF NOT EXISTS course_lectures (
                course_id INTEGER NOT NULL,
                lecturer_id INTEGER NOT NULL,
                PRIMARY KEY (course_id, lecturer_id),
                FOREIGN KEY (course_id) REFERENCES courses(id),
                FOREIGN KEY (lecturer_id) REFERENCES lecturers(id)
            )
            """
        )

    def add(self, course_id: int, lecturer_id: int) -> None:
        # Link a lecturer to a course
        self.db.cursor().execute(
            "INSERT INTO course_lectures(course_id, lecturer_id) VALUES (?, ?)",
            (course_id, lecturer_id),
        )
        self.db.commit()

    def get_teacher_names_by_course(self, code: str) -> list[str]:
        # Return a list of lecturers teaching the given course code
        cursor = self.db.cursor()
        cursor.execute(
            """
            SELECT DISTINCT l.name
            FROM lecturers l
            JOIN course_lectures cl ON l.id = cl.lecturer_id
            JOIN courses c ON c.id = cl.course_id
            WHERE c.code = ?
            ORDER BY l.name
            """,
            (code,),
        )
        return [row[0] for row in cursor.fetchall()]
