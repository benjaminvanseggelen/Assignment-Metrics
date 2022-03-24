import csv

with open('versions.csv') as f:
    csv_reader = csv.DictReader(f)

    for row in csv_reader:
        version = row['version']
        lib_directory = row['libdirectory']
        jar_path = row['jarpath']

        print(f'\nVersion: {version}')

        with open(f'./fwbr-metrics/fwbr-metrics-{version}.csv') as fwbr_f:
            fwbr_csv_reader = csv.DictReader(fwbr_f)

            fwbr_differences = []
            fwbr_higher = []

            for row in fwbr_csv_reader:
                fwbr = float(row['fwbr'])
                fwbr_sub = float(row['fwbr_sub'])
                fwbr_differences.append(abs(fwbr - fwbr_sub))

                fwbr_higher.append(True if fwbr > fwbr_sub else False)

            avg_difference = sum(fwbr_differences) / len(fwbr_differences)

            print(f'Average difference: {avg_difference}')

            avg_higher = sum(1 for x in fwbr_higher if x ==
                             True) / len(fwbr_higher)

            print(
                f'FWBR is higher than FWBR-sub metric {avg_higher * 100}% of the time')
