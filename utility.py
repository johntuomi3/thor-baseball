import os
import sys
import csv
import psycopg2
import pandas
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:Portage2!@localhost/mlb")

def main():
    initialize()


def initialize():
    csv_file_list = getCSVFiles()
    parseCSV(csv_file_list)


def getCSVFiles():
    csv_file_list = []
    for dirs, subdirs, files, in os.walk("res\\"):
       for file in files:
           if file.split(".")[1] == 'csv':
               csv_file_path = os.path.join(dirs, file)
               if csv_file_path not in csv_file_list:
                   csv_file_list.append(csv_file_path)
    return csv_file_list


def parseCSV(csv_file_list):
    for csv_file_path in csv_file_list:
        csv_file = open(csv_file_path, 'r')
        reader = csv.DictReader(csv_file)        
        for i in reader:
            print(i)



if __name__ == "__main__":
    main()