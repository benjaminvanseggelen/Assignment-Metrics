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

        with open(f'./le-metrics/le-metrics-{version}.csv') as le_f:
            le_rows = list(csv.DictReader(le_f))
            sorted_le_rows = sorted(le_rows, key=lambda x: x['ClassName'])

        with open(f'./le-metrics/le-metrics-{versions[i-1]["version"]}.csv') as le_f_old:
            le_rows_old = list(csv.DictReader(le_f_old))
            sorted_le_rows_old = sorted(
                le_rows_old, key=lambda x: x['ClassName'])

        number_of_changed_classes = 0

        for row_old in sorted_le_rows_old:
            row_new = next(
                (row for row in sorted_le_rows if row['ClassName'] == row_old['ClassName']), None)

            if row_new:
                # Class exists in both versions
                layer_old = row_old['layer']
                layer_new = row_new['layer']

                if layer_old != layer_new:
                    # FWBR value changed
                    number_of_changed_classes += 1
                    print(row_new['ClassName'], layer_old, layer_new)

        print(f'Number of changed classes: {number_of_changed_classes}')
