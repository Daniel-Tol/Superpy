# Imports
from datetime import datetime
import csv

# Function profit today
def profit_today(todays_date):
    profit = 0

    # Increments profit with sell price amount
    with open("sold.csv", "r") as csv_file:
        csv_sold = csv.reader(csv_file)
        next(csv_file)
        for row_sold in csv_sold:
            sell_date = datetime.strptime(row_sold[2], "%Y-%m-%d").date()
            if sell_date == todays_date:
                profit += float(row_sold[3]) * int(row_sold[4])

                # Decrement profit with buy price amount
                with open("bought.csv", "r") as csv_file:
                    csv_bought = csv.reader(csv_file)
                    for row_bought in csv_bought:
                        if row_sold[1] == row_bought[0]:
                            profit -= float(row_bought[3]) * int(row_sold[4])
    
    # Print profit
    print("Today's profit so far: " + str(profit))

# Function profit yesterday
def profit_yesterday(yesterdays_date):
    profit = 0
    # Increments profit with sell price amount
    with open("sold.csv", "r") as csv_file:
        csv_sold = csv.reader(csv_file)
        next(csv_file)
        for row_sold in csv_sold:
            sell_date = datetime.strptime(row_sold[2], "%Y-%m-%d").date()
            if sell_date == yesterdays_date:
                profit += float(row_sold[3]) * int(row_sold[4])

                # Decrement profit with buy price amount
                with open("bought.csv", "r") as csv_file:
                    csv_bought = csv.reader(csv_file)
                    for row_bought in csv_bought:
                        if row_sold[1] == row_bought[0]:
                            profit -= float(row_bought[3]) * int(row_sold[4])

    # Print profit
    print("Yesterday's profit: " + str(profit))

# Function profit date
def profit_date(date):
    profit = 0

    # First try data format YYYY-MM-DD to report specific date
    try:
        year_month_day = datetime.strptime(date, "%Y-%m-%d").strftime("%d %B, %Y")

        # Increments profit with sell price amount
        with open("sold.csv", "r") as csv_file:
            csv_sold = csv.reader(csv_file)
            next(csv_file)
            for row_sold in csv_sold:
                sell_date = datetime.strptime(row_sold[2], "%Y-%m-%d").strftime("%Y-%m-%d")
                if sell_date == date:
                    profit += float(row_sold[3]) * int(row_sold[4])

                    # Decrement profit with buy price amount
                    with open("bought.csv", "r") as csv_file:
                        csv_bought = csv.reader(csv_file)
                        for row_bought in csv_bought:
                            if row_sold[1] == row_bought[0]:
                                profit -= float(row_bought[3]) * int(row_sold[4])

        # Print profit
        print("Profit from " + year_month_day + ": " + str(profit))

    # Then try data format YYYY-MM to report specific year and month
    except ValueError:
        try:
            year_month = datetime.strptime(date, "%Y-%m").strftime("%B, %Y")

            # Increments profit with sell price amount
            with open("sold.csv", "r") as csv_file:
                csv_sold = csv.reader(csv_file)
                next(csv_file)
                for row_sold in csv_sold:
                    sell_date = datetime.strptime(row_sold[2], "%Y-%m-%d").strftime("%Y-%m")
                    if sell_date == date:
                        profit += float(row_sold[3]) * int(row_sold[4])

                        # Decrement profit with buy price amount
                        with open("bought.csv", "r") as csv_file:
                            csv_bought = csv.reader(csv_file)
                            for row_bought in csv_bought:
                                if row_sold[1] == row_bought[0]:
                                    profit -= float(row_bought[3]) * int(row_sold[4])
            
            # Print profit
            print("Profit from " + year_month + ": " + str(profit))

        # At last try data format YYYY to report specific year
        except ValueError:
            year = datetime.strptime(date, "%Y").strftime("%Y")

            # Increments profit with sell price amount
            with open("sold.csv", "r") as csv_file:
                csv_sold = csv.reader(csv_file)
                next(csv_file)
                for row_sold in csv_sold:
                    sell_date = datetime.strptime(row_sold[2], "%Y-%m-%d").strftime("%Y")
                    if sell_date == date:
                        profit += float(row_sold[3]) * int(row_sold[4])

                        # Decrement profit with buy price amount
                        with open("bought.csv", "r") as csv_file:
                            csv_bought = csv.reader(csv_file)
                            for row_bought in csv_bought:
                                if row_sold[1] == row_bought[0]:
                                    profit -= float(row_bought[3]) * int(row_sold[4])

            # Print profit
            print("Profit from " + year + ": " + str(profit))

# Function profit between start and end
def profit_between_start_and_end(start_date,end_date):
    profit = 0

    # Increments profit with sell price amount
    with open("sold.csv", "r") as csv_file:
        csv_sold = csv.reader(csv_file)
        next(csv_file)
        for row_sold in csv_sold:
            sell_date = datetime.strptime(row_sold[2], "%Y-%m-%d").date()
            if sell_date >= start_date and sell_date <= end_date:
                profit += float(row_sold[3]) * int(row_sold[4])

                # Decrement profit with buy price amount
                with open("bought.csv", "r") as csv_file:
                    csv_bought = csv.reader(csv_file)
                    for row_bought in csv_bought:
                        if row_sold[1] == row_bought[0]:
                            profit -= float(row_bought[3]) * int(row_sold[4])

    # Print profit
    print("Profit between " + start_date.strftime("%d %B, %Y") + " and " + end_date.strftime("%d %B, %Y") + ": " + str(profit))

# Function profit after start
def profit_after_start(start_date):
    profit = 0

    # Increments profit with sell price amount
    with open("sold.csv", "r") as csv_file:
        csv_sold = csv.reader(csv_file)
        next(csv_file)
        for row_sold in csv_sold:
            sell_date = datetime.strptime(row_sold[2], "%Y-%m-%d").date()
            if sell_date >= start_date:
                profit += float(row_sold[3]) * int(row_sold[4])

                # Decrement profit with buy price amount
                with open("bought.csv", "r") as csv_file:
                    csv_bought = csv.reader(csv_file)
                    for row_bought in csv_bought:
                        if row_sold[1] == row_bought[0]:
                            profit -= float(row_bought[3]) * int(row_sold[4])
    
    # Print profit
    print("Profit on and after " + start_date.strftime("%d %B, %Y") + ": " + str(profit))

# Function profit before end
def profit_before_end(end_date):
    profit = 0

    # Increments profit with sell price amount
    with open("sold.csv", "r") as csv_file:
        csv_sold = csv.reader(csv_file)
        next(csv_file)
        for row_sold in csv_sold:
            sell_date = datetime.strptime(row_sold[2], "%Y-%m-%d").date()
            if sell_date <= end_date:
                profit += float(row_sold[3]) * int(row_sold[4])
                
                # Decrement profit with buy price amount
                with open("bought.csv", "r") as csv_file:
                    csv_bought = csv.reader(csv_file)
                    for row_bought in csv_bought:
                        if row_sold[1] == row_bought[0]:
                            profit -= float(row_bought[3]) * int(row_sold[4])
    
    # Print profit
    print("Profit on and before " + end_date.strftime("%d %B, %Y") + ": " + str(profit))