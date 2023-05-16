# Imports
import argparse
from datetime import date, datetime, timedelta
from buy_product import buy_product
from sell_product import sell_product
from inventory import inventory_today, inventory_yesterday, inventory_date
from sold import sold_today, sold_yesterday, sold_date, sold_between_start_and_end, sold_after_start, sold_before_end
from expires import expires_today, expires_yesterday, expires_date, expires_between_start_and_end, expires_after_start, expires_before_end, expires_tomorrow, expires_within_one_week
from revenue import revenue_today, revenue_yesterday, revenue_date, revenue_between_start_and_end, revenue_after_start, revenue_before_end
from profit import profit_today, profit_yesterday, profit_date, profit_between_start_and_end, profit_after_start, profit_before_end

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
    pass

# Validates date and returns the choosen data format as a string
def validate_date(date):
    try:
        return datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError:
        try: 
            return datetime.strptime(date, "%Y-%m").strftime("%Y-%m")
        except ValueError:
            try:
                return datetime.strptime(date, "%Y").strftime("%Y")
            except ValueError:
                message = "not a valid date: {0!r}\n".format(date) + "Valid data formats are 'YYYY-MM-DD', 'YYYY-MM' and 'YYYY'."
                raise argparse.ArgumentTypeError(message)
            
# Validates date and returns datetime.date
def validate_specific_date(date):
    try:
        return datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
                message = "not a valid date: {0!r}\n".format(date) + "Valid data format is 'YYYY-MM-DD'."
                raise argparse.ArgumentTypeError(message)

# Create parser, argument and subparser
parser = argparse.ArgumentParser(prog="Superpy", formatter_class=argparse.RawTextHelpFormatter, 
description="Buy products, sell products, change time and report various data of the store.\n"
"Please choose between 'buy', 'sell' or 'report'.\n Change the time with '--advance_time', '--reverse_time' or '--correct_time'")
parser.add_argument("--advance_time", type=int, help="Advances days by number count. Requires number.")
parser.add_argument("--reverse_time", type=int, help="Reverses days by number count. Requires number.")
parser.add_argument("--correct_time", action="store_true", help="Changes date to current official date. No value needed.")
subparsers = parser.add_subparsers(dest="command")

# Subparser buy
buy_parser = subparsers.add_parser("buy", help="Buy products. Requires arguments are '--product_name', '--price', '--expiration_date' and '--amount'.")
buy_parser.add_argument("--product_name", type=str, required=True, help="Name of the product. Use underscore for multiple words.")
buy_parser.add_argument("--price", type=float, required=True, help="Buying price of the product. Requires number and accepts number after decimal point.")
buy_parser.add_argument("--expiration_date", type=validate_specific_date, required=True, help="Expiration date of the product. Data format is 'YYYY-MM-DD'.")
buy_parser.add_argument("--amount", type=int, required=True, help="The amount of the product to buy. Requires number.")

# Subparser sell
sell_parser =  subparsers.add_parser("sell", help="Sell products. Requires arguments are '--product_name', '--price', '--expiration_date' and '--amount'.")
sell_parser.add_argument("--product_name", type=str, required=True, help="Name of the product. Use underscore for multiple words.")
sell_parser.add_argument("--price", type=float, required=True, help="Requires number and accepts number after decimal point.")
sell_parser.add_argument("--expiration_date", type=validate_specific_date, required=True, help="Expiration date of the product. Data format is 'YYYY-MM-DD'.")
sell_parser.add_argument("--amount", type=int, required=True, help="The amount of the product to sell. Requires number.")

# Subparser report
report = subparsers.add_parser("report", help="Reports specific data. Please choose between 'inventory', 'sold', 'expires', 'revenue' or 'profit'.")
subparsers_report = report.add_subparsers(dest="command")

# Report inventory
inventory_parser = subparsers_report.add_parser("inventory", help="Reports products currently in inventory. Date arguments are '--today', '--yesterday' and '--date'.")
inventory_parser.add_argument("--today", action="store_true", help="Reports products in inventory today. No value needed.")
inventory_parser.add_argument("--yesterday", action="store_true", help="Reports products in inventory yesterday. No value needed.")
inventory_parser.add_argument("--date", type=validate_specific_date, help="Reports products in inventory from specific date. Data format is 'YYYY-MM-DD'.")

# Report sold
sold_parser = subparsers_report.add_parser("sold", help="Reports products that are sold. Date arguments are '--today', '--yesterday', '--date', 'start_date' and '--end_date'.")
sold_parser.add_argument("--today", action="store_true", help="Reports products sold today. No value needed.")
sold_parser.add_argument("--yesterday", action="store_true", help="Reports products sold yesterday. No value needed.")
sold_parser.add_argument("--date", type=validate_date, help="Reports products sold from specific date(s). Data format is 'YYYY-MM-DD', 'YYYY-MM' or 'YYYY'.")
sold_parser.add_argument("--start_date", type=validate_specific_date, help="Start of products sold report range. Data format is 'YYYY-MM-DD'.")
sold_parser.add_argument("--end_date", type=validate_specific_date, help="End of products sold range. Data format is 'YYYY-MM-DD'.")

# Report expired
expires_parser = subparsers_report.add_parser("expires", help="Reports products that are expired. "
"Date arguments are '--today', '--yesterday', '--date', 'start_date', '--end_date', '--tomorrow' and '--within_one_week'.")
expires_parser.add_argument("--today", action="store_true", help="Reports products expired today. No value needed.")
expires_parser.add_argument("--yesterday", action="store_true", help="Reports products expired yesterday. No value needed.")
expires_parser.add_argument("--date", type=validate_date, help="Reports products expired from specific date(s). Data format is 'YYYY-MM-DD', 'YYYY-MM' or 'YYYY'.")
expires_parser.add_argument("--start_date", type=validate_specific_date, help="Start of products expired report range. Data format is 'YYYY-MM-DD'.")
expires_parser.add_argument("--end_date", type=validate_specific_date, help="End of products expired range. Data format is 'YYYY-MM-DD'.")
expires_parser.add_argument("--tomorrow", action="store_true", help="Reports products expiring tomorrow. No value needed.")
expires_parser.add_argument("--within_one_week", action="store_true", help="Reports products expiring within one week. No value needed.")

# Report revenue
revenue_parser = subparsers_report.add_parser("revenue", help="Reports revenue. Date arguments are '--today', '--yesterday', '--date', '--start_date' and '--end_date'.")
revenue_parser.add_argument("--today", action="store_true", help="Reports revenue from today. No value needed.")
revenue_parser.add_argument("--yesterday", action="store_true", help="Reports revenue from yesterday. No value needed.")
revenue_parser.add_argument("--date", type=validate_date, help="Reports revenue from specific date(s). Data formats are 'YYYY-MM-DD', 'YYYY-MM' and 'YYYY'.")
revenue_parser.add_argument("--start_date", type=validate_specific_date, help="Start of revenue report range. Data format is 'YYYY-MM-DD'.")
revenue_parser.add_argument("--end_date", type=validate_specific_date, help="End of revenue report range. Data format is 'YYYY-MM-DD'.")

# Report profit
profit_parser = subparsers_report.add_parser("profit", help="Reports profit. Date arguments are '--today', '--yesterday', '--date', '--start_date' and '--end_date'.")
profit_parser.add_argument("--today", action="store_true", help="Reports profit from today. No value needed.")
profit_parser.add_argument("--yesterday", action="store_true", help="Reports profit from yesterday. No value needed.")
profit_parser.add_argument("--date", type=validate_date, help="Reports profit from specific date(s). Data formats are 'YYYY-MM-DD', 'YYYY-MM' and 'YYYY'.")
profit_parser.add_argument("--start_date", type=validate_specific_date, help="Start of profit report range. Data format is 'YYYY-MM-DD'.")
profit_parser.add_argument("--end_date", type=validate_specific_date, help="End of profit report range. Data format is 'YYYY-MM-DD'.")

