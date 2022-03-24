import csv
from math import log10 as log


def calculate_fwbr(CBO, DIT, WMC, RFC, LCOM, NOC):
    return -1 * (8.753 * log(CBO + 1) + 2.505 * log(DIT + 1)
                 - 1.922 * log(WMC + 1) + 0.892 * log(RFC + 1)
                 - 0.399 * log(LCOM + 1) - 1.080 * log(NOC + 1))


def calculate_fwbr_s(CBO, DIT, WMC, RFC, LCOM, NOC):
    return -1 * (5.810 * log(CBO + 1) + 3.112 * log(DIT + 1)
                 + 0.067 * log(WMC + 1) - 1.012 * log(RFC + 1)
                 - 0.041 * log(LCOM + 1) - 0.132 * log(NOC + 1))


def calculate_fwbr_n(CBO, DIT, WMC, RFC, LCOM, NOC):
    return -1 * (9.023 * log(CBO + 1) + 3.945 * log(DIT + 1)
                 - 0.678 * log(WMC + 1) - 0.826 * log(RFC + 1)
                 - 0.378 * log(LCOM + 1))


def calculate_fwbr_l(CBO, DIT, WMC, RFC, LCOM, NOC):
    return -1 * (8.151 * log(CBO + 1) + 1.431 * log(DIT + 1)
                 - 2.788 * log(WMC + 1) + 2.501 * log(RFC + 1)
                 - 0.191 * log(LCOM + 1) - 1.242 * log(NOC + 1))


with open('versions.csv') as f:
    csv_reader = csv.DictReader(f)

    for row in csv_reader:
        version = row['version']
        lib_directory = row['libdirectory']
        jar_path = row['jarpath']

        print(f'\n\nVersion: {version}')

        # First count the number of classes
        with open(f'./ck-metrics/ck-metrics-{version}.csv') as ck_f:
            number_of_classes = sum(1 for class_line in ck_f) - 1

        with open(f'./ck-metrics/ck-metrics-{version}.csv') as ck_f:
            ck_csv_reader = csv.DictReader(ck_f)

            with open(f'./fwbr-metrics/fwbr-metrics-{version}.csv', 'w') as o:
                o.write('ClassName, fwbr, fwbr_sub_type, fwbr_sub\n')

                for ck_row in ck_csv_reader:
                    class_name = ck_row['ClassName']
                    CBO = int(ck_row['CBO'])
                    DIT = int(ck_row['DIT'])
                    WMC = int(ck_row['WMC'])
                    RFC = int(ck_row['RFC'])
                    LCOM = int(ck_row['LCOM'])
                    NOC = int(ck_row['NOC'])

                    o.write(
                        f'{class_name}, {calculate_fwbr(CBO, DIT, WMC, RFC, LCOM, NOC)}, ')

                    if number_of_classes <= 500:
                        o.write(
                            f's, {calculate_fwbr_s(CBO, DIT, WMC, RFC, LCOM, NOC)}\n')
                    elif number_of_classes <= 1499:
                        o.write(
                            f'n, {calculate_fwbr_n(CBO, DIT, WMC, RFC, LCOM, NOC)}\n')
                    else:
                        o.write(
                            f'l, {calculate_fwbr_l(CBO, DIT, WMC, RFC, LCOM, NOC)}\n')
