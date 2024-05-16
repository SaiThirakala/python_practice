import csv

input_filename = 'country_info.txt'

with open(input_filename, encoding='utf-8', newline='') as countries_data:
    # Take a sample of the csv file
    sample = ""
    for line in range(3):
        sample += countries_data.readline()
    # sample = countries_data.read()

    # Sniffer finds out the format of csv format based on sample
    country_dialect = csv.Sniffer().sniff(sample)
    country_dialect.skipinitialspace = True

    # Reset to start of the csv file
    countries_data.seek(0)

    # Read csv file based on dialect from sniffer
    country_reader = csv.reader(countries_data, dialect=country_dialect)
    for row in country_reader:
        print(row)

print("*" * 80)
attributes = ['delimiter',
              'doublequote',
              'escapechar',
              'lineterminator',
              'quotechar',
              'quoting',
              'skipinitialspace',
              ]

for attribute in attributes:
    print(f"{attribute}: {repr(getattr(country_dialect, attribute))}")
