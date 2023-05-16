# Imports
from datetime import datetime
import csv

# Function revenue today
def revenue_today(todays_date):
    revenue = 0

    # Increments revenue with sell price amount
    with open("sold.csv", "r") as csv_file:
        csv_sold = csv.reader(csv_file)
        next(csv_file)
        for row_sold in csv_sold:
            sell_date = datetime.strptime(row_sold[2], "%Y-%m-%d").date()
            if sell_date == todays_date:
                revenue += float(row_sold[3]) * int(row_sold[4])
    
    # Print revenue
    print("Today's revenue so far: " + str(revenue))

# Function revenue yesterday
def revenue_yesterday(yesterdays_date):
    revenue = 0
    
    # Increments revenue with sell price amount
    with open("sold.csv", "r") as csv_file:
        csv_sold = csv.reader(csv_file)
        next(csv_file)
        for row_sold in csv_sold:
            sell_date = datetime.strptime(row_sold[2], "%Y-%m-%d").date()
            if sell_date == yesterdays_date:
                revenue += float(row_sold[3]) * int(row_sold[4])

    # Print revenue
    print("Yesterday's revenue: " + str(revenue))

# Function revenue date
def revenue_date(date):
    revenue = 0

    # First try data format YYYY-MM-DD to report specific date
    try:
        year_month_day = datetime.strptime(date, "%Y-%m-%d").strftime("%d %B, %Y")

        # Increments revenue with sell price amount
        with open("sold.csv", "r") as csv_file:
            csv_sold = csv.reader(csv_file)
            next(csv_file)
            for row_sold in csv_sold:
                sell_date = datetime.strptime(row_sold[2], "%Y-%m-%d").strftime("%Y-%m-%d")
                if sell_date == date:
                    revenue += float(row_sold[3]) * int(row_sold[4])

        # Print revenue
        print("Revenue from " + year_month_day + ": " + str(revenue))

    # Then try data format YYYY-MM to report specific year and month
    except ValueError:
        try:
            year_month = datetime.strptime(date, "%Y-%m").strftime("%B, %Y")

            # Increments revenue with sell price amount
            with open("sold.csv", "r") as csv_file:
                csv_sold = csv.reader(csv_file)
                next(csv_file)
                for row_sold in csv_sold:
                    sell_date = datetime.strptime(row_sold[2], "%Y-%m-%d").strftime("%Y-%m")
                    if sell_date == date:
                        revenue += float(row_sold[3]) * int(row_sold[4])
            
            # Print revenue
            print("Revenue from " + year_month + ": " + str(revenue))

        # At last try data format YYYY to report specific year
        except ValueError:
            year = datetime.strptime(date, "%Y").strftime("%Y")

            # Increments revenue with sell price amount
            with open("sold.csv", "r") as csv_file:
                csv_sold = csv.reader(csv_file)
                next(csv_file)
                for row_sold in csv_sold:
                    sell_date = datetime.strptime(row_sold[2], "%Y-%m-%d").strftime("%Y")
                    if sell_date == date:
                        revenue += float(row_sold[3]) * int(row_sold[4])

            # Print revenue
            print("Revenue from " + year + ": " + str(revenue))

# Function revenue between start and end
def revenue_between_start_and_end(start_date,end_date):
    revenue = 0

    # Increments revenue with sell price amount
    with open("sold.csv", "r") as csv_file:
        csv_sold = csv.reader(csv_file)
        next(csv_file)
        for row_sold in csv_sold:
            sell_date = datetime.strptime(row_sold[2], "%Y-%m-%d").date()
            if sell_date >= start_date and sell_date <= end_date:
                revenue += float(row_sold[3]) * int(row_sold[4])

    # Print revenue
    print("Revenue between " + start_date.strftime("%d %B, %Y") + " and " + end_date.strftime("%d %B, %Y") + ": " + str(revenue))

# Function revenue after start
def revenue_after_start(start_date):
    revenue = 0

    # Increments revenue with sell price amount
    with open("sold.csv", "r") as csv_file:
        csv_sold = csv.reader(csv_file)
        next(csv_file)
        for row_sold in csv_sold:
            sell_date = datetime.strptime(row_sold[2], "%Y-%m-%d").date()
            if sell_date >= start_date:
                revenue += float(row_sold[3]) * int(row_sold[4])
    
    # Print revenue
    print("Revenue on and after " + start_date.strftime("%d %B, %Y") + ": " + str(revenue))

# Function revenue before end
def revenue_before_end(end_date):
    revenue = 0

    # Increments revenue with sell price amount
    with open("sold.csv", "r") as csv_file:
        csv_sold = csv.reader(csv_file)
        next(csv_file)
        for row_sold in csv_sold:
            sell_date = datetime.strptime(row_sold[2], "%Y-%m-%d").date()
            if sell_date <= end_date:
                revenue += float(row_sold[3]) * int(row_sold[4])
    
    # Print revenue
    print("Revenue on and before " + end_date.strftime("%d %B, %Y") + ": " + str(revenue))