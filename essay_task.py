from base_task import AcademicTask


class Essay(AcademicTask):
    """Essay assignment subclass with word-count requirement and penalty grading."""

    def __init__(self, title: str, max_points: float, minimum_words: int):
        if isinstance(minimum_words, bool) or not isinstance(minimum_words, int) or minimum_words <= 0:
            raise ValueError("Minimum words must be a positive integer.")

        super().__init__(title, max_points)
        self.__minimum_words: int = minimum_words
        self.submitted_word_count: int = 0

    @property
    def minimum_words(self) -> int:
        return self.__minimum_words

    def submit_work(self, word_count: int) -> None:
        if isinstance(word_count, bool) or not isinstance(word_count, int) or word_count < 0:
            raise ValueError("Word count must be a non-negative integer.")

        self.submitted_word_count = word_count
        print(f"Essay submitted: {self.title}")

    def grade_work(self) -> float:
        self._is_graded = True
        if self.submitted_word_count >= self.__minimum_words:
            return float(self.max_points)
        return float(self.max_points - (self.max_points * 0.20))

    def get_details(self) -> None:
        print(
            f"[ESSAY] {self.title} - Max Points: {self.max_points} | "
            f"Minimum Words: {self.__minimum_words}"
        )