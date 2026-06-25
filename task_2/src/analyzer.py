import csv
import json
import os
from typing import List, Dict


def read_submissions(file_path: str) -> List[Dict]:
    """
    Read submission data from CSV file.
    """
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        data = list(reader)

        # Convert score from string to integer
        for row in data:
            row["score"] = int(row["score"])

        return data


def get_submitted_students(data: List[Dict]) -> List[Dict]:
    """
    Return only students who submitted.
    """
    return [student for student in data if student["submitted"].lower() == "yes"]


def calculate_average_score(data: List[Dict]) -> float:
    """
    Calculate average score of submitted students.
    """
    submitted = get_submitted_students(data)

    if not submitted:
        return 0.0

    total = sum(student["score"] for student in submitted)
    return round(total / len(submitted), 2)


def get_domain_wise_average(data: List[Dict]) -> Dict:
    """
    Calculate average score for each domain.
    """
    domain_scores = {}

    for student in get_submitted_students(data):
        domain = student["domain"]

        if domain not in domain_scores:
            domain_scores[domain] = []

        domain_scores[domain].append(student["score"])

    averages = {}

    for domain, scores in domain_scores.items():
        averages[domain] = round(sum(scores) / len(scores), 2)

    return averages


def get_missing_submissions(data: List[Dict]) -> List[str]:
    """
    Return names of students who did not submit.
    """
    return [
        student["name"]
        for student in data
        if student["submitted"].lower() == "no"
    ]


def write_summary(summary: Dict, output_path: str) -> None:
    """
    Write summary dictionary to JSON file.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as file:
        json.dump(summary, file, indent=4)