from datetime import datetime, timedelta

from base_task import AssignmentTask
from portal import Portal
from student import Student


def run_demo() -> None:
    portal = Portal("CS 102 - Object-Oriented Programming")
    print(f"=== Initialized {portal.course_name} ===")

    alice = Student("STU-001", "Alice Santos")
    bob = Student("STU-002", "Bob Reyes")
    portal.register_student(alice)
    portal.register_student(bob)
    print(f"Registered: {alice}, {bob}")

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
    print(f"Added tasks: '{lab_task.title}' and '{quiz_task.title}'")

    portal.submit_task(
        student_id="STU-001",
        task_title="OOP Lab 1: Classes & Encapsulation",
        content="class Book: pass",
        submitted_at=now,
    )
    portal.assign_grade("STU-001", "OOP Lab 1: Classes & Encapsulation", 47.5)
    print(f"Alice submissions: {alice.submissions}")
    print(f"Alice grades: {alice.grades}")

    try:
        portal.submit_task(
            student_id="STU-002",
            task_title="Quiz 1: Inheritance Basics",
            content="My late answer",
            submitted_at=now,
        )
    except PermissionError as exc:
        print(f"[Expected Error - Late Submission]: {exc}")

    try:
        portal.assign_grade("STU-001", "OOP Lab 1: Classes & Encapsulation", 99.0)
    except ValueError as exc:
        print(f"[Expected Error - Invalid Score]: {exc}")

    try:
        portal.assign_grade("STU-002", "OOP Lab 1: Classes & Encapsulation", 40.0)
    except ValueError as exc:
        print(f"[Expected Error - Missing Submission]: {exc}")


if __name__ == "__main__":
    run_demo()