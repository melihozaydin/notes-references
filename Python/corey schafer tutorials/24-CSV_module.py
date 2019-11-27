import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line[0:3])  # this can be indexed

# copy names.csv to a new csv file and change ',' default delimiter to '-'
# note that if a value has a '-' already program will save it
# in quotes so when we read it back it wont confuse the '-' for a delimiter
# you need to use define the correct delimiter while reading
#  if it's diffrent from the default (',')
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='-')

        for line in csv_reader:
            csv_writer.writerow(line)

print('\n Dictionary Reader \n')

# preferred method of working with csv data
# dictionary reader/writer

# this formats the csv so you can work on it like a dict

# dict reader
with open('names.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line)
        print(line['email'], line['last_name'], '\n')

# dict writer
with open('names.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('dict_names.csv', 'w') as dict_file:
        field_names = ['first_name', 'last_name', 'email']

        csv_writer = csv.DictWriter(dict_file, fieldnames=field_names, delimiter='\t')

        csv_writer.writeheader()  # write fieldnames as first line

        for line in csv_reader:
            # This would delete the emails
            # del line['email']
            csv_writer.writerow(line)
