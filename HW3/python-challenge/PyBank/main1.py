import csv
import os

csvpath = os.path.join('budget_data.csv')
#output_csv = os.path.join("PyBank_output.csv")
output_txt = os.path.join("PyBank_output.txt")

num_months = 0
sum_profit = 0
avg_profit = 0
month = []
profit = []
MoM_change = []
MoM_change.append(0)

i = 0

with open(csvpath) as csvfile:
    csv_pybank = csv.reader(csvfile, delimiter=',')
    header = next(csv_pybank)

    for row in csv_pybank:

        month.append(row[0])
        profit.append(row[1])
        sum_profit += int(profit[i])

        i += 1

    #for x in range(0, len(month) - 1):
        #MoM_change.append(int(profit[x + 1]) - int(profit[x]))
        #x += 1

    for i, x in enumerate(month[:-1],1):
        MoM_change.append(int(profit[i])-int(profit[i-1]))

    avg_profit = sum(MoM_change) / (len(month)-1)
    max_profit = max(MoM_change)
    min_profit = min(MoM_change)
    max_month = MoM_change.index(max_profit)
    min_month = MoM_change.index(min_profit)

    print(f'Total Months: {len(month)}')
    print(f'Total: ${sum_profit}')
    print(f'Average Change: ${avg_profit}')
    print(f'Greatest increase in profits: {month[max_month]} (${max_profit})')
    print(f'Greatest decrease in profits: {month[min_month]} (${min_profit})')

#cleaned_csv = list(zip(month,profit,MoM_change))

#with open(output_csv, 'w') as csvfile:
    #csvwriter = csv.writer(csvfile, delimiter=',')
    #csvwriter.writerows(cleaned_csv)
    #for row in cleaned_csv:
       #csvwriter.writerow(row)

with open(output_txt, 'w') as txtfile:
    txtfile.write(f'Total Months: {len(month)}\n')
    txtfile.write(f'Total: ${sum_profit}\n')
    txtfile.write(f'Average Change: ${avg_profit}\n')
    txtfile.write(f'Greatest increase in profits: {month[max_month]} (${max_profit})\n')
    txtfile.write(f'Greatest decrease in profits: {month[min_month]} ${min_profit}\n')