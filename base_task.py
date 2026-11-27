
from abc import ABC, abstractmethod


class AcademicTask(ABC):
    """Abstract base class for academic tasks."""

    def __init__(self, title: str, max_points: float):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Task title cannot be empty.")

        if not isinstance(max_points, (int, float)) or isinstance(max_points, bool):
            raise TypeError("Max points must be a number.")

        if max_points <= 0:
            raise ValueError("Max points must be greater than zero.")

        self.__title = title.strip()
        self.__max_points = float(max_points)
        self.__is_graded = False

    @property
    def title(self):
        return self.__title

    @property
    def max_points(self):
        return self.__max_points

    @property
    def is_graded(self):
        return self.__is_graded

    @abstractmethod
    def submit_work(self):
        """Submit academic work."""
        pass

    @abstractmethod
    def grade_work(self):
        """Grade submitted academic work."""
        pass

    @abstractmethod
    def get_details(self):
        """Return task details."""
        pass
