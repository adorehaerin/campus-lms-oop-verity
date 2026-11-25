from datetime import datetime


class Portal:
    """LMS portal managing students, tasks, deadline-checked submissions, and grading."""

    def __init__(self, course_name: str):
        if not course_name or not course_name.strip():
            raise ValueError("Course name cannot be empty.")

        self.__course_name = course_name.strip()
        self.__students: dict[str, object] = {}
        self.__tasks: dict[str, object] = {}

    @property
    def course_name(self) -> str:
        return self.__course_name

    def register_student(self, student) -> None:
        student_id = getattr(student, "student_id", None)
        if not student_id:
            raise ValueError("Student must have a valid student_id.")
        self.__students[student_id] = student

    def get_student(self, student_id: str):
        return self.__students.get(student_id)

    def add_task(self, task) -> None:
        title = getattr(task, "title", None)
        if not title:
            raise ValueError("Task must have a valid title.")
        self.__tasks[title] = task

    def get_task(self, task_title: str):
        return self.__tasks.get(task_title)

    def submit_task(
        self,
        student_id: str,
        task_title: str,
        content: str,
        submitted_at: datetime | None = None,
    ) -> None:
        student = self.__students.get(student_id)
        if student is None:
            raise KeyError(f"Student '{student_id}' is not registered.")

        task = self.__tasks.get(task_title)
        if task is None:
            raise KeyError(f"Task '{task_title}' does not exist.")

        if hasattr(task, "validate_submission"):
            task.validate_submission(content, submitted_at=submitted_at)
        elif hasattr(task, "is_past_deadline") and task.is_past_deadline(submitted_at):
            raise PermissionError(f"Cannot submit '{task_title}': deadline has passed.")

        if hasattr(student, "record_submission"):
            student.record_submission(task_title, content)

    def assign_grade(self, student_id: str, task_title: str, score: float) -> None:
        student = self.__students.get(student_id)
        if student is None:
            raise KeyError(f"Student '{student_id}' is not registered.")

        task = self.__tasks.get(task_title)
        if task is None:
            raise KeyError(f"Task '{task_title}' does not exist.")

        max_points = getattr(task, "max_points", 100.0)
        if hasattr(student, "set_grade"):
            student.set_grade(task_title, score, max_points=max_points)