import csv
import os

csvpath = os.path.join('election_data.csv')

csvpath = os.path.join('election_data.csv')
output_txt = os.path.join("PyRoll_output.txt")

id = []
county = []
candidate = []

i = 0
total_votes = 0
candidate1 = 0
candidate2 = 0
candidate3 = 0
candidate4 = 0

with open(csvpath) as csvfile:
    csv_pyroll = csv.reader(csvfile, delimiter=',')
    header = next(csv_pyroll)

    for row in csv_pyroll:
        if row[2] not in candidate:
            candidate.append(row[2])
        i += 1

    total_votes = i
    set_candidate = set(candidate)

with open(csvpath) as csvfile:
    csv_pyroll = csv.reader(csvfile, delimiter=',')
    header = next(csv_pyroll)

    for row in csv_pyroll:
        if row[2] == list(set_candidate)[0]:
            candidate1 += 1
        elif row[2] == list(set_candidate)[1]:
            candidate2 += 1
        elif row[2] == list(set_candidate)[2]:
            candidate3 += 1
        elif row[2] == list(set_candidate)[3]:
            candidate4 += 1

    if (candidate1 > candidate2) and (candidate1 > candidate3) and (candidate1 > candidate4):
        winner = list(set_candidate)[0]
    elif (candidate2 > candidate3) and (candidate2 > candidate4):
        winner = list(set_candidate)[1]
    elif (candidate3 > candidate4):
        winner = list(set_candidate)[2]
    else:
        winner = list(set_candidate)[3]

    print("Election Results")
    print('---------------------')
    print(f'Total Votes: {total_votes}')
    print('---------------------')
    print(f'{list(set_candidate)[0]}: {candidate1 / total_votes:.3%} ({candidate1})')
    print(f'{list(set_candidate)[1]}: {candidate2 / total_votes:.3%} ({candidate2})')
    print(f'{list(set_candidate)[2]}: {candidate3 / total_votes:.3%} ({candidate3})')
    print(f'{list(set_candidate)[3]}: {candidate4 / total_votes:.3%} ({candidate4})')
    print('---------------------')
    print(f'Winner: {winner}')

with open(output_txt, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write('---------------------\n')
    txtfile.write(f'Total Votes: {total_votes}\n')
    txtfile.write('---------------------\n')
    txtfile.write(f'{list(set_candidate)[0]}: {candidate1 / total_votes:.3%} ({candidate1})\n')
    txtfile.write(f'{list(set_candidate)[1]}: {candidate2 / total_votes:.3%} ({candidate2})\n')
    txtfile.write(f'{list(set_candidate)[2]}: {candidate3 / total_votes:.3%} ({candidate3})\n')
    txtfile.write(f'{list(set_candidate)[3]}: {candidate4 / total_votes:.3%} ({candidate4})\n')
    txtfile.write('---------------------\n')
    txtfile.write(f'Winner: {winner}\n')