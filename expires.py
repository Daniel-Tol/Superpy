# Imports
from datetime import datetime
from rich.console import Console
from rich.table import Table
import csv

# Function expires today
def expires_today(todays_date):

    # Table
    table_expired_today = Table(title="Expired today")
    table_expired_today.add_column("Product Name", justify="right", style="cyan")
    table_expired_today.add_column("Count", style="magenta")
    table_expired_today.add_column("Buy Price", justify="right", style="green")

    # Add rows to table
    with open("bought.csv", "r") as csv_file:
        csv_bought = csv.reader(csv_file)
        next(csv_file)
        for row_bought in csv_bought:
            expired_date = datetime.strptime(row_bought[4], "%Y-%m-%d").date()
            if expired_date == todays_date:
                combine_amount = 0

                # Increments combine amount if linked id sold row is the same as bought row id
                with open("sold.csv", "r") as csv_file:
                    csv_sold = csv.reader(csv_file)
                    for row_sold in csv_sold:
                        if row_bought[0] == row_sold[1]:
                            combine_amount += int(row_sold[4])

                # Decrements the amount that has been sold with combine amount
                if row_bought[5] != str(combine_amount):
                    amount_unsold = int(row_bought[5]) - combine_amount
                    row_bought[5] = str(amount_unsold)
                    table_expired_today.add_row(row_bought[1], row_bought[5], row_bought[3])

    # Print table
    console = Console()
    console.print(table_expired_today)

# Function expires yesterday
def expires_yesterday(yesterdays_date):

    # Table
    table_expired_yesterday = Table(title="Expired yesterday")
    table_expired_yesterday.add_column("Product Name", justify="right", style="cyan")
    table_expired_yesterday.add_column("Count", style="magenta")
    table_expired_yesterday.add_column("Buy Price", justify="right", style="green")

    # Add rows to table
    with open("bought.csv", "r") as csv_file:
        csv_bought = csv.reader(csv_file)
        next(csv_file)
        for row_bought in csv_bought:
            expired_date = datetime.strptime(row_bought[4], "%Y-%m-%d").date()
            if expired_date == yesterdays_date:
                combine_amount = 0

                # Increments combine amount if linked id sold row is the same as bought row id
                with open("sold.csv", "r") as csv_file:
                    csv_sold = csv.reader(csv_file)
                    for row_sold in csv_sold:
                        if row_bought[0] == row_sold[1]:
                            combine_amount += int(row_sold[4])

                # Decrements the amount that has been sold with combine amount
                if row_bought[5] != str(combine_amount):
                    amount_unsold = int(row_bought[5]) - combine_amount
                    row_bought[5] = str(amount_unsold)
                    table_expired_yesterday.add_row(row_bought[1], row_bought[5], row_bought[3])

    # Print table
    console = Console()
    console.print(table_expired_yesterday)

