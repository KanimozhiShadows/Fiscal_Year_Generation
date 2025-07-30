# Fiscal_Year_Generation
---

# 📅 Fiscal Calendar Generator

This Python script generates a comprehensive fiscal calendar starting from **February** (configurable via `fiscalyear.START_MONTH`) for any given year. The calendar includes details down to the day level, associating each fiscal day with fiscal months, weeks, quarters, and calendar equivalents.

## 🚀 Features

* Custom fiscal year start month (default: February)
* Generates:

  * Fiscal quarters (Q1–Q4)
  * Fiscal months (M1–M12)
  * Weeks (W1, W2, ...)
  * Daily breakdown with corresponding calendar date and day
* Outputs a tabular format for easy inspection
* Automatically aligns the calendar date from January 1st of the fiscal start year

## 📂 File Structure

* **Fiscal\_Year.py**
  Main script that:

  * Accepts fiscal year input
  * Builds the fiscal calendar with quarters, months, weeks, and days
  * Prints a detailed tabular summary

## 🛠️ Dependencies

Install the required Python libraries using pip:

```bash
pip install fiscalyear pandas
```

## 📌 Usage

Run the script in your terminal:

```bash
python Fiscal_Year.py
```

Enter a fiscal year (e.g., `2026`) when prompted.

### Sample Input

```
Enter the fiscal year you want to view (e.g., 2026): 2026
```

### Sample Output (shortened)

```
📅 Fiscal Calendar with Calendar Date (starting Jan 1) for 2026

Fiscal Yr  Quarter  Quarter Start   Quarter End     Month   Month Start     Month End       Week  Week Start      Week End        Day        Fiscal Date  Calendar Date   Cal Day   
FY2026     Q1       2025-02-01      2025-04-30      M1      2025-02-01      2025-02-28      W1    2025-02-01      2025-02-07      Saturday   2025-02-01    2025-01-01      Wednesday
...
```

## 📅 Fiscal Logic

* The fiscal year starts in February, e.g., FY2026 → starts Feb 1, 2025.
* Each fiscal month spans typical month boundaries.
* Weeks are aligned sequentially, not strictly ISO 8601 weeks.
* Each day in the fiscal year is mapped to a Gregorian calendar date starting from Jan 1 of the fiscal start year.

## 📤 Output Format

The table includes:

* Fiscal year, quarter, and month details
* Start and end dates of quarters/months/weeks
* Day name, fiscal date, and corresponding calendar date

## 📎 Notes

* Uses the `fiscalyear` library for accurate fiscal date calculations.
* Handles user input errors gracefully.

---
