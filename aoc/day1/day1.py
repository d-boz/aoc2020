from aoc.helpers import io
                
expense_report = []
def add_to_expense_report(line):
    try:
        expense_item = int(line)
        expense_report.append(expense_item)
    except ValueError:
        return

read_file_by_newline("day1.txt", add_to_expense_report)

# Calculate 2020 add & sum brute force O^2
break_flag = False
for i in range(0, len(expense_report)):
    for j in range(i, len(expense_report)):
        if expense_report[i] + expense_report[j] == 2020:
            print("Answer: {}".format(expense_report[i]* expense_report[j]))
            break_flag = True
            break
    if break_flag:
        break
print("Finished...")