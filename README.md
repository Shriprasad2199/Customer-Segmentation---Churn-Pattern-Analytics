# Customer Segmentation & Churn Pattern Analytics in European Banking

## Project Overview

Customer churn is a major challenge for retail banking, as customer loss can reduce customer lifetime value, increase acquisition costs and create financial and operational uncertainty.

This project analyses customer churn patterns across a European banking customer dataset of 10,000 customers. The analysis focuses on identifying high-risk customer segments, comparing churn across geographic and demographic groups, understanding engagement and tenure patterns, and assessing the financial characteristics of churned customers.

The project combines descriptive data analytics, customer segmentation, financial exposure analysis and an interactive Streamlit dashboard to provide evidence-based insights for banking and public-sector stakeholders.

---

## Project Objectives

### Primary Objectives

- Measure the overall customer churn rate.
- Identify churn distribution across different customer segments.
- Compare customer churn behaviour across European regions.

### Secondary Objectives

- Understand churn among high-value customers.
- Evaluate engagement and tenure patterns associated with churn.
- Examine the financial exposure associated with customer churn.
- Support strategic planning and targeted customer retention decisions.

---

## Dataset

The project uses a European banking customer dataset containing **10,000 customer records**.

### Main Variables

| Category | Variables |
|---|---|
| Customer | CustomerId |
| Demographic | Geography, Gender, Age |
| Financial | CreditScore, Balance, EstimatedSalary |
| Relationship | Tenure, NumOfProducts |
| Engagement | HasCrCard, IsActiveMember |
| Target | Exited |

`Exited` represents customer churn:

- `0` = Retained
- `1` = Churned

The `Surname` field was removed because it does not provide analytical value for customer segmentation or churn analysis.

---

## Methodology

The project follows a structured analytical workflow:

### 1. Data Ingestion and Validation

- Load the banking customer dataset.
- Validate engagement and product fields.
- Check binary variables for consistency.
- Validate the churn label.

### 2. Data Cleaning & Preparation

- Remove non-analytical fields.
- Validate categorical variables.
- Create derived customer segmentation fields.

### 3. Customer Segmentation

Customers were segmented across five major dimensions.

#### Geography

- France
- Germany
- Spain

#### Age

- Under 30
- 30–45
- 46–60
- 60+

#### Credit Score

- Low: <580
- Medium: 580–669
- High: ≥670

#### Tenure

- New: 0–3 years
- Mid-term: 4–7 years
- Long-term: 8–10 years

#### Balance

- Zero Balance: 0
- Low Balance: >0 and <100,000
- High Balance: ≥100,000

---

## Key Findings

### Overall Churn

- **Total customers:** 10,000
- **Churned customers:** 2,037
- **Retained customers:** 7,963
- **Overall churn rate:** **20.37%**

### Geographic Churn

Germany recorded the highest churn rate:

| Geography | Churn Rate |
|---|---:|
| Germany | **32.44%** |
| Spain | 16.67% |
| France | 16.15% |

### Age-Based Churn

Customers aged 46–60 showed the highest churn rate:

| Age Segment | Churn Rate |
|---|---:|
| Under 30 | 7.56% |
| 30–45 | 15.30% |
| 46–60 | **51.12%** |
| 60+ | 24.78% |

### Geography × Age

The strongest combined churn pattern was observed among:

**Germany + 46–60 years = 67.33% churn rate**

This demonstrates why analysing interactions between customer characteristics can reveal patterns that may be hidden when variables are considered individually.

### Gender

- Female churn rate: **25.07%**
- Male churn rate: **16.46%**

The difference represents an observed association and should not be interpreted as evidence of causation.

### Customer Engagement

Inactive customers represented **63.92% of churners**, compared with 44.54% of retained customers.

This indicates that engagement is an important dimension for understanding the composition of churned customers.

### Tenure

Tenure showed comparatively limited variation:

- New: 21.14%
- Mid-term: 19.64%
- Long-term: 20.45%

This suggests that tenure alone was a relatively weak differentiator of churn in this dataset.

---

## High-Value Customer Analysis

High-balance customers were examined as a proxy for higher-value customers.

### Key Findings

- **1,211 high-balance customers churned**
- High-balance churn rate: **25.23%**
- Balance associated with all churned customers: **185,588,094.63**
- High-balance churn exposure: **159,489,691.00**
- High-balance share of churned balance exposure: **85.94%**

The balance figures represent **financial exposure associated with churn**, rather than actual lost revenue or profit.

### Salary vs Balance

Among high-balance churners, the Pearson correlation between salary and balance was:

**r = 0.0123**

This indicates an essentially negligible linear relationship between salary and balance within this group.

---

## Business & Policy Implications

The analysis highlights several areas for further investigation:

1. **Geographic monitoring**  
   Germany demonstrates substantially higher observed churn than France and Spain.

2. **Age-specific retention analysis**  
   Customers aged 46–60 represent a particularly important segment for further investigation.

3. **Engagement monitoring**  
   Customer inactivity is disproportionately represented among churners.

4. **High-balance customer monitoring**  
   A large proportion of churn-associated balance exposure comes from high-balance customers.

5. **Segment-level analysis**  
   Aggregate churn rates can hide substantial differences between customer groups.

6. **Responsible use of customer analytics**  
   Segment-level findings should support investigation and service improvement rather than automatic decisions about individual customers.

---

## Streamlit Dashboard

An interactive Streamlit dashboard was developed to allow users to explore customer churn across different segments.

### Dashboard Filters

Users can filter customers by:

- Geography
- Age Segment
- Credit Score Segment
- Tenure Segment
- Balance Segment

### Dashboard Views

The dashboard includes:

- Overall Churn Rate
- Segment Churn Rate
- Geographic Risk Index
- Customer Summary
- Engagement & Churn
- Geography-wise Churn
- Age-wise Churn
- Tenure-wise Churn
- High-Value Customer Churn Explorer
- Salary vs Balance Analysis
- Balance Exposure Associated with Churn

---

## Project Structure

```text
Customer Segmentation & Churn Pattern/
│
├── app/
│   └── streamlit_app.py
│
├── data/
│   └── raw/
│       └── European_Bank.csv
│
├── notebooks/
│   └── 01_data_inspection.ipynb
│
├── outputs/
│   ├── charts/
│   └── tables/
│
├── src/
│
├── .gitignore
├── README.md
├── requirements.txt
├── Research_Paper_Customer_Segment_&_Churn_pattern_Analytics.pdf
└── Executive Summary.pdf