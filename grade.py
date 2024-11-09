
def calculate_grade(score):
    """
    Calculate grade based on score.

    Args:
        score (float): Average score.

    Returns:
        str: Grade (A, B, C, D, F).
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def student_grade_calculator():
    """
    Calculate student grade based on scores.
    """
    
    name = input("Enter student's name: ")

    
    num_subjects = int(input("Enter number of subjects: "))

    
    total_score = 0

    scores = []
    for i in range(num_subjects):
        score = float(input(f"Enter score for subject {i+1}: "))
        scores.append(score)
        total_score += score

    
    avg_score = total_score / num_subjects

    
    grade = calculate_grade(avg_score)

    
    print("\nStudent Grade Report:")
    print(f"Name: {name}")
    print(f"Scores: {scores}")
    print(f"Average Score: {avg_score:.2f}")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    student_grade_calculator()
