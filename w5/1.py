import re

with open('raw.txt', 'r', encoding='utf-8') as f:
    all_lines = ''.join(f.readlines())

company_name = re.search(r'ДУБЛИКАТ\n(.+)\n', all_lines).group(1)
bin_number = re.search(r'БИН (\d+)', all_lines).group(1)

items = re.findall(r'\d+\.\n([^\n]+)\n([0-9, ]+) x ([0-9, ]+)\n([0-9, ]+)', all_lines)
                    #num. nl  name  nl quantity  x    cost   nl   sum

date = re.search(r'\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2}', all_lines).group(0)
address = re.search(r'г\.[^\n]+', all_lines).group(0)
overall_cost = re.search(r'ИТОГО:\n([0-9, ]+)', all_lines).group(1)

print(f'Company name: {company_name}')
print(f'BIN number: {bin_number}')
print(f'Date: {date}')
print(f'Address: {address}')
print()

def prettify(s):
    s = s.replace(' ', '')
    s = s.replace(',', '.')
    return float(s)

check_sum = 0
for index, item in enumerate(items):
    print(f'{index + 1}) {item[0]}')
    print(f'\t{item[1]} * {item[2]} = {item[3]}')
    check_sum += prettify(item[3])

print(f'Overall sum from check: {overall_cost}')
print(f'Our sum: {check_sum}')


############ CSV ############

import csv

# Russian windows features
csv.excel.delimiter = ';'
csv.excel.lineterminator = '\n'

# Writing to csv file
with open('1.csv', 'w', encoding='cp1251') as f:
    writer = csv.writer(f, csv.excel)
    writer.writerow([company_name])
    writer.writerow([f'BIN number: {bin_number}'])
    writer.writerow([f'Date: {date}', f'Address: {address}'])
    writer.writerows([('Name', 'Quantity', 'Price', 'Sum')] + items)

# Reading from csv
with open('1.csv', 'r', encoding='cp1251') as f:
    for line in csv.reader(f, csv.excel):
        print(line)
    
