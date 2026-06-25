import sys

from analyzer import (
    read_submissions,
    get_submitted_students,
    calculate_average_score,
    get_domain_wise_average,
    get_missing_submissions,
    write_summary,
)


def main():
    try:
        input_file = sys.argv[1]
        output_file = sys.argv[2]

        data = read_submissions(input_file)

        submitted = get_submitted_students(data)

        highest = max(submitted, key=lambda x: x["score"])
        lowest = min(submitted, key=lambda x: x["score"])

        summary = {
            "total_students": len(data),
            "submitted_students": len(submitted),
            "missing_submissions": len(get_missing_submissions(data)),
            "average_score": calculate_average_score(data),
            "highest_scorer": highest["name"],
            "lowest_scorer": lowest["name"],
            "domain_wise_average": get_domain_wise_average(data),
            "students_not_submitted": get_missing_submissions(data),
            "students_below_5": [
                student["name"]
                for student in submitted
                if student["score"] < 5
            ],
        }

        print("===== Submission Summary =====")
        print("Total Students:", summary["total_students"])
        print("Submitted Students:", summary["submitted_students"])
        print("Missing Submissions:", summary["missing_submissions"])
        print("Average Score:", summary["average_score"])
        print("Highest Scorer:", summary["highest_scorer"])
        print("Lowest Scorer:", summary["lowest_scorer"])
        print("Students Not Submitted:", summary["students_not_submitted"])
        print("Students Below 5:", summary["students_below_5"])
        print("Domain-wise Average:", summary["domain_wise_average"])

        write_summary(summary, output_file)

        print("\nSummary written successfully!")

    except FileNotFoundError:
        print("Error: Input file not found.")

    except IndexError:
        print(
            "Usage: python main.py <input_csv> <output_json>"
        )

    except Exception as e:
        print("Unexpected Error:", e)


if __name__ == "__main__":
    main()