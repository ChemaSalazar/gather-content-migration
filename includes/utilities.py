import json
import csv


def esc(code):
    return f'\033[{code}m'


def progress(percent=0, width=30):
    left = width * percent // 100
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']',
          f' {percent:.0f}%',
          sep='', end='', flush=True)


def json_to_csv(path_to_json_file, output_file_path):
    with open(path_to_json_file) as json_file:
        data = json.load(json_file)
        main_key = list(data.keys())[0]

    entries = data[main_key]

    # now we will open a file for writing
    data_file = open(output_file_path, 'w')

    # create the csv writer object
    csv_writer = csv.writer(data_file)

    # Counter variable used for writing
    # headers to the CSV file
    count = 0

    for data in entries:
        if count == 0:
            # Writing headers of CSV file
            header = data.keys()
            csv_writer.writerow(header)
            count += 1

        # Writing data of CSV file
        csv_writer.writerow(data.values())

    data_file.close()
