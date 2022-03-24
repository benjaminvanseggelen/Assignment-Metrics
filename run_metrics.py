import csv
import subprocess

with open('versions.csv') as f:
    csv_reader = csv.DictReader(f)

    for row in csv_reader:
        version = row['version']
        lib_directory = row['libdirectory']
        jar_path = row['jarpath']

        print(
            f'\n\nVersion: {version}\n Library directoy: {lib_directory}\n JAR path: {jar_path}')

        if lib_directory:
            # To skip 5.5.13.3
            with open(f'./ck-metrics/ck-metrics-{version}.csv', 'w') as o:
                subprocess.run(['java', '-jar', 'ckjm_adapted.jar',
                               '.'+jar_path, '.'+lib_directory], stdout=o)

        with open(f'./le-metrics/le-metrics-{version}.csv', 'w') as o:
            subprocess.run(
                ['java', '-jar', 'layer_extractor.jar', '.'+jar_path], stdout=o)
