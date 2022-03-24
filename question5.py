import csv

with open('versions.csv') as f:
    versions = list(csv.DictReader(f))

    for i, row in enumerate(versions):
        if i == 0:
            continue

        version = row['version']
        lib_directory = row['libdirectory']
        jar_path = row['jarpath']

        print(
            f'\nVersion {version} compared to version {versions[i-1]["version"]}')

        with open(f'./fwbr-metrics/fwbr-metrics-{version}.csv') as fwbr_f:
            fwbr_rows = list(csv.DictReader(fwbr_f))
            sorted_fwbr_rows = sorted(fwbr_rows, key=lambda x: x['ClassName'])

        with open(f'./fwbr-metrics/fwbr-metrics-{versions[i-1]["version"]}.csv') as fwbr_f_old:
            fwbr_rows_old = list(csv.DictReader(fwbr_f_old))
            sorted_fwbr_rows_old = sorted(
                fwbr_rows_old, key=lambda x: x['ClassName'])

        number_of_changed_classes = 0

        for row_old in sorted_fwbr_rows_old:
            row_new = next(
                (row for row in sorted_fwbr_rows if row['ClassName'] == row_old['ClassName']), None)

            if row_new:
                # Class exists in both versions
                fwbr_old = row_old['fwbr']
                fwbr_new = row_new['fwbr']

                if fwbr_old != fwbr_new:
                    # FWBR value changed
                    number_of_changed_classes += 1

        print(f'Number of changed classes: {number_of_changed_classes}')
