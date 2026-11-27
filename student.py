class Student:
    """Student record with encapsulated submissions and grade validation."""

    def __init__(self, student_id: str, name: str):
        if not student_id or not student_id.strip():
            raise ValueError("Student ID cannot be empty.")
        if not name or not name.strip():
            raise ValueError("Student name cannot be empty.")

        self.__student_id = student_id.strip()
        self.__name = name.strip()
        self.__submissions: dict[str, str] = {}
        self.__grades: dict[str, float] = {}

    @property
    def student_id(self) -> str:
        return self.__student_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def submissions(self) -> dict[str, str]:
        return dict(self.__submissions)

    @property
    def grades(self) -> dict[str, float]:
        return dict(self.__grades)

    def record_submission(self, task_title: str, content: str) -> None:
        if not task_title or not task_title.strip():
            raise ValueError("Task title cannot be empty.")
        if not content or not content.strip():
            raise ValueError("Submission content cannot be empty.")

        self.__submissions[task_title.strip()] = content.strip()

    def set_grade(self, task_title: str, score: float, max_points: float = 100.0) -> None:
        clean_title = task_title.strip() if isinstance(task_title, str) else ""
        if not clean_title:
            raise ValueError("Task title cannot be empty.")
        if clean_title not in self.__submissions:
            raise ValueError(f"Cannot assign grade for '{clean_title}': no submission recorded.")
        if isinstance(score, bool) or not isinstance(score, (int, float)):
            raise TypeError("Score must be a valid number.")
        if isinstance(max_points, bool) or not isinstance(max_points, (int, float)) or max_points <= 0:
            raise ValueError("Max points must be greater than zero.")
        if score < 0 or score > max_points:
            raise ValueError(f"Score {score} must be between 0 and {max_points}.")

        self.__grades[clean_title] = float(score)

    def __str__(self) -> str:
        return f"Student({self.__student_id} - {self.__name})"