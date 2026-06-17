from dataclasses import asdict, dataclass


@dataclass
class Student:
    student_id: int
    name: str
    sex: str
    major: str
    diem_tb: float
    hoc_luc: str


def greeting(name: str, age: int) -> str:
    return f"Xin chào {name}, bạn {age} tuổi"


def circle_area(radius: float) -> float:
    return round(3.14 * radius * radius, 2)


def parity(number: int) -> str:
    return "chẵn" if number % 2 == 0 else "lẻ"


def even_sum(values):
    return sum(value for value in values if value % 2 == 0)


def reverse_text(text: str) -> str:
    return text[::-1]


def to_tuple(values):
    return tuple(values)


def classify_hoc_luc(diem_tb: float) -> str:
    if diem_tb >= 9:
        return "Xuất sắc"
    if diem_tb >= 8:
        return "Giỏi"
    if diem_tb >= 7:
        return "Khá"
    if diem_tb >= 5:
        return "Trung bình"
    return "Yếu"


def build_student(student_id: int, name: str, sex: str, major: str, diem_tb: float) -> dict:
    student = Student(
        student_id=student_id,
        name=name,
        sex=sex,
        major=major,
        diem_tb=diem_tb,
        hoc_luc=classify_hoc_luc(diem_tb),
    )
    return asdict(student)
