import fiscalyear
from fiscalyear import FiscalYear, FiscalQuarter, FiscalMonth
from datetime import timedelta, date
import pandas as pd
import oracledb

# Set fiscal year to start in February
fiscalyear.START_MONTH = 2

def generate_fiscal_calendar(year):
    fiscal_year = FiscalYear(year)
    calendar = {
        "fiscal_year": fiscal_year.fiscal_year,
        "quarters": [],
        "months": [],
        "weeks": [],
        "days": []
    }

    # Generate quarters
    for q in range(1, 5):
        fq = FiscalQuarter(year, q)
        calendar["quarters"].append({
            "quarter": f"Q{q}",
            "start_date": fq.start.date(),
            "end_date": fq.end.date()
        })

    # Generate fiscal months, weeks, and days
    week_counter = 1
    for m in range(1, 13):
        fm = FiscalMonth(year, m)
        start_date = fm.start.date()
        end_date = fm.end.date()
        month_code = f"M{m}"
        quarter_index = (m - 1) // 3
        quarter = calendar["quarters"][quarter_index]

        current_date = start_date
        while current_date <= end_date:
            week_start = current_date
            week_end = min(week_start + timedelta(days=6), end_date)
            week_code = f"W{week_counter}"

            # Add days
            day_cursor = week_start
            while day_cursor <= week_end:
                calendar["days"].append({
                    "fiscal_year": f"FY{year}",
                    "quarter": quarter["quarter"],
                    "quarter_start": quarter["start_date"],
                    "quarter_end": quarter["end_date"],
                    "month": month_code,
                    "month_start": start_date,
                    "month_end": end_date,
                    "week": week_code,
                    "week_start": week_start,
                    "week_end": week_end,
                    "day": day_cursor.strftime("%A"),
                    "fiscal_date": day_cursor
                })
                day_cursor += timedelta(days=1)

            week_counter += 1
            current_date = week_end + timedelta(days=1)

    # Add calendar date column starting from Jan 1 of fiscal start year
    fiscal_start_year = fiscal_year.start.year
    calendar_start_date = date(fiscal_start_year, 1, 1)
    for i, day in enumerate(calendar["days"]):
        calendar_date = calendar_start_date + timedelta(days=i)
        day["calendar_date"] = calendar_date
        day["calendar_day"] = calendar_date.strftime('%A')

    return calendar

def print_fiscal_table(calendar):
    print(f"\n📅 Fiscal Calendar with Calendar Date (starting Jan 1) for {calendar['fiscal_year']}\n")
    print("{:<10} {:<8} {:<15} {:<15} {:<8} {:<15} {:<15} {:<6} {:<15} {:<15} {:<10} {:<12} {:<15} {:<10}".format(
        "Fiscal Yr", "Quarter", "Quarter Start", "Quarter End",
        "Month", "Month Start", "Month End",
        "Week", "Week Start", "Week End",
        "Day", "Fiscal Date", "Calendar Date", "Cal Day"
    ))
    print("-" * 190)

    for d in calendar["days"]:
        print("{:<10} {:<8} {:<15} {:<15} {:<8} {:<15} {:<15} {:<6} {:<15} {:<15} {:<10} {:<12} {:<15} {:<10}".format(
            d["fiscal_year"],
            d["quarter"],
            str(d["quarter_start"]),
            str(d["quarter_end"]),
            d["month"],
            str(d["month_start"]),
            str(d["month_end"]),
            d["week"],
            str(d["week_start"]),
            str(d["week_end"]),
            d["day"],
            str(d["fiscal_date"]),
            str(d["calendar_date"]),
            d["calendar_day"]
        ))


if __name__ == "__main__":
    try:
        user_input = input("Enter the fiscal year you want to view (e.g., 2026): ")
        fiscal_year = int(user_input)
        calendar = generate_fiscal_calendar(fiscal_year)
        print_fiscal_table(calendar)
        insert_calendar_to_db(calendar)
    except ValueError:
        print("Invalid input. Please enter a valid year as an integer (e.g., 2026).")
