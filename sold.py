# Imports
from datetime import datetime
from rich.console import Console
from rich.table import Table
import csv

# Function sold today
def sold_today(todays_date):

    # Table
    table_today = Table(title="Sold today")
    table_today.add_column("Product Name", justify="right", style="cyan")
    table_today.add_column("Count", style="magenta")
    table_today.add_column("Sell Price", justify="right", style="green")

    # Add rows to table
    with open("sold.csv", "r") as csv_file:
        csv_sold = csv.reader(csv_file)
        next(csv_file)
        for row_sold in csv_sold:
            sell_date = datetime.strptime(row_sold[2], "%Y-%m-%d").date()
            if todays_date == sell_date:

                # Look for linked bought id to find the product name
                with open("bought.csv", "r") as csv_file:
                    csv_bought = csv.reader(csv_file)
                    for row_bought in csv_bought:
                        if row_sold[1] == row_bought[0]:
                            product_name = row_bought[1]

                # Add row
                table_today.add_row(product_name, row_sold[4], row_sold[3])

    # Print table
    console = Console()
    console.print(table_today)

# Function sold yesterday
def sold_yesterday(yesterdays_date):

    # Table
    table_yesterday = Table(title="Sold yesterday")
    table_yesterday.add_column("Product Name", justify="right", style="cyan")
    table_yesterday.add_column("Count", style="magenta")
    table_yesterday.add_column("Sell Price", justify="right", style="green")

    # Add rows to table
    with open("sold.csv", "r") as csv_file:
        csv_sold = csv.reader(csv_file)
        next(csv_file)
        for row_sold in csv_sold:
            sell_date = datetime.strptime(row_sold[2], "%Y-%m-%d").date()
            if yesterdays_date == sell_date:

                # Look for linked bought id to find the product name
                with open("bought.csv", "r") as csv_file:
                    csv_bought = csv.reader(csv_file)
                    for row_bought in csv_bought:
                        if row_sold[1] == row_bought[0]:
                            product_name = row_bought[1]
        
                # Add row
                table_yesterday.add_row(product_name, row_sold[4], row_sold[3])

    # Print table
    console = Console()
    console.print(table_yesterday)

# Function sold date
def sold_date(date):

    # First try data format YYYY-MM-DD to report specific date
    try:
        title_year_month_day = datetime.strptime(date, "%Y-%m-%d").strftime("%d %B, %Y")

        # Table
        table_sold_date = Table(title="Sold on " + title_year_month_day)
        table_sold_date.add_column("Product Name", justify="right", style="cyan")
        table_sold_date.add_column("Count", style="magenta")
        table_sold_date.add_column("Sell Price", justify="right", style="green")

        # Add rows to table
        with open("sold.csv", "r") as csv_file:
            csv_sold = csv.reader(csv_file)
            next(csv_file)
            for row_sold in csv_sold:
                sell_date = datetime.strptime(row_sold[2], "%Y-%m-%d").strftime("%Y-%m-%d")
                if date == sell_date:

                    # Look for linked bought id to find the product name
                    with open("bought.csv", "r") as csv_file:
                        csv_bought = csv.reader(csv_file)
                        for row_bought in csv_bought:
                            if row_sold[1] == row_bought[0]:
                                product_name = row_bought[1]

                    # Add row
                    table_sold_date.add_row(product_name, row_sold[4], row_sold[3])

        # Print table
        console = Console()
        console.print(table_sold_date)

    # Then try data format YYYY-MM to report specific year and month
    except ValueError:
        try:
            title_year_month = datetime.strptime(date, "%Y-%m").strftime("%B, %Y")

            # Table
            table_sold_date = Table(title="Sold in " + title_year_month)
            table_sold_date.add_column("Product Name", justify="right", style="cyan")
            table_sold_date.add_column("Count", style="magenta")
            table_sold_date.add_column("Sell Price", justify="right", style="green")
            table_sold_date.add_column("Sell Day", justify="right", style="blue")

            # Add rows to table
            with open("sold.csv", "r") as csv_file:
                csv_sold = csv.reader(csv_file)
                next(csv_file)
                for row_sold in csv_sold:
                    sell_date = datetime.strptime(row_sold[2], "%Y-%m-%d").strftime("%Y-%m")
                    if date == sell_date:

                        # Look for linked bought id to find the product name
                        with open("bought.csv", "r") as csv_file:
                            csv_bought = csv.reader(csv_file)
                            for row_bought in csv_bought:
                                if row_sold[1] == row_bought[0]:
                                    product_name = row_bought[1]

                        # Add row
                        day = datetime.strptime(row_sold[2], "%Y-%m-%d").strftime("%d")
                        table_sold_date.add_row(product_name, row_sold[4], row_sold[3], day)

            # Print table
            console = Console()
            console.print(table_sold_date)

        # At last try data format YYYY to report specific year
        except ValueError:
            title_year = datetime.strptime(date, "%Y").strftime("%Y")

            # Table
            table_sold_date = Table(title="Sold in " + title_year)
            table_sold_date.add_column("Product Name", justify="right", style="cyan")
            table_sold_date.add_column("Count", style="magenta")
            table_sold_date.add_column("Sell Price", justify="right", style="green")
            table_sold_date.add_column("Sell Date", justify="right", style="blue")

            # Add rows to table
            with open("sold.csv", "r") as csv_file:
                csv_sold = csv.reader(csv_file)
                next(csv_file)
                for row_sold in csv_sold:
                    sell_date = datetime.strptime(row_sold[2], "%Y-%m-%d").strftime("%Y")
                    if date == sell_date:

                        # Look for linked bought id to find the product name
                        with open("bought.csv", "r") as csv_file:
                            csv_bought = csv.reader(csv_file)
                            for row_bought in csv_bought:
                                if row_sold[1] == row_bought[0]:
                                    product_name = row_bought[1]

                        # Add row
                        month_day = datetime.strptime(row_sold[2], "%Y-%m-%d").strftime("%m-%d")
                        table_sold_date.add_row(product_name, row_sold[4], row_sold[3], month_day)

            # Print table
            console = Console()
            console.print(table_sold_date)

