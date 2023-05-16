# Imports
import csv

# Function buy product
def buy_product(product_name,price,expiration_date,amount,todays_date):
    with open("bought.csv", "a", newline="") as csv_file:
        bought_csv = csv.writer(csv_file)

        # Create var for last row id 
        with open("bought.csv", "r") as csv_file:
            rows_bought = list(csv.reader(csv_file))
        last_row_bought = rows_bought[-1]
        if last_row_bought[0] == "id":
            last_row_id = 0
        else: 
            last_row_id = last_row_bought[0]

        # Write command line to bought csv
        bought_csv.writerow([int(last_row_id) + 1,str.title(product_name).replace("_", " "),todays_date,"%.2f" % price,expiration_date,amount])
        print("OK")