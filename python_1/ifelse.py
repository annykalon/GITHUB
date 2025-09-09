"""
Student Score Analyzer
- Uses descriptive variable names
- Integrates multiple data types (str, float/int, bool)
- Includes decision-making structures (if/elif/else)
- Performs repeated tasks with loops (for and while)
- Modularized with reusable custom functions
- Iterates a list (sequence) and uses its elements
"""

from typing import List, Dict


def calculate_average_score(scores: List[float]) -> float:
    """Return the average of a list of numeric scores."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def determine_letter_grade(average_score: float) -> str:
    """Convert a numeric average into a letter grade."""
    if average_score >= 90:
        return "A"
    elif average_score >= 80:
        return "B"
    elif average_score >= 70:
        return "C"
    elif average_score >= 60:
        return "D"
    else:
        return "F"


def did_student_pass(letter_grade: str) -> bool:
    """Decide pass/fail based on letter grade (decision structure)."""
    # Consider C or higher as passing
    return letter_grade in {"A", "B", "C"}


def summarize_student(student_record: Dict) -> Dict:
    """
    Compute derived fields for a single student and return a summary.
    Demonstrates accessing list elements and using multiple data types.
    """
    average_score: float = calculate_average_score(student_record["scores"])
    letter_grade: str = determine_letter_grade(average_score)
    passed_course: bool = did_student_pass(letter_grade)

    return {
        "name": student_record["name"],               # str
        "scores": student_record["scores"],           # list of floats/ints
        "average_score": round(average_score, 2),     # float (rounded)
        "letter_grade": letter_grade,                 # str
        "passed_course": passed_course,               # bool
        "num_assignments": len(student_record["scores"])  # int
    }


def main() -> None:
    """
    Main workflow:
    - Prepare a list (sequence) of student records
    - Iterate the list and compute summaries (repeated tasks via loops)
    - Make decisions per student (if/elif/else inside helper functions)
    - Print a clear report
    """

    # --- Sample data (three distinct data types present) ---
    # name: str, scores: list of float/int, bonus_points_enabled: bool (used below)
    student_records: List[Dict] = [
        {"name": "Avery Chen", "scores": [88, 92, 79, 95], "bonus_points_enabled": True},
        {"name": "Diego Morales", "scores": [72, 68, 74], "bonus_points_enabled": False},
        {"name": "Fatima Khalid", "scores": [99, 100, 97, 98], "bonus_points_enabled": True},
        {"name": "Nora Patel", "scores": [55, 61, 59], "bonus_points_enabled": False},
    ]

    # --- Optional: perform a repeated task via a while loop ---
    # Here we simulate a “bonus pass” that adds 2 points to each score for students
    # with bonus_points_enabled == True. This shows a loop handling repetitive tasks.
    apply_bonus_pass: bool = True
    while apply_bonus_pass:
        for student_record in student_records:
            if student_record["bonus_points_enabled"]:
                # Mutate the scores list (sequence) item-by-item (iterated list usage)
                updated_scores: List[float] = []
                for original_score in student_record["scores"]:
                    updated_scores.append(min(original_score + 2, 100))  # cap at 100
                student_record["scores"] = updated_scores
        # Exit after one pass; toggle to False so we don't loop forever.
        apply_bonus_pass = False

    # --- Process each student (for-loop over the list) ---
    student_summaries: List[Dict] = []
    for student_record in student_records:
        summary: Dict = summarize_student(student_record)
        student_summaries.append(summary)

    # --- Output a simple report with decision-based messaging ---
    print("=== Student Score Report ===")
    for summary in student_summaries:
        status_message: str = (
            f"✅ PASSED ({summary['letter_grade']})"
            if summary["passed_course"]
            else f"❌ FAILED ({summary['letter_grade']})"
        )

        print(
            f"\nName: {summary['name']}\n"
            f"Assignments: {summary['num_assignments']}\n"
            f"Scores: {summary['scores']}\n"
            f"Average: {summary['average_score']}\n"
            f"Result: {status_message}"
        )

    # --- Aggregate stats (extra use of loops/decisions) ---
    overall_average: float = calculate_average_score(
        [s["average_score"] for s in student_summaries]
    )
    passing_count: int = sum(1 for s in student_summaries if s["passed_course"])
    total_students: int = len(student_summaries)

    print("\n=== Class Summary ===")
    print(f"Class Average: {round(overall_average, 2)}")
    print(f"Passing: {passing_count}/{total_students}")


if __name__ == "__main__":
    main()