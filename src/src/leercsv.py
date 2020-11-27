#
import csv

#../ para regresar un path arriba

def leer_csv():
    path_archivo = "data/empleados.csv"

    with open(path_archivo) as csv_file:
        reader = csv.reader(csv_file)

        for linea in reader:
            print(linea)

def leer_csv_dict():
    path_archivo = "data/empleados.csv"
    with open(path_archivo) as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            print(row)

if __name__ == "__main__":

    leer_csv_dict()

