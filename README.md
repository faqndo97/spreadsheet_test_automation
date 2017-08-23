# Spreadsheet test automation

*La idea de este script es poder automatizar los test que listamos en hojas de calculo y luego corremos a mano. Dicha hoja de calculo debe tener un formato esperado que aclararemos mas abajo. Cuando se corra el script se deben especificar la cantidad de test a correr asi como el archivo de input (**que debe tener un formato .tsv**) y el archivo de output (**que debe tener un formato .html**, si dicho archivo que definimos para el output no existe, lo crea dentro de la carpeta del proyecto).*

## Spreadsheet Format:

![example](http://i.imgur.com/JNRdMTM.png)

*El formato esperado en el script coincide con este formato. La idea es que la hoja de calculo que armemos tenga este formato y luego la descarguemos como un **.tsv**. Podemos observar que en la url tenemos un **[URL]** todo este valor se cambia por la url que ingresamos cuando corremos el script. Los headers se deben de ingresar como los mostramos en el ejemplo y separados por coma.*

## Local setup:

1. Instalar [python](https://www.python.org/downloads/release/python-2710/) (2.7.10 if possible)

2. Instalar las dependencias: **requests**, **jinja2**, **progress**

		$ sudo pip install requests jinja2 progress
		
3. Descargar dentro de la carpeta del proyecto la hoja de calculos en el formato **.tsv**

4. Ir al proyecto y correr el script

		$ python spreadsheet_test_automation.py file.tsv out.html https://domain.com quantityOfTests


## Doubts, problems
- facundo.espinosa@mercadolibre.com
