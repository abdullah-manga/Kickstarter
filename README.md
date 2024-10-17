# Kickstarter Projects Analysis

This project analyzes data from **Kickstarter**, a global crowdfunding platform. The analysis focuses on project success rates, funding goals, and backer contributions across different countries and categories using **Power BI** for data visualization.

---

## Project Overview

![Logo](./Images/Repo/Kickstarter-Logo-2009-2017.png)

Kickstarter is a crowdfunding platform for creative projects across categories like technology, art, and music. This analysis provides insights into project success rates, funding patterns, and backer behavior.

---

## Project Objectives

- **Analyze project success rates** by country, category, and backer range.
- **Understand funding dynamics**, including total goals vs. total pledged amounts.
- **Visualize** the success and failure trends of Kickstarter projects using **Power BI**.

---

## Tools & Technologies

- **Power BI**: Used for creating dashboards to analyze Kickstarter project data.

### Data Analysis Insights

#### Success & Fail Rate by Country

The success and failure rates of projects vary across countries. For example:
- **United States**: Highest success rate of 37.18%
- **Luxembourg**: Highest fail rate at 66.40%

#### Total Goals vs. Pledged USD by Country


This visualization compares total goals set by project creators with the actual amount pledged by backers in different countries, showcasing potential funding gaps.

#### Success & Fail Rate by Category


Categories like **Dance** and **Theater** exhibit the highest success rates (65.86% and 64.22%), while **Technology** and **Journalism** experience lower success rates (23.64% and 24.65%).

---

## Dashboard Features

### 1. **Projects By Country**

This dashboard provides an overview of all Kickstarter projects, including the number of successful, failed, live, and suspended projects.

![projects by country](./Images/Repo/Projects%20by%20country.png)

#### Key Visualizations

- **Success & Fail Rate by Country**: A comparison of project success rates across different countries.
- **Total Goals vs. Pledged**: A comparison of project goals and the total amount pledged by backers.

#### Filters

The dashboard includes the following filters:
   - **Country**
   - **Category**
   - **Launch Year**
   - **Project State** (successful, failed, live, etc.)

### 2. **Projects By Category**

This dashboard focuses on backer behavior and contribution trends.

![projects by country](./Images/Repo/Projects%20by%20categories.png)
#### Key Visualizations

- **Total Backers by Country**: Highlights the number of backers supporting projects in various countries.
- **Failed vs. Successful Projects by Backer Range**: A breakdown of project success based on the number of backers.

#### Filters

You can filter the data based on:
   - **Backer Range**: Filters projects based on the number of backers.
   - **Project State**: Focus on successful or failed projects.

---

## Conclusion

The analysis reveals key insights into Kickstarter project success:
- **Geographical Trends**: Countries like the United States and the United Kingdom have higher success rates, while Luxembourg and Mexico have lower success rates.
- **Category Performance**: Categories such as Dance and Theater are more successful, while Technology faces more challenges.
- **Backer Engagement**: Projects with more backers generally have higher success rates, though not all ranges exhibit linear success patterns.

---

## Important Note

> **Warning**: Some visualizations use a **logarithmic scale** due to the large variations in the dataset. This may affect how certain values appear in the graphs. To avoid any misinterpretation of the data, it is **recommended to hover over the visuals** to see the actual values and better understand the data distributions.

---

## How to Use

1. **Filter Data**: Use slicers to explore Kickstarter projects by category, country, and year.
2. **Interactive Visuals**: Click on charts and graphs to drill down into specific data.

---

## Installation and Setup

1. Download and install [Power BI Desktop](https://powerbi.microsoft.com/desktop/).
2. Open the provided `.pbix` file.
3. Refresh the data connections to load the latest Kickstarter data.
4. Explore the dashboards and apply filters to customize your analysis.
