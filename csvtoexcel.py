import xlsxwriter
import argparse
import csv
import os
import sys


def main():
    parser = argparse.ArgumentParser(description='Convert CSV to Excel')
    parser.add_argument('input_path', type=str, help='The path to the CSV file')
    parser.add_argument('output_path', type=str, help='The path to the Excel file')
    args = parser.parse_args()

    try:
        with xlsxwriter.Workbook(args.output_path) as wb:
            ws = wb.add_worksheet()
            with open(args.input_path, "r") as f:
                reader = csv.reader(f)
                x = 0
                for line in reader:
                    for i in range(len(line)):
                        ws.write(x, i, line[i])
                    x += 1

    except Exception as e:
        print(e)
        if not os.path.exists(args.output_path):
            pass
        else:
            os.remove(args.output_path)
        sys.exit()


if __name__ == '__main__':
    main()
