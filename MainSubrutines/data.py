import pandas as pd
from sodapy import Socrata

columnas = {"Ciudad_ubi": 'ciudad_municipio_nom',
         'Departamento': 'departamento_nom',
         'Edad': 'edad',
         'Sexo': 'sexo',
         'Estado': 'estado',
         'Pais_procedencia': 'pais_viajo_1_nom'}

def getData(limite_registros, nombre_departamento):
    client = Socrata('www.datos.gov.co', None)
    results = client.get('gt2j-8ykr', limit=limite_registros, departamento_nom=nombre_departamento)
    results_df = pd.DataFrame.from_records(results, columns = [columnas['Ciudad_ubi'],
                                                                columnas['Departamento'],
                                                                columnas['Edad'],
                                                                columnas['Sexo'],
                                                                columnas['Estado'],
                                                                columnas['Pais_procedencia']])

    return results_df
