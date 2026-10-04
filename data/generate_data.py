"""
Generates the two synthetic datasets used in this repository.

Run:  python generate_data.py
Output: salary_data.csv, student_pass_fail.csv

Both datasets are SYNTHETIC (randomly generated with a fixed seed), made for
learning and demonstrating machine learning models. They are not real people.
"""
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
N = 300

# ---------------------------------------------------------------- salary data
years_experience = np.round(rng.uniform(0, 15, N), 1)
education_level  = rng.choice([1, 2, 3], size=N, p=[0.5, 0.35, 0.15])  # 1=Bachelor, 2=Master, 3=PhD
skills_score     = np.clip(np.round(rng.normal(60, 15, N)), 0, 100).astype(int)

salary = (
    250_000
    + 55_000 * years_experience
    - 1_500 * years_experience ** 2            # growth slows with experience (curved)
    + 60_000 * (education_level - 1)
    + 1_800 * skills_score
    + rng.normal(0, 30_000, N)                 # random noise
)
salary_df = pd.DataFrame({
    "years_experience": years_experience,
    "education_level": education_level,
    "skills_score": skills_score,
    "salary": np.round(salary, -2).astype(int),   # annual salary in INR, rounded to nearest 100
})
salary_df.to_csv("salary_data.csv", index=False)

# ---------------------------------------------------------- student pass/fail
study_hours    = np.round(rng.uniform(0, 10, N), 1)
attendance_pct = np.round(rng.uniform(50, 100, N)).astype(int)
previous_score = np.clip(np.round(rng.normal(60, 15, N)), 20, 100).astype(int)

z = 2.0 * (0.55 * (study_hours - 5) + 0.045 * (attendance_pct - 75) + 0.045 * (previous_score - 60))
prob_pass = 1 / (1 + np.exp(-z))
passed = (rng.random(N) < prob_pass).astype(int)

pd.DataFrame({
    "study_hours": study_hours,
    "attendance_pct": attendance_pct,
    "previous_score": previous_score,
    "passed": passed,
}).to_csv("student_pass_fail.csv", index=False)

print("Created salary_data.csv and student_pass_fail.csv")