# Function expires date
def expires_date(date):

    # First try data format YYYY-MM-DD to report specific date
    try:
        title_year_month_day = datetime.strptime(date, "%Y-%m-%d").strftime("%d %B, %Y")

        # Table
        table_expired_date = Table(title="Expires in " + title_year_month_day)
        table_expired_date.add_column("Product Name", justify="right", style="cyan")
        table_expired_date.add_column("Count", style="magenta")
        table_expired_date.add_column("Sell Price", justify="right", style="green")

        # Add rows to table
        with open("bought.csv", "r") as csv_file:
            csv_bought = csv.reader(csv_file)
            next(csv_file)
            for row_bought in csv_bought:
                expired_date = datetime.strptime(row_bought[4], "%Y-%m-%d").strftime("%Y-%m-%d")
                if expired_date == date:
                    combine_amount = 0

                    # Increments combine amount if linked id sold row is the same as bought row id
                    with open("sold.csv", "r") as csv_file:
                        csv_sold = csv.reader(csv_file)
                        for row_sold in csv_sold:
                            if row_bought[0] == row_sold[1]:
                                combine_amount += int(row_sold[4])

                    # Decrements the amount that has been sold with combine amount
                    if row_bought[5] != str(combine_amount):
                        amount_unsold = int(row_bought[5]) - combine_amount
                        row_bought[5] = str(amount_unsold)
                        table_expired_date.add_row(row_bought[1], row_bought[5], row_bought[3])

        # Print table
        console = Console()
        console.print(table_expired_date)

    # Then try data format YYYY-MM to report specific year and month
    except ValueError: 
        try:
            title_year_month = datetime.strptime(date, "%Y-%m").strftime("%B, %Y")

            # Table
            table_expired_date = Table(title="Expires in " + title_year_month)
            table_expired_date.add_column("Product Name", justify="right", style="cyan")
            table_expired_date.add_column("Count", style="magenta")
            table_expired_date.add_column("Buy Price", justify="right", style="green")
            table_expired_date.add_column("Expiration Day", justify="right", style="blue")

            # Add rows to table
            with open("bought.csv", "r") as csv_file:
                csv_bought = csv.reader(csv_file)
                next(csv_file)
                for row_bought in csv_bought:
                    expired_date = datetime.strptime(row_bought[4], "%Y-%m-%d").strftime("%Y-%m")
                    if expired_date == date:
                        combine_amount = 0

                        # Increments combine amount if linked id sold row is the same as bought row id
                        with open("sold.csv", "r") as csv_file:
                            csv_sold = csv.reader(csv_file)
                            for row_sold in csv_sold:
                                if row_bought[0] == row_sold[1]:
                                    combine_amount += int(row_sold[4])

                        # Decrements the amount that has been sold with combine amount
                        if row_bought[5] != str(combine_amount):
                            amount_unsold = int(row_bought[5]) - combine_amount
                            row_bought[5] = str(amount_unsold)
                            day = datetime.strptime(row_bought[4], "%Y-%m-%d").strftime("%d")
                            table_expired_date.add_row(row_bought[1], row_bought[5], row_bought[3], day)

            # Print table
            console = Console()
            console.print(table_expired_date)

        # At last try data format YYYY to report specific year
        except ValueError: 
            title_year = datetime.strptime(date, "%Y").strftime("%Y")

            # Table
            table_expired_date = Table(title="Expires in " + title_year)
            table_expired_date.add_column("Product Name", justify="right", style="cyan")
            table_expired_date.add_column("Count", style="magenta")
            table_expired_date.add_column("Buy Price", justify="right", style="green")
            table_expired_date.add_column("Expiration Date", justify="right", style="blue")

            # Add rows to table
            with open("bought.csv", "r") as csv_file:
                csv_bought = csv.reader(csv_file)
                next(csv_file)
                for row_bought in csv_bought:
                    expired_date = datetime.strptime(row_bought[4], "%Y-%m-%d").strftime("%Y")
                    if expired_date == date:
                        combine_amount = 0

                        # Increments combine amount if linked id sold row is the same as bought row id
                        with open("sold.csv", "r") as csv_file:
                            csv_sold = csv.reader(csv_file)
                            for row_sold in csv_sold:
                                if row_bought[0] == row_sold[1]:
                                    combine_amount += int(row_sold[4])

                        # Decrements the amount that has been sold with combine amount
                        if row_bought[5] != str(combine_amount):
                            amount_unsold = int(row_bought[5]) - combine_amount
                            row_bought[5] = str(amount_unsold)
                            month_day = datetime.strptime(row_bought[4], "%Y-%m-%d").strftime("%m-%d")
                            table_expired_date.add_row(row_bought[1], row_bought[5], row_bought[3], month_day)

            # Print table
            console = Console()
            console.print(table_expired_date)

# Function expires between start and end
def expires_between_start_and_end(start_date,end_date):
    title_start_date = start_date.strftime("%d %B, %Y")
    title_end_date = end_date.strftime("%d %B, %Y")

    # Table
    table_expired_between_start_and_end = Table(title="Expires between " + title_start_date + " and " + title_end_date)
    table_expired_between_start_and_end.add_column("Product Name", justify="right", style="cyan")
    table_expired_between_start_and_end.add_column("Count", style="magenta")
    table_expired_between_start_and_end.add_column("Buy Price", justify="right", style="green")
    table_expired_between_start_and_end.add_column("Expiration Date", justify="right", style="blue")

    # Add rows to table
    with open("bought.csv", "r") as csv_file:
        csv_bought = csv.reader(csv_file)
        next(csv_file)
        for row_bought in csv_bought:
            expired_date = datetime.strptime(row_bought[4], "%Y-%m-%d").date()
            if expired_date >= start_date and expired_date <= end_date:
                combine_amount = 0

                # Increments combine amount if linked id sold row is the same as bought row id
                with open("sold.csv", "r") as csv_file:
                    csv_sold = csv.reader(csv_file)
                    for row_sold in csv_sold:
                        if row_bought[0] == row_sold[1]:
                            combine_amount += int(row_sold[4])

                # Decrements the amount that has been sold with combine amount
                if row_bought[5] != str(combine_amount):
                    amount_unsold = int(row_bought[5]) - combine_amount
                    row_bought[5] = str(amount_unsold)
                    table_expired_between_start_and_end.add_row(row_bought[1], row_bought[5], row_bought[3], row_bought[4])

    # Print table
    console = Console()
    console.print(table_expired_between_start_and_end)

# Function expires after start
def expires_after_start(start_date):
    title_start_date = start_date.strftime("%d %B, %Y")

    # Table
    table_expired_after_start = Table(title="Expires after or on " + title_start_date)
    table_expired_after_start.add_column("Product Name", justify="right", style="cyan")
    table_expired_after_start.add_column("Count", style="magenta")
    table_expired_after_start.add_column("Buy Price", justify="right", style="green")
    table_expired_after_start.add_column("Expiration Date", justify="right", style="blue")

    # Add rows to table
    with open("bought.csv", "r") as csv_file:
        csv_bought = csv.reader(csv_file)
        next(csv_file)
        for row_bought in csv_bought:
            expired_date = datetime.strptime(row_bought[4], "%Y-%m-%d").date()
            if expired_date >= start_date:
                combine_amount = 0

                # Increments combine amount if linked id sold row is the same as bought row id
                with open("sold.csv", "r") as csv_file:
                    csv_sold = csv.reader(csv_file)
                    for row_sold in csv_sold:
                        if row_bought[0] == row_sold[1]:
                            combine_amount += int(row_sold[4])

                # Decrements the amount that has been sold with combine amount
                if row_bought[5] != str(combine_amount):
                    amount_unsold = int(row_bought[5]) - combine_amount
                    row_bought[5] = str(amount_unsold)
                    table_expired_after_start.add_row(row_bought[1], row_bought[5], row_bought[3], row_bought[4])

    # Print table
    console = Console()
    console.print(table_expired_after_start)

