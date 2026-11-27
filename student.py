class StudentProfile:
    """Student profile with encapsulated score tracking and validation."""

    def __init__(self, student_name: str, student_id: str):
        if not student_name or not student_name.strip():
            raise ValueError("Student name cannot be empty.")
        if not student_id or not student_id.strip():
            raise ValueError("Student ID cannot be empty.")

        self.student_name = student_name.strip()
        self.student_id = student_id.strip()
        self.__total_score: float = 0.0

    def add_points(self, points_earned: float, max_allowed: float | None = None) -> None:
        if isinstance(points_earned, bool) or not isinstance(points_earned, (int, float)):
            raise TypeError("Points earned must be a valid number.")
        if points_earned < 0:
            raise ValueError("Cannot add negative points!")
        if max_allowed is not None and (self.__total_score + points_earned) > max_allowed:
            raise ValueError(
                f"Cannot exceed maximum allowed points ({max_allowed})."
            )

        self.__total_score += float(points_earned)

    def get_current_score(self) -> float:
        return self.__total_score

    def __str__(self) -> str:
        return f"StudentProfile({self.student_id} - {self.student_name}: {self.__total_score:g} pts)"

from student import StudentProfile

student = StudentProfile("Member B", "2026-002")
student.add_points(40, max_allowed=100)
print(student)

try:
    student.add_points(-5, max_allowed=100)
except ValueError as e:
    print("Blocked negative points:", e)

try:
    student.add_points(70, max_allowed=100)
except ValueError as e:
    print("Blocked over-limit points:", e) 