from collections import defaultdict

students = [
    {
        "name": "Rahul",
        "marks": {
            "Python": 88,
            "DBMS": 76,
            "Computer Networks": 91,
            "Operating Systems": 84
        }
    },
    {
        "name": "Ananya",
        "marks": {
            "Python": 95,
            "DBMS": 89,
            "Computer Networks": 93,
            "Operating Systems": 90
        }
    },
    {
        "name": "Karthik",
        "marks": {
            "Python": 72,
            "DBMS": 81,
            "Computer Networks": 68,
            "Operating Systems": 77
        }
    },
    {
        "name": "Sneha",
        "marks": {
            "Python": 91,
            "DBMS": 94,
            "Computer Networks": 87,
            "Operating Systems": 96
        }
    },
    {
        "name": "Arjun",
        "marks": {
            "Python": 79,
            "DBMS": 73,
            "Computer Networks": 85,
            "Operating Systems": 80
        }
    },
    {
        "name": "Priya",
        "marks": {
            "Python": 86,
            "DBMS": 92,
            "Computer Networks": 89,
            "Operating Systems": 88
        }
    }
]


def subject_wise_marks(students):
    marks_dict = {}
    for each in students:
        for key, value in each["marks"].items():
            if key not in marks_dict:
                marks_dict[key] = []

            marks_dict[key].append(value)
    return marks_dict


def calculate_average(marks):
    sum = 0
    count = 0
    for key, value in marks.items():
        sum += value
        count += 1
    return sum / count


subject_marks = subject_wise_marks(students)


students_data = []
for each in students:
    student_dict = {}
    subject_dict = {}
    student_dict["name"] = each["name"]
    student_dict["average"] = calculate_average(each["marks"])
    students_data.append(student_dict)


subject_data = {}
for key, value in subject_marks.items():
    subject_dict = {}
    sum_data = sum(value)
    leng = len(value)
    subject_dict["average"] = sum_data / leng
    subject_dict["max_score"] = max(value)
    subject_dict["min_score"] = min(value)
    subject_data[key] = subject_dict

top_scorer = students_data[0]
for student in students_data:
    if student["average"] > top_scorer["average"]:
        top_scorer = student

students_data.append({
    "subject_wise_marks": subject_data
})

students_data.append({
    "top_scorer": top_scorer
})

print(students_data)