# Function expires before end
def expires_before_end(end_date):
    title_end_date = end_date.strftime("%d %B, %Y")

    # Table
    table_expired_before_end = Table(title="Expires before or on " + title_end_date)
    table_expired_before_end.add_column("Product Name", justify="right", style="cyan")
    table_expired_before_end.add_column("Count", style="magenta")
    table_expired_before_end.add_column("Buy Price", justify="right", style="green")
    table_expired_before_end.add_column("Expiration Date", justify="right", style="blue")

    # Add rows to table
    with open("bought.csv", "r") as csv_file:
        csv_bought = csv.reader(csv_file)
        next(csv_file)
        for row_bought in csv_bought:
            expired_date = datetime.strptime(row_bought[4], "%Y-%m-%d").date()
            if expired_date <= end_date:
                combine_amount = 0

                # Increments combine amount if linked id sold row is the same as bought row id
                with open("sold.csv", "r") as csv_file:
                    csv_sold = csv.reader(csv_file)
                    for row_sold in csv_sold:
                        if row_bought[0] == row_sold[1]:
                            combine_amount += int(row_sold[4])

                # Decrements the amount that has been sold with combine amount
                if row_bought[5] != str(combine_amount):
                    amount_unsold = int(row_bought[5]) - combine_amount
                    row_bought[5] = str(amount_unsold)
                    table_expired_before_end.add_row(row_bought[1], row_bought[5], row_bought[3], row_bought[4])

    # Print table
    console = Console()
    console.print(table_expired_before_end)

# Function expires tomorrow
def expires_tomorrow(tomorrows_date):

    # Table
    table_expires_tomorrow = Table(title="Expires tomorrow")
    table_expires_tomorrow.add_column("Product Name", justify="right", style="cyan")
    table_expires_tomorrow.add_column("Count", style="magenta")
    table_expires_tomorrow.add_column("Buy Price", justify="right", style="green")

    # Add rows to table
    with open("bought.csv", "r") as csv_file:
        csv_bought = csv.reader(csv_file)
        next(csv_file)
        for row_bought in csv_bought:
            expired_date = datetime.strptime(row_bought[4], "%Y-%m-%d").date()
            if expired_date == tomorrows_date:
                combine_amount = 0

                # Increments combine amount if linked id sold row is the same as bought row id
                with open("sold.csv", "r") as csv_file:
                    csv_sold = csv.reader(csv_file)
                    for row_sold in csv_sold:
                        if row_bought[0] == row_sold[1]:
                            combine_amount += int(row_sold[4])

                # Decrements the amount that has been sold with combine amount
                if row_bought[5] != str(combine_amount):
                    amount_unsold = int(row_bought[5]) - combine_amount
                    row_bought[5] = str(amount_unsold)
                    table_expires_tomorrow.add_row(row_bought[1], row_bought[5], row_bought[3])

    # Print table
    console = Console()
    console.print(table_expires_tomorrow)

# Function expires within one week
def expires_within_one_week(one_week,todays_date):

    # Table
    table_expires_within_one_week = Table(title="Expires within one week")
    table_expires_within_one_week.add_column("Product Name", justify="right", style="cyan")
    table_expires_within_one_week.add_column("Count", style="magenta")
    table_expires_within_one_week.add_column("Buy Price", justify="right", style="green")
    table_expires_within_one_week.add_column("Expiration Date", justify="right", style="blue")

    # Add rows to table
    with open("bought.csv", "r") as csv_file:
        csv_bought = csv.reader(csv_file)
        next(csv_file)
        for row_bought in csv_bought:
            expired_date = datetime.strptime(row_bought[4], "%Y-%m-%d").date()
            if expired_date >= todays_date and expired_date <= one_week:
                combine_amount = 0

                # Increments combine amount if linked id sold row is the same as bought row id
                with open("sold.csv", "r") as csv_file:
                    csv_sold = csv.reader(csv_file)
                    for row_sold in csv_sold:
                        if row_bought[0] == row_sold[1]:
                            combine_amount += int(row_sold[4])

                # Decrements the amount that has been sold with combine amount
                if row_bought[5] != str(combine_amount):
                    amount_unsold = int(row_bought[5]) - combine_amount
                    row_bought[5] = str(amount_unsold)
                    table_expires_within_one_week.add_row(row_bought[1], row_bought[5], row_bought[3], row_bought[4])

    # Print table
    console = Console()
    console.print(table_expires_within_one_week)