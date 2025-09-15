def average(students_dict):
    total_score = sum(students_dict.values())
    number_of_students = len(students_dict)
    if number_of_students == 0:
        return 0
    return total_score / number_of_students

class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}
class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

print(f"Average for class 3B: {average(class_3B)}.")    
print(f"Average for class 3C: {average(class_3C)}.")