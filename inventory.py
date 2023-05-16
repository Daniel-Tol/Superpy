# Imports
from datetime import datetime
from rich.console import Console
from rich.table import Table
import csv

# Function inventory today
def inventory_today(todays_date):

    # Table
    table_today = Table(title="Inventory today")
    table_today.add_column("Product Name", justify="right", style="cyan")
    table_today.add_column("Count", style="magenta")
    table_today.add_column("Buy Price", justify="right", style="green")
    table_today.add_column("Expiration Date", justify="right", style="blue")

    # Add rows to table
    with open("bought.csv", "r") as csv_file:
        csv_bought = csv.reader(csv_file)
        next(csv_file)
        for row_bought in csv_bought:
            buy_date = datetime.strptime(row_bought[2], "%Y-%m-%d").date()
            expired_date = datetime.strptime(row_bought[4], "%Y-%m-%d").date()
            if buy_date <= todays_date and expired_date >= todays_date:
                combine_amount = 0

                # Increments combine amount when more than one row has the same id
                with open("sold.csv", "r") as csv_file:
                    csv_sold = csv.reader(csv_file)
                    for row_sold in csv_sold:
                        if row_bought[0] == row_sold[1]:
                            sell_date = datetime.strptime(row_sold[2], "%Y-%m-%d").date()
                            if sell_date <= todays_date:
                                combine_amount += int(row_sold[4])

                # Decrements the amount that has been sold with combine amount
                if row_bought[5] != str(combine_amount):
                    amount_unsold = int(row_bought[5]) - combine_amount
                    row_bought[5] = str(amount_unsold)
                    table_today.add_row(row_bought[1], row_bought[5], row_bought[3], row_bought[4])

    # Print table
    console = Console()
    console.print(table_today)

# Function inventory yesterday
def inventory_yesterday(yesterdays_date):

    # Table
    table_yesterday = Table(title="Inventory yesterday")
    table_yesterday.add_column("Product Name", justify="right", style="cyan")
    table_yesterday.add_column("Count", style="magenta")
    table_yesterday.add_column("Buy Price", justify="right", style="green")
    table_yesterday.add_column("Expiration Date", justify="right", style="blue")

    # Add rows to table
    with open("bought.csv", "r") as csv_file:
        csv_bought = csv.reader(csv_file)
        next(csv_file)
        for row_bought in csv_bought:
            buy_date = datetime.strptime(row_bought[2], "%Y-%m-%d").date()
            expired_date = datetime.strptime(row_bought[4], "%Y-%m-%d").date()
            if buy_date <= yesterdays_date and expired_date >= yesterdays_date:
                combine_amount = 0

                # Increments combine amount when more than one row has the same id
                with open("sold.csv", "r") as csv_file:
                    csv_sold = csv.reader(csv_file)
                    for row_sold in csv_sold:
                        if row_bought[0] == row_sold[1]:
                            sell_date = datetime.strptime(row_sold[2], "%Y-%m-%d").date()
                            if sell_date <= yesterdays_date:
                                combine_amount += int(row_sold[4])

                # Decrements the amount that has been sold with combine amount
                if row_bought[5] != str(combine_amount):
                    amount_unsold = int(row_bought[5]) - combine_amount
                    row_bought[5] = str(amount_unsold)
                    table_yesterday.add_row(row_bought[1], row_bought[5], row_bought[3], row_bought[4])

    # Print table
    console = Console()
    console.print(table_yesterday)

# Function inventory date
def inventory_date(date):
    title_date = date.strftime("%d %B, %Y")

    # Table
    table_date = Table(title="Inventory on " + title_date)
    table_date.add_column("Product Name", justify="right", style="cyan")
    table_date.add_column("Count", style="magenta")
    table_date.add_column("Buy Price", justify="right", style="green")
    table_date.add_column("Expiration Date", justify="right", style="blue")

    # Add rows to table
    with open("bought.csv", "r") as csv_file:
        csv_bought = csv.reader(csv_file)
        next(csv_file)
        for row_bought in csv_bought:
            buy_date = datetime.strptime(row_bought[2], "%Y-%m-%d").date()
            expired_date = datetime.strptime(row_bought[4], "%Y-%m-%d").date()
            if buy_date <= date and expired_date >= date:
                combine_amount = 0

                # Increments combine amount when more than one row has the same id
                with open("sold.csv", "r") as csv_file:
                    csv_sold = csv.reader(csv_file)
                    for row_sold in csv_sold:
                        if row_bought[0] == row_sold[1]:
                            sell_date = datetime.strptime(row_sold[2], "%Y-%m-%d").date()
                            if sell_date <= date:
                                combine_amount += int(row_sold[4])

                # Decrements the amount that has been sold with combine amount
                if row_bought[5] != str(combine_amount):
                    amount_unsold = int(row_bought[5]) - combine_amount
                    row_bought[5] = str(amount_unsold)
                    table_date.add_row(row_bought[1], row_bought[5], row_bought[3], row_bought[4])

    # Print table
    console = Console()
    console.print(table_date)