# Function sold between start and end
def sold_between_start_and_end(start_date,end_date):
    title_start_date = start_date.strftime("%d %B, %Y")
    title_end_date = end_date.strftime("%d %B, %Y")

    # Table
    table_sold_between_start_and_end = Table(title="Sold between " + title_start_date + " and " + title_end_date)
    table_sold_between_start_and_end.add_column("Product Name", justify="right", style="cyan")
    table_sold_between_start_and_end.add_column("Count", style="magenta")
    table_sold_between_start_and_end.add_column("Sell Price", justify="right", style="green")
    table_sold_between_start_and_end.add_column("Sell Date", justify="right", style="blue")

    # Add rows to table
    with open("sold.csv", "r") as csv_file:
        csv_sold = csv.reader(csv_file)
        next(csv_file)
        for row_sold in csv_sold:
            sell_date = datetime.strptime(row_sold[2], "%Y-%m-%d").date()
            if sell_date >= start_date and sell_date <= end_date:

                # Look for linked bought id to find the product name
                with open("bought.csv", "r") as csv_file:
                    csv_bought = csv.reader(csv_file)
                    for row_bought in csv_bought:
                        if row_sold[1] == row_bought[0]:
                            product_name = row_bought[1]

                # Add row
                table_sold_between_start_and_end.add_row(product_name, row_sold[4], row_sold[3], row_sold[2])

    # Print table
    console = Console()
    console.print(table_sold_between_start_and_end)

# Function sold after start
def sold_after_start(start_date):
    title_start_date = start_date.strftime("%d %B, %Y")

    # Table
    table_sold_after_start = Table(title="Sold on and after " + title_start_date)
    table_sold_after_start.add_column("Product Name", justify="right", style="cyan")
    table_sold_after_start.add_column("Count", style="magenta")
    table_sold_after_start.add_column("Sell Price", justify="right", style="green")
    table_sold_after_start.add_column("Sell Date", justify="right", style="blue")

    # Add rows to table
    with open("sold.csv", "r") as csv_file:
        csv_sold = csv.reader(csv_file)
        next(csv_file)
        for row_sold in csv_sold:
            sell_date = datetime.strptime(row_sold[2], "%Y-%m-%d").date()
            if sell_date >= start_date:

                # Look for linked bought id to find the product name
                with open("bought.csv", "r") as csv_file:
                    csv_bought = csv.reader(csv_file)
                    for row_bought in csv_bought:
                        if row_sold[1] == row_bought[0]:
                            product_name = row_bought[1]

                # Add row
                table_sold_after_start.add_row(product_name, row_sold[4], row_sold[3], row_sold[2])

    # Print table
    console = Console()
    console.print(table_sold_after_start)

# Function sold before end
def sold_before_end(end_date):
    title_end_date = end_date.strftime("%d %B, %Y")

    # Table
    table_sold_before_end = Table(title="Sold on and before " + title_end_date)
    table_sold_before_end.add_column("Product Name", justify="right", style="cyan")
    table_sold_before_end.add_column("Count", style="magenta")
    table_sold_before_end.add_column("Sell Price", justify="right", style="green")
    table_sold_before_end.add_column("Sell Date", justify="right", style="blue")

    # Add rows to table
    with open("sold.csv", "r") as csv_file:
        csv_sold = csv.reader(csv_file)
        next(csv_file)
        for row_sold in csv_sold:
            sell_date = datetime.strptime(row_sold[2], "%Y-%m-%d").date()
            if sell_date <= end_date:

                # Look for linked bought id to find the product name
                with open("bought.csv", "r") as csv_file:
                    csv_bought = csv.reader(csv_file)
                    for row_bought in csv_bought:
                        if row_sold[1] == row_bought[0]:
                            product_name = row_bought[1]

                # Add row
                table_sold_before_end.add_row(product_name, row_sold[4], row_sold[3], row_sold[2])

    # Print table
    console = Console()
    console.print(table_sold_before_end)