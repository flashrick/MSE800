from pathlib import Path
from database import Database
from programs import Programs
from courses import Courses
from students import Students
from lecturers import Lecturers
from course_lectures import CourseLectures


if __name__ == "__main__":
    db_file = Path("school.db")
    # Check if the database already exists on disk
    db_exists = db_file.exists()

    db = Database(str(db_file))
    programs = Programs(db)
    courses = Courses(db)
    students = Students(db)
    lecturers = Lecturers(db)
    course_lectures = CourseLectures(db)

    if not db_exists:
        # First run: create all tables and insert the base data
        programs.create_table()
        courses.create_table()
        students.create_table()
        lecturers.create_table()
        course_lectures.create_table()
        db.commit()

        # Add the Master of Software Engineering program
        mse_program_id = programs.add(
            "Master of Software Engineering", 2025, "2025-11-17", "2026-11-15"
        )

        # Add the two software courses that belong to the program
        mse800_id = courses.add(
            mse_program_id,
            "Professional Software Engineering",
            "2025-11-17",
            "2026-03-01",
            "MSE800",
        )
        mse801_id = courses.add(
            mse_program_id, 
            "Research Methods", 
            "2025-11-17", 
            "2026-03-01", 
            "MSE801"
        )

        # Add a few students who are inside the program
        students.add("Tom", "1999-07-14", "Female", mse_program_id)
        students.add("Peter", "1998-05-02", "Male", mse_program_id)

        # Add lecturers that teach the MSE801 course
        nvidia_id = lecturers.add("Nvidia", "1983-10-04", "Female")
        amd_id = lecturers.add("AMD", "1988-06-21", "Male")
        course_lectures.add(mse801_id, nvidia_id)
        course_lectures.add(mse801_id, amd_id)

    # Show the number of students for the MSE800 course
    mse800_count = students.count_by_course_code("MSE800")
    print(f"Number of students taking MSE800: {mse800_count}")

    # Show the list of lecturer names for the MSE801 course
    teacher_names = course_lectures.get_teacher_names_by_course("MSE801")
    print("Teachers for MSE801:")
    for name in teacher_names:
        print(f" - {name}")

    db.close()
