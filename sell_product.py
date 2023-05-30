# Imports
from datetime import datetime
import csv


# Function sell product
def sell_product(product_name,price,amount,todays_date):
    list_sell = list()
    product_amount = amount

    # Append command line to list sell if product is in stock
    with open("bought.csv", "r") as csv_file:
        csv_bought = csv.reader(csv_file)
        next(csv_file)
        for row_bought in csv_bought:
            buy_date = datetime.strptime(row_bought[2], "%Y-%m-%d").date()
            expiration_date = datetime.strptime(row_bought[4], "%Y-%m-%d").date()
            if row_bought[1] == str.title(product_name).replace("_", " ") and buy_date <= todays_date and expiration_date > todays_date and product_amount != 0:
                combine_amount = 0

                # Increments combine amount when more than one row has the same id
                with open("sold.csv", "r") as csv_file:
                    csv_sold = csv.reader(csv_file)
                    for row_sold in csv_sold:
                        if row_bought[0] == row_sold[1]:
                            combine_amount += int(row_sold[4])

                    # If product has been partially sold, creates var amount unsold
                    if int(row_bought[5]) != combine_amount:
                        amount_unsold = int(row_bought[5]) - combine_amount

                        # If amount unsold higher than amount selling, row amount is product amount and product amount hits zero
                        if amount_unsold > product_amount:
                            row_bought[5] = product_amount
                            list_sell.append(row_bought)
                            product_amount = 0
                            
                        # Else, row amount is amount unsold and product amount is decremented with amount unsold
                        else:
                            row_bought[5] = amount_unsold
                            list_sell.append(row_bought)
                            product_amount -= amount_unsold

    # If product amount is decrement to zero, open sold csv
    if product_amount == 0:
        with open("sold.csv", "a", newline="") as csv_file:
            csv_sold = csv.writer(csv_file)
            
            # Create var for last row id and increment id
            with open("sold.csv", "r") as csv_file:
                rows_sold = list(csv.reader(csv_file))
            last_row_sold = rows_sold[-1]
            if last_row_sold[0] == "id":
                last_row_id = 0
            else: 
                last_row_id = last_row_sold[0]
            increment_id = 1

            # Append to sold csv and increment var increment id
            for row in list_sell:
                csv_sold.writerow([int(last_row_id) + increment_id,row[0],todays_date,"%.2f" % price,row[5]])
                increment_id += 1
            print("OK")

    # Else prints error that product or product amount is not in stock
    else:
        print("ERROR: Product (amount) not in stock.")