import csv
from math import log10 as log

def calculate_fwbr(CBO, DIT, WMC, RFC, LCOM, NOC):
    return -1 * (8.753 * log(CBO + 1) + 2.505 * log(DIT + 1) 
    - 1.922 * log(WMC + 1) + 0.892 * log(RFC + 1) 
    - 0.399 * log(LCOM + 1) - 1.080 * log(NOC + 1))

with open('versions.csv') as f:
    csv_reader = csv.DictReader(f)

    for row in csv_reader:
        version = row['version']
        lib_directory = row['libdirectory']
        jar_path = row['jarpath']

        print(f'\n\nVersion: {version}')

        with open(f'./ck-metrics/ck-metrics-{version}.csv') as ck_f:
            ck_csv_reader = csv.DictReader(ck_f)
            
            with open(f'./fwbr-metrics/fwbr-metrics-{version}.csv', 'w') as o:
                o.write('ClassName, fwbr\n')

                for ck_row in ck_csv_reader:
                    class_name = ck_row['ClassName']
                    CBO = int(ck_row['CBO'])
                    DIT = int(ck_row['DIT'])
                    WMC = int(ck_row['WMC'])
                    RFC = int(ck_row['RFC'])
                    LCOM = int(ck_row['LCOM'])
                    NOC = int(ck_row['NOC'])
                    
                    o.write(f'{class_name}, {calculate_fwbr(CBO, DIT, WMC, RFC, LCOM, NOC)}\n')
