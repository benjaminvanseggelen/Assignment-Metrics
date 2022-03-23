import csv
import subprocess

with open('versions.csv') as f:
    csv_reader = csv.reader(f)
    csv_rows = iter(csv_reader)
    next(csv_rows) # Skip header row

    for row in csv_rows:
        version = row[0]
        lib_directory = row[1]
        jar_path = row[2]

        print(f'\n\nVersion: {version}\n Library directoy: {lib_directory}\n JAR path: {jar_path}')

        if lib_directory:
            # To skip 5.5.13.3
            with open(f'./ck-metrics/ck-metrics-{version}.csv', 'w') as o:
                subprocess.run(['java', '-jar', 'ckjm_adapted.jar', '.'+jar_path, '.'+lib_directory], stdout=o)
        
        with open(f'./le-metrics/le-metrics-{version}.csv', 'w') as o:
            subprocess.run(['java', '-jar', 'layer_extractor.jar', '.'+jar_path], stdout=o)
