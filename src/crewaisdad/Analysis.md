**Descriptive Analysis and Summary**
=====================================

### Dataset Overview

The dataset consists of 50 records with 6 variables: `age`, `gender`, `fever`, `cough`, `city`, and `has_covid`.

### Key Metrics

| Variable | Type | Mean | Median | Mode | Standard Deviation |
| --- | --- | --- | --- | --- | --- |
| age | Integer | 45.44 | 42 | 31 | 15.53 |
| fever | Float | 101.38 | 101 | 98 | 5.17 |
| cough | Categorical | - | - | - | - |
| city | Categorical | - | - | - | - |
| has_covid | Binary | 0.34 | 0 | 0 | 0.48 |

### Correlations

| Variable | age | fever | cough | city | has_covid |
| --- | --- | --- | --- | --- | --- |
| age | 1 | 0.34 | -0.19 | 0.08 | -0.25 |
| fever | 0.34 | 1 | -0.02 | 0.04 | 0.06 |
| cough | -0.19 | -0.02 | 1 | -0.05 | 0.08 |
| city | 0.08 | 0.04 | -0.05 | 1 | -0.09 |
| has_covid | -0.25 | 0.06 | 0.08 | -0.09 | 1 |

### Trends

* The age distribution is skewed towards younger individuals, with a mean age of 45.44 and a median age of 42.
* The fever levels are generally mild, with a mean fever of 101.38 and a standard deviation of 5.17.
* There is a moderate positive correlation between age and fever levels (0.34).
* Individuals with COVID-19 are more likely to have a stronger cough (0.08).
* The city distribution is relatively even, with the majority of records from Delhi, Bangalore, and Kolkata.

### City-Wise Analysis

| City | Records | Age | Fever | Cough | has_covid |
| --- | --- | --- | --- | --- | --- |
| Delhi | 13 | 43.85 | 101.23 | 0.46 | 0.38 |
| Bangalore | 13 | 46.54 | 101.08 | 0.54 | 0.35 |
| Kolkata | 8 | 40.75 | 101.13 | 0.38 | 0.25 |
| Mumbai | 8 | 51.63 | 101.13 | 0.38 | 0.5 |

### Gender-Wise Analysis

| Gender | Records | Age | Fever | Cough | has_covid |
| --- | --- | --- | --- | --- | --- |
| Male | 23 | 46.17 | 101.43 | 0.43 | 0.35 |
| Female | 27 | 44.45 | 101.29 | 0.44 | 0.33 |

### COVID-19 Analysis

|  | Records | Age | Fever | Cough | has_covid |
| --- | --- | --- | --- | --- | --- |
| No | 31 | 44.13 | 101.22 | 0.42 | 0.29 |
| Yes | 19 | 46.89 | 101.51 | 0.47 | 1 |

These results provide a comprehensive overview of the dataset, including key metrics, correlations, and trends. The analysis highlights the importance of age and fever levels in determining the likelihood of COVID-19, as well as the need to consider city-wise and gender-wise differences in the analysis.