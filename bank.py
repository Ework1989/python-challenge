import os
import csv

budget_data_path = os.path.join(".", "Resources", "budget_data.csv")

# Open the CSV file
with open(budget_data_path, newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # The total number of months included in the dataset (row count after the header)
    next(csvreader)
    data = list(csvreader)
    row_count = len(data)

    # The net total amount of "Profit/Losses" over the entire period
    total = sum(int(row[1]) for row in data)

    # The average of the changes in "Profit/Losses" over the entire period
    diff_list = [int(data[i][1]) - int(data[i - 1][1]) for i in range(1, row_count)]
    avg_change = round(sum(diff_list) / len(diff_list), 2)

    # The greatest increase in profits (date and amount) over the entire period
    max_diff = max(diff_list)
    max_diff_pos = diff_list.index(max_diff) + 1

    # The greatest decrease in losses (date and amount) over the entire period
    min_diff = min(diff_list)
    min_diff_pos = diff_list.index(min_diff) + 1

    # Print the results to the terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {row_count}")
    print(f"Total: ${total:,}")
    print(f"Average Change: ${avg_change:,}")
    print(f"Greatest Increase in Profits: {data[max_diff_pos][0]} (${max_diff:,})")
    print(f"Greatest Decrease in Profits: {data[min_diff_pos][0]} (${min_diff:,})")

    # Print the results to "PyBank.txt" file
    with open("PyBank.txt", "a") as output_file:
        print("Financial Analysis", file=output_file)
        print("----------------------------", file=output_file)
        print(f"Total Months: {row_count}", file=output_file)
        print(f"Total: ${total:,}", file=output_file)
        print(f"Average Change: ${avg_change:,}", file=output_file)
        print(f"Greatest Increase in Profits: {data[max_diff_pos][0]} (${max_diff:,})", file=output_file)
        print(f"Greatest Decrease in Profits: {data[min_diff_pos][0]} (${min_diff:,})", file=output_file)
