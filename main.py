from datetime import datetime, timedelta

from base_task import AssignmentTask
from portal import Portal
from student import Student


def format_dt(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M")


def print_student_summary(student: Student) -> None:
    print(f"\n--- {student.name} ({student.student_id}) ---")
    if not student.submissions:
        print("  Submissions: None")
    else:
        for task_title, content in student.submissions.items():
            grade = student.grades.get(task_title)
            grade_text = f"{grade:g} pts" if grade is not None else "Ungraded"
            print(f"  - {task_title}: [{grade_text}] -> {content}")


def run_demo() -> None:
    portal = Portal("CS 102 - Object-Oriented Programming")
    print(f"=== {portal.course_name} ===\n")

    alice = Student("STU-001", "Alice Santos")
    bob = Student("STU-002", "Bob Reyes")
    portal.register_student(alice)
    portal.register_student(bob)
    print(f"Students registered : {alice.name}, {bob.name}")

    now = datetime.now()
    lab_task = AssignmentTask(
        title="OOP Lab 1: Classes & Encapsulation",
        deadline=now + timedelta(days=3),
        max_points=50.0,
    )
    quiz_task = AssignmentTask(
        title="Quiz 1: Inheritance Basics",
        deadline=now - timedelta(hours=2),
        max_points=20.0,
    )
    portal.add_task(lab_task)
    portal.add_task(quiz_task)
    print(
        f"Tasks added         : "
        f"{lab_task.title} (due {format_dt(lab_task.deadline)}, {lab_task.max_points:g} pts) | "
        f"{quiz_task.title} (due {format_dt(quiz_task.deadline)}, {quiz_task.max_points:g} pts)\n"
    )

    portal.submit_task(
        student_id="STU-001",
        task_title="OOP Lab 1: Classes & Encapsulation",
        content="class Book: pass",
        submitted_at=now,
    )
    portal.assign_grade("STU-001", "OOP Lab 1: Classes & Encapsulation", 47.5)

    checks = [
        (
            "Late Submission",
            lambda: portal.submit_task(
                student_id="STU-002",
                task_title="Quiz 1: Inheritance Basics",
                content="My late answer",
                submitted_at=now,
            ),
            (PermissionError, ValueError),
        ),
        (
            "Invalid Score",
            lambda: portal.assign_grade("STU-001", "OOP Lab 1: Classes & Encapsulation", 99.0),
            (ValueError, TypeError),
        ),
        (
            "Missing Submission",
            lambda: portal.assign_grade("STU-002", "OOP Lab 1: Classes & Encapsulation", 40.0),
            (ValueError,),
        ),
    ]

    for label, action, expected_exceptions in checks:
        try:
            action()
        except expected_exceptions as exc:
            print(f"[PASSED - {label}] {exc}")

    print_student_summary(alice)
    print_student_summary(bob)


if __name__ == "__main__":
    run_demo()