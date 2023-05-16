This is a report of technical elements of my implementation I found notable while working on this program and why I chose to implement it in a certain way.

### TECHNICAL ELEMENT 1

Something I wanted to work on quite early on was being able to sell an amount of a product with a number.
This wasn't much of an issue, until I wanted to be able to sell everything in one command when two or more identical products rows in bought.csv had been bought.
My solution to this was to make a list of the row that had been completely sold, and iterate the next viable row until the amount selling had been depleted.

For example:

```
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
```

With the list I was able to add everything once the selling amount hit 0, and add nothing at all when the selling amount never hit 0.

### TECHNICAL ELEMENT 2

With 'sold', 'expires', 'revenue' and 'profit' I wanted to have the additional date formats 'YYYY-MM' and 'YYYY' working on the same '--date' argument.
To do this, I used the 'try' and 'except' method inside of the 'validate_date' function when parsing the date argument.
Then turning the datetime format to a string so that in the called function it would only receive the year and month or year to work with.

For example:

```
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
```

The called function has the same 'try' and 'except' method as 'validate_date' and will function accordingly to the chosen data format.

### TECHNICAL ELEMENT 3

After adding the extra 'between_start_and_end' argument, I wanted to also report data using only '--start_date' or '--end_date' instead of both.
To do this, I first experimented with a dud and a min/max date, however I found it becoming unorginized.
So I decided to just make a seperate function which is called when only one of the two date arguments are given.
The new 'after_start' and 'before_end' functions only take one 'if' statement when iterating through the data report.

For example:

```
if expired_date >= start_date:
```

and

```
if expired_date <= end_date:
```

instead of

```
if expired_date >= start_date and expired_date <= end_date:
```

Now when only the '--start_date' is given, it will report everthing after that or on that date.
And when only the '--end_date' argument is given, it will report everything before or on that date.
