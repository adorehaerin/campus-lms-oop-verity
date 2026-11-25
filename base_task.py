from abc import ABC, abstractmethod
from datetime import datetime


class BaseTask(ABC):
    """Abstract base class for LMS tasks with encapsulated deadline rules."""

    def __init__(self, title: str, deadline: datetime, max_points: float = 100.0):
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty.")
        if not isinstance(deadline, datetime):
            raise TypeError("Deadline must be a datetime instance.")
        if max_points <= 0:
            raise ValueError("Max points must be greater than zero.")

        self.__title = title.strip()
        self.__deadline = deadline
        self.__max_points = float(max_points)

    @property
    def title(self) -> str:
        return self.__title

    @property
    def deadline(self) -> datetime:
        return self.__deadline

    @property
    def max_points(self) -> float:
        return self.__max_points

    def is_past_deadline(self, check_time: datetime | None = None) -> bool:
        current_time = check_time if check_time is not None else datetime.now()
        return current_time > self.__deadline

    @abstractmethod
    def validate_submission(self, content: str, submitted_at: datetime | None = None) -> None:
        """Validate whether a submission is allowed."""
        pass


class AssignmentTask(BaseTask):
    """Concrete task implementation enforcing deadline checks."""

    def validate_submission(self, content: str, submitted_at: datetime | None = None) -> None:
        if self.is_past_deadline(submitted_at):
            raise PermissionError(
                f"Submission rejected for '{self.title}': deadline ({self.deadline}) has passed."
            )
        if not content or not content.strip():
            raise ValueError("Submission content cannot be empty.")