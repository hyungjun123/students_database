from database import get_students

def show_average():
    students = get_students()
    avg = sum(s["score"] for s in students) / len(students)
    print(f"평균 점수 : {avg}")