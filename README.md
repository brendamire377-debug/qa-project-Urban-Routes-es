# Proyecto Urban.Routes 

## Descripción del proyecto

El proyecto consiste en la automatización de 8 pruebas que verifican la funcionalidad del proceso de pedir un taxi en la aplicación Urban.Routes. El proceso incluye pruebas de las siguientes funciones:
* Ingresar la ruta
* Seleccionar el  tipo de tarifa
* Ingresar un número teléfónico y un código de confirmación
* Ingresar el método de pago (tarjeta)
* Enviar un mensaje para el conductor
* Añadir productos extra a la solicitud
* Confirmar la solicitud del taxi


## Tecnologías utilizadas

* Python
* Selenium WebDriver
* Pytest
* Page Object Model

## Estructura del proyecto

Project/

→data/

→pages/

→test/

→utils/

  README .md

## Archivos y clases principales
* *data.py*  Este archivo contiene los datos para ejecutar algunos métodos de las pruebas.


* *urban_routes_pages.py* Dentro de este archivo está la clase *UrbanRoutesPage* que contiene los localizadores de todos los elementos de la aplicación que fueron usados para las pruebas.La clase *UrbanRoutesPage* contiene también los métodos para  obtener los elementos y realizar una determinada acción sobre ellos (hacer click, escribir texto, seleccionar el elemento). Finalmente, en esta clase están los métodos para obtener los valores necesarios para evaluar cada prueba.


* *test_urban_routes.py*  Este archivo contiene la clase *TestUrbanRoutes* que incluye de manera ordenada, cada una de las pruebas con sus respectivos métodos.Contiene tambien el método *setup_method*,cuya función es preparar el entorno, aquí se realizan acciones como crear el controlador con webdriver, este caso se hizo con el navegador Chrome, en esta parte se hace la conexión con la URL de la página de Urban Routes.


* *retrive_code.py* Este archivo contiene un método que devuelve como string un número de confirmación de teléfono utilizado en la prueba número 3.

## Instalación y ejecución
* Necesitas tener instalado pytest y selenium para ejecutar las pruebas.
* Ejecuta todas las pruebas con el comando pytest

## Autor
Brenda Mireya Cisneros Cruz
