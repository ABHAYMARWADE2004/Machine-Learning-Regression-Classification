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
| KNN | Same pass/fail task | Accuracy 87%, precision 91%, recall 78% |
| Decision Tree | Same pass/fail task | Accuracy 78% (overfits when grown deep) |
| Random Forest | Same pass/fail task | Accuracy 87%, precision 95%, recall 74% |

**Model comparison** (5-fold cross-validation on all 300 students):

| Model | CV accuracy |
|-------|-------------|
| Random Forest | 84.7% |
| Logistic Regression | 84.0% |
| Naive Bayes | 83.7% |
| KNN (K=15) | 83.3% |
| SVM (RBF) | 83.3% |
| Decision Tree (depth 5) | 83.0% |

**What the results show:**
- A curve fits salary growth better than a straight line (R² 0.85 to 0.91).
- Adding education and skills improves the model further (R² 0.93), and each feature's contribution can be read from its coefficient.
- For KNN, feature scaling matters a lot: accuracy rose from 72% to 88% just by scaling.
- A single decision tree overfits when it grows deep, and a random forest of many trees fixes this (78% to 87%).
- All six classifiers land within about 2 points of each other, which is smaller than the fold-to-fold variation, so **no model is clearly best**. When models tie, the simpler one (logistic regression) is the better choice.
- Caveat: the pass/fail data was generated from a logistic formula, so logistic regression naturally fits it well. On real data the ranking could differ.

## Notebooks

| # | Notebook | Type | What it covers |
|---|----------|------|----------------|
| 1 | [Linear Regression](notebooks/regression/01_linear_regression_salary.ipynb) | Regression | Train/test split, coefficients, R², MAE, RMSE |
| 2 | [Multiple Regression](notebooks/regression/02_multiple_regression_salary.ipynb) | Regression | Correlation heatmap, several features, actual vs predicted |
| 3 | [Polynomial Regression](notebooks/regression/03_polynomial_regression_salary.ipynb) | Regression | Curved fits, choosing the degree, overfitting check |
| 4 | [Logistic Regression](notebooks/classification/01_logistic_regression_pass_fail.ipynb) | Classification | Sigmoid curve, confusion matrix, precision, recall, odds ratios |
| 5 | [KNN](notebooks/classification/02_knn_pass_fail.ipynb) | Classification | Feature scaling, choosing K with cross-validation |
| 6 | [Decision Tree](notebooks/classification/03_decision_tree_pass_fail.ipynb) | Classification | Reading a tree, overfitting, choosing the depth, feature importance |
| 7 | [Random Forest](notebooks/classification/04_random_forest_pass_fail.ipynb) | Classification | Ensembles, number of trees, forest vs single tree |
| 8 | [Model Comparison](notebooks/classification/05_model_comparison.ipynb) | Classification | Six models compared with cross-validation (incl. SVM and Naive Bayes) |

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
│       ├── 01_logistic_regression_pass_fail.ipynb
│       ├── 02_knn_pass_fail.ipynb
│       ├── 03_decision_tree_pass_fail.ipynb
│       ├── 04_random_forest_pass_fail.ipynb
│       └── 05_model_comparison.ipynb
├── requirements.txt
└── README.md
```

## Workflow in Every Notebook

**Load data → Explore → Split into train and test → Train → Evaluate → Visualize → Predict → Conclude**

## Tech Stack

Python · NumPy · Pandas · Matplotlib · Scikit-learn · Jupyter Notebook

## Skills Demonstrated

Supervised learning · Regression · Classification · Model evaluation (R², MAE, RMSE, confusion matrix, precision, recall) · Cross-validation · Hyperparameter selection · Ensemble methods · Overfitting checks · Data visualization

## Author

**Abhay Marwade**, Aspiring Data Analyst

[GitHub](https://github.com/ABHAYMARWADE2004)
