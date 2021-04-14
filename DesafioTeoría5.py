import csv
import collections

archivo_csv = open('netflix_titles.csv', "r", encoding="utf8")
csvreader = csv.reader(archivo_csv, delimiter=',')

archivo_csv_nuevo = open('nuevo_netflix_titles.csv', "w", encoding="utf8")
csvwriter = csv.writer(archivo_csv_nuevo)

released_2020 = filter(lambda x : x[7] == '2020', csvreader)

csvwriter.writerow(next(csvreader))
csvwriter.writerows(released_2020)

archivo_csv.seek(0)
cinco_paises_mas_producciones = collections.Counter(list(map(lambda x : x[5], csvreader))).most_common(5)

print('Cinco paises con mas producciones en Netflix: ')
for elem in cinco_paises_mas_producciones:
    print('Pais: ' + elem[0] + ' - Cantidad de producciones: ' + str(elem[1]))