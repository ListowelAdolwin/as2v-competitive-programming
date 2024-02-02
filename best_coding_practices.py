def assign_grade_letter(grade):
    """
    assigns the grade letter to student given the student's grade
    """

    if grade >= 90:
        l = 'A'
    elif grade >= 80:
        l = 'B'
    elif grade >= 70:
        l = 'C'
    elif grade >= 60:
        l = 'D'
    else:
        l = 'F'
    
    return l


def passed_all_grades(grades):
    """
    checks if student has passed all courses
    """

    for g in grades:
        if g < 60:
            return False
        
    return True


def process_student_d(grades):
    """
    process the grades of a student
    """

    total = sum(grades)
    avg = total / len(grades)

    l = assign_grade_letter(avg)
    
    passed = passed_all_grades(grades)
    
    sdt_data = {
        'average_grade': avg,
        'all_grades_pass': passed,
        'grade_letter': l
    }

    return sdt_data