import csv

countries_filename = 'country_info.txt'
with open(countries_filename, encoding='utf-8', newline="") as countries_file:
    # Take sample from csv file
    sample = ""
    for row in range(3):
        sample += countries_file.readline()

    # Sniff sample to get dialect
    dialect = csv.Sniffer().sniff(sample)

    # Move back to start of the file
    countries_file.seek(0)

    # Read as dict
    country_reader = csv.DictReader(countries_file, dialect=dialect)
    for country in country_reader:
        print(country)

