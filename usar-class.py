from csv_class import CsvProcessor

arquivo_csv = './exemplo.csv'

filtro = 'estado'
limite = 'SP'

arquivo_csv = CsvProcessor(arquivo_csv)
arquivo_csv.carregar_csv()
print(arquivo_csv.filtrar(['estado', 'preço'],['SP', '10,50']))
#print(arquivo_csv.filtrar(filtro, limite))
#print(arquivo_csv.sub_filtro('preço', '10,50'))