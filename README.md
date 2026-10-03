# Machine Learning: Regression and Classification

A beginner-friendly collection of machine learning notebooks built with **Python and Scikit-learn**. Each notebook solves one prediction problem end to end: loading data, exploring it, training a model, evaluating it on unseen data and explaining the result.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?logo=scikitlearn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)

## Results

All scores are measured on **unseen test data** (80% train, 20% test, `random_state=42`).

| Notebook | Task | Test result |
|----------|------|-------------|
| Linear Regression | Salary from experience | R² 0.85, average error Rs. 49,731 |
| Polynomial Regression | Salary from experience (curved fit) | R² 0.91, average error Rs. 37,635 |
| Multiple Regression | Salary from experience, education, skills | R² 0.93, average error Rs. 34,269 |
| Logistic Regression | Pass or fail from study hours, attendance, previous score | Accuracy 88%, precision 100%, recall 74% |

**What the results show:**
- A curve fits salary growth better than a straight line (R² 0.85 to 0.91).
- Adding education and skills improves the model further (R² 0.93), and each feature's contribution can be read from its coefficient.
- The classification model never wrongly predicts a pass, but it misses about a quarter of the students who actually passed.

## Notebooks

| # | Notebook | Type | What it covers |
|---|----------|------|----------------|
| 1 | [Linear Regression](notebooks/regression/01_linear_regression_salary.ipynb) | Regression | Train/test split, coefficients, R², MAE, RMSE |
| 2 | [Multiple Regression](notebooks/regression/02_multiple_regression_salary.ipynb) | Regression | Correlation heatmap, several features, actual vs predicted |
| 3 | [Polynomial Regression](notebooks/regression/03_polynomial_regression_salary.ipynb) | Regression | Curved fits, choosing the degree, overfitting check |
| 4 | [Logistic Regression](notebooks/classification/01_logistic_regression_pass_fail.ipynb) | Classification | Sigmoid curve, confusion matrix, precision, recall, odds ratios |

## Datasets

Both datasets are **synthetic**: they were generated randomly with a fixed seed using [`data/generate_data.py`](data/generate_data.py) so the results are reproducible. They do not describe real people and are meant for learning.

**`data/salary_data.csv`** (300 rows)

| Column | Meaning |
|--------|---------|
| `years_experience` | Years of work experience (0 to 15) |
| `education_level` | 1 = Bachelor, 2 = Master, 3 = PhD |
| `skills_score` | Skills score (0 to 100) |
| `salary` | Annual salary in INR (target) |

**`data/student_pass_fail.csv`** (300 rows)

| Column | Meaning |
|--------|---------|
| `study_hours` | Daily study hours (0 to 10) |
| `attendance_pct` | Attendance percentage (50 to 100) |
| `previous_score` | Previous exam score (20 to 100) |
| `passed` | 1 = passed, 0 = failed (target) |

## Getting Started

```bash
git clone https://github.com/ABHAYMARWADE2004/Machine-Learning-Regression-Classification.git
cd Machine-Learning-Regression-Classification

pip install -r requirements.txt
jupyter notebook
```

Open any notebook from the `notebooks/` folder. They find the data in `data/` automatically.

## Project Structure

```
Machine-Learning-Regression-Classification/
├── data/
│   ├── salary_data.csv
│   ├── student_pass_fail.csv
│   └── generate_data.py
├── notebooks/
│   ├── regression/
│   │   ├── 01_linear_regression_salary.ipynb
│   │   ├── 02_multiple_regression_salary.ipynb
│   │   └── 03_polynomial_regression_salary.ipynb
│   └── classification/
│       └── 01_logistic_regression_pass_fail.ipynb
├── requirements.txt
└── README.md
```

## Workflow in Every Notebook

**Load data → Explore → Split into train and test → Train → Evaluate → Visualize → Predict → Conclude**

## Tech Stack

Python · NumPy · Pandas · Matplotlib · Scikit-learn · Jupyter Notebook

## Skills Demonstrated

Supervised learning · Regression · Classification · Model evaluation (R², MAE, RMSE, confusion matrix, precision, recall) · Overfitting checks · Data visualization

## Author

**Abhay Marwade**, Aspiring Data Analyst

[GitHub](https://github.com/ABHAYMARWADE2004)
