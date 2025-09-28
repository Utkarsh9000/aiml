# Employee Attrition Exploration – AIML Recruitment Task
# Author: Utkarsh

import os
import pandas as pd
import matplotlib.pyplot as plt

# Check if file exists
csv_path = "Employee_Performance_Retention.csv"
if not os.path.exists(csv_path):
    print(f"ERROR: File '{csv_path}' not found in {os.getcwd()}")
    exit(1)

# Load dataset
df = pd.read_csv(csv_path)

# Basic info
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Missing values:\n", df.isnull().sum())

# Target column analysis
if "Attrition" not in df.columns:
    print("ERROR: 'Attrition' column not found in the dataset.")
    exit(1)
print("Attrition counts:\n", df["Attrition"].value_counts())

# Group by Department
if "Department" in df.columns:
    dept_attrition = df.groupby("Department")["Attrition"].value_counts(normalize=True).unstack()
    print("Attrition rate by department:\n", dept_attrition)
else:
    print("WARNING: 'Department' column not found.")

# Experience vs Attrition
if "Experience" in df.columns:
    avg_exp_yes = df[df["Attrition"] == "Yes"]["Experience"].mean()
    avg_exp_no = df[df["Attrition"] == "No"]["Experience"].mean()
