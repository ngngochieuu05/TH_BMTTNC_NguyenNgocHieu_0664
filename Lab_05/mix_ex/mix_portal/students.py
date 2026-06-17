import json
from pathlib import Path

from .basics import build_student


class StudentStore:
    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self.path.write_text("[]", encoding="utf-8")

    def _load(self):
        return json.loads(self.path.read_text(encoding="utf-8"))

    def _save(self, students):
        self.path.write_text(json.dumps(students, ensure_ascii=True, indent=2), encoding="utf-8")

    def list_students(self):
        return self._load()

    def create_student(self, name: str, sex: str, major: str, diem_tb: float):
        students = self._load()
        next_id = max((student["student_id"] for student in students), default=0) + 1
        student = build_student(next_id, name, sex, major, diem_tb)
        students.append(student)
        self._save(students)
        return student

    def update_student(self, student_id: int, name: str, sex: str, major: str, diem_tb: float):
        students = self._load()
        for index, student in enumerate(students):
            if student["student_id"] == student_id:
                updated = build_student(student_id, name, sex, major, diem_tb)
                students[index] = updated
                self._save(students)
                return updated
        raise KeyError("Student not found")

    def delete_student(self, student_id: int):
        students = self._load()
        remaining = [student for student in students if student["student_id"] != student_id]
        if len(remaining) == len(students):
            raise KeyError("Student not found")
        self._save(remaining)

    def search_by_name(self, keyword: str):
        keyword_upper = keyword.upper()
        return [student for student in self._load() if keyword_upper in student["name"].upper()]

    def sort_by_name(self):
        return sorted(self._load(), key=lambda student: student["name"])

    def sort_by_diem_tb(self):
        return sorted(self._load(), key=lambda student: student["diem_tb"], reverse=True)
