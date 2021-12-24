import csv
import pandas as pd
from collections import Counter

def getmean(total_weight, total_entries):
    mean = total_weight/total_entries
    print(f"Mean is {mean:2f}")

def getmedian(total_entries, sorted_data):
    if total_entries % 2 == 0:
        median1 = float(sorted_data[total_entries//2])
        median2 = float(sorted_data[total_entries//2 - 1])
        median = (median1+median2)/2
    else:
        median = float(sorted_data[total_entries//2])
    print(f"Median is {median:2f}")

def getmode(sorted_data):
    data = Counter(sorted_data)
    mode_data_range = {
        "75-85": 0,
        "85-95": 0,
        "95-105": 0,
        "105-115": 0,
        "115-125": 0,
        "125-135": 0,
        "135-145": 0,
        "145-155": 0,
        "155-165": 0,
        "165-175": 0,
    }
    for weight, occurance in data.items():
        if 75 < weight < 85:
            mode_data_range["75-85"]+=occurance
        elif 85 < weight <95:
            mode_data_range["85-95"]+=occurance
        elif 95 < weight <105:
            mode_data_range["95-105"]+=occurance
        elif 105 < weight <115:
            mode_data_range["105-115"]+=occurance
        elif 115 < weight <125:
            mode_data_range["115-125"]+=occurance
        elif 125 < weight <135:
            mode_data_range["125-135"]+=occurance
        elif 135 < weight <145:
            mode_data_range["135-145"]+=occurance
        elif 145 < weight <155:
            mode_data_range["145-155"]+=occurance
        elif 155 < weight <165:
            mode_data_range["155-165"]+=occurance
        elif 165 < weight <175:
            mode_data_range["165-175"]+=occurance
        mode_range, mode_occurance = 0,0
        for range, occurance in mode_data_range.items():
            if occurance > mode_occurance:
                mode_range, mode_occurance = [int (range.split("-")[0]), int (range.split("-")[1])], occurance
        mode = float((mode_range[0]+mode_range[1])/2)
        print(f"Mode is {mode:2f}")

with open("pro104.csv", newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

total_weight = 0
total_entries = len(file_data)
sorted_data = []
for person_data in file_data:
    total_weight += float(person_data[2])
    sorted_data.append(float(person_data[2]))
sorted_data.sort()

getmean(total_weight, total_entries)
getmedian(total_entries, sorted_data)
getmode(sorted_data)