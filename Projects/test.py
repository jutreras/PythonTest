import sys
import requests
sys.path.append('C:\Python34\Projects\Librerias')
import func
rut = '14.300.052-4'



if func.validaRut(rut):
    print('Verdadero')
else:
    print ('Falso')
