# Care Transition Efficiency & Placement Outcome Analytics

## Project Overview

This project analyzes the efficiency of the Unaccompanied Alien Children (UAC) care pipeline using data from the U.S. Department of Health and Human Services (HHS).

The analysis focuses on how children move through the care process:

**CBP Custody → HHS Care → Sponsor Placement**

The goal is to identify bottlenecks, evaluate transfer and discharge efficiency, and provide insights that can help improve reunification timelines and child welfare outcomes.

---

## Problem Statement

While aggregate counts of children in custody are monitored, process efficiency metrics are often missing. This project answers key questions such as:

* How efficiently are children transferred from CBP to HHS?
* Are discharges keeping pace with inflows?
* Where do care backlogs accumulate?
* Are placement outcomes improving over time?

---

## Dataset Information

**Dataset Name:**
HHS Unaccompanied Alien Children Program Dataset

### Dataset Columns

| Column                                         | Description          |
| ---------------------------------------------- | -------------------- |
| Date                                           | Reporting date       |
| Children apprehended and placed in CBP custody | Daily intake volume  |
| Children in CBP custody                        | Active CBP care load |
| Children transferred out of CBP custody        | Flow into HHS system |
| Children in HHS Care                           | Active HHS care load |
| Children discharged from HHS Care              | Sponsor placements   |

---

## Key Performance Indicators (KPIs)

### Transfer Efficiency Ratio

Measures the efficiency of transfers from CBP custody to HHS care.

### Discharge Effectiveness Index

Measures how effectively children are discharged from HHS care to sponsors.

### Pipeline Throughput Rate

Evaluates overall movement through the care pipeline.

### Backlog Accumulation Rate

Identifies delays and unresolved cases.

### Outcome Stability Score

Measures consistency of placement outcomes over time.

---

## Features

* Data Cleaning and Validation
* KPI Calculation
* Interactive Streamlit Dashboard
* Dataset Preview
* Trend Analysis
* Bottleneck Detection
* Outcome Stability Monitoring
* Visual Analytics using Plotly and Matplotlib

---

## Technologies Used

* Python
* Pandas
* NumPy
* Streamlit
* Matplotlib
* Seaborn
* Plotly
* Git & GitHub

---

## Dashboard Screenshots

### Main Dashboard

(Add screenshot here)

### KPI Analysis

(Add screenshot here)

### Trend Analysis

(Add screenshot here)

---

## How to Run the Project

### Clone Repository

```bash
git clone https://github.com/mrudulahub17/care-transition-analytics.git
```

### Open Project Folder

```bash
cd care-transition-analytics
```

### Create Virtual Environment

```bash
python3 -m venv venv
```

### Activate Virtual Environment

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit Application

```bash
streamlit run app.py
```

---

## Project Outcomes

* Identified transfer and discharge trends.
* Evaluated care pipeline efficiency.
* Highlighted potential bottlenecks in the process.
* Provided actionable insights for improving reunification outcomes.

---

## Author

**Mandali Mrudula Sai**

GitHub: https://github.com/mrudulahub17