# Parse args
args = parser.parse_args()

# Change date
if args.advance_time:
    with open("date.txt", "w") as txt_file:
        txt_file.write(str(date.today() + timedelta(args.advance_time)))
    print("OK")
if args.reverse_time:
    with open("date.txt", "w") as txt_file:
        txt_file.write(str(date.today() - timedelta(args.reverse_time)))
    print("OK")
if args.correct_time:
    with open("date.txt", "w") as txt_file:
        txt_file.write(str(date.today()))
    print("OK")

# Open date txt
with open("date.txt", "r") as txt_file:
    time = txt_file.read()

# Date vars
todays_date = datetime.strptime(time, "%Y-%m-%d").date()
yesterdays_date = todays_date - timedelta(1)
tomorrow_date = todays_date + timedelta(1)
one_week = todays_date + timedelta(7)

# Calls buy product function
if args.command == "buy":
    buy_product(args.product_name,args.price,args.expiration_date,args.amount,todays_date)

# Calls sell product function
if args.command == "sell":
    if args.expiration_date < todays_date:
        print("ERROR: Can't sell expired products!")
    else:
        sell_product(args.product_name,args.price,args.expiration_date,args.amount,todays_date)

# Calls inventory functions based on selected dates
if args.command == "inventory":
    if args.today:
        inventory_today(todays_date)
    if args.yesterday:
        inventory_yesterday(yesterdays_date)
    if args.date:
        inventory_date(args.date)

# Calls sold functions based on selected dates
if args.command == "sold":
    if args.today:
        sold_today(todays_date)
    if args.yesterday:
        sold_yesterday(yesterdays_date)
    if args.date:
        sold_date(args.date)
    if args.start_date and args.end_date:
        if args.start_date < args.end_date:
            sold_between_start_and_end(args.start_date,args.end_date)
        else:
            print("'end_date' should be a later date than 'start_date'")
    elif args.start_date:
        sold_after_start(args.start_date)
    elif args.end_date:
        sold_before_end(args.end_date)

# Calls expired functions based on selected dates
if args.command == "expires":
    if args.today:
        expires_today(todays_date)
    if args.yesterday:
        expires_yesterday(yesterdays_date)
    if args.date:
        expires_date(args.date)
    if args.start_date and args.end_date:
        if args.start_date < args.end_date:
            expires_between_start_and_end(args.start_date,args.end_date)
        else:
            print("'end_date' should be a later date than 'start_date'")
    elif args.start_date:
        expires_after_start(args.start_date)
    elif args.end_date:
        expires_before_end(args.end_date)
    if args.tomorrow:
        expires_tomorrow(tomorrow_date)
    if args.within_one_week:
        expires_within_one_week(one_week,todays_date)

# Calls revenue functions based on selected dates
if args.command == "revenue":
    if args.today:
        revenue_today(todays_date)
    if args.yesterday:
        revenue_yesterday(yesterdays_date)
    if args.date:
        revenue_date(args.date)
    if args.start_date and args.end_date:
        if args.start_date < args.end_date:
            revenue_between_start_and_end(args.start_date,args.end_date)
        else: 
            print("'end_date' should be a later date than 'start_date'")
    elif args.start_date:
        revenue_after_start(args.start_date)
    elif args.end_date:
        revenue_before_end(args.end_date)
    
# Calls profit functions based on selected dates
if args.command == "profit":
    if args.today:
        profit_today(todays_date)
    if args.yesterday:
        profit_yesterday(yesterdays_date)
    if args.date:
        profit_date(args.date)
    if args.start_date and args.end_date:
        if args.start_date < args.end_date:
            profit_between_start_and_end(args.start_date,args.end_date)
        else: 
            print("'end_date' should be a later date than 'start_date'")
    elif args.start_date:
        profit_after_start(args.start_date)
    elif args.end_date:
        profit_before_end(args.end_date)

if __name__ == "__main__":
    main()
