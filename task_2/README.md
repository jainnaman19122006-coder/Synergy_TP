# Task 2: Student Submission Analyzer

## Description

This project analyzes student submission data stored in a CSV file.

It performs the following tasks:

- Reads submission data from a CSV file.
- Calculates average score.
- Finds highest and lowest scorers.
- Finds students who did not submit.
- Calculates domain-wise average scores.
- Generates a JSON summary report.

## Folder Structure

task_2/
├── data/
│   └── submissions.csv
├── output/
│   └── summary.json
├── src/
│   ├── analyzer.py
│   └── main.py
├── README.md
└── requirements.txt

## How to Run

```bash
python task_2/src/main.py task_2/data/submissions.csv task_2/output/summary.json
```

## Output

The program creates:

```
task_2/output/summary.json
```