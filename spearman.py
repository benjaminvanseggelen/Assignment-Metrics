import csv
from scipy.stats import spearmanr

with open('versions.csv') as f:
    csv_reader = csv.DictReader(f)

    for row in csv_reader:
        version = row['version']
        lib_directory = row['libdirectory']
        jar_path = row['jarpath']

        print(f'\nVersion: {version}')

        with open(f'./fwbr-metrics/fwbr-metrics-{version}.csv') as fwbr_f:
            fwbr_csv_reader = csv.DictReader(fwbr_f)
            fwbr_values = [float(row['fwbr']) for row in fwbr_csv_reader]

        with open(f'./fwbr-metrics/fwbr-metrics-{version}.csv') as fwbr_f:
            fwbr_csv_reader = csv.DictReader(fwbr_f)
            fwbr_sub_values = [float(row['fwbr_sub'])
                               for row in fwbr_csv_reader]

        with open(f'./le-metrics/le-metrics-{version}.csv') as le_f:
            le_csv_reader = csv.DictReader(le_f)
            le_values = [float(row['layer']) for row in le_csv_reader]

        coefficient, p = spearmanr(le_values, fwbr_values)
        sub_coefficient, sub_p = spearmanr(le_values, fwbr_sub_values)

        print(f'For FWBR and layer:')
        print(f'  Spearman\'s coefficient: {coefficient}')
        print(f'  p-value: {p}')
        print(f'For FWBR sub-metric and layer:')
        print(f'  Spearman\'s coefficient: {sub_coefficient}')
        print(f'  p-value: {sub_p}\n')
