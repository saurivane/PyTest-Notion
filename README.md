# ***Integración PyTest en Notion Automáticamente***

---
## 1. Configuración.
---

Script para automatizar la salida de test con ***PyTest*** y llevar el resultado a una database en ***Notion***.

[notion-client]:https://pypi.org/project/notion-client/
El script utiliza la librería [notion_client][notion-client] para la conexión con ***Notion***.

En el fichero ***config.py*** se pueden introducir las siguientes configuraciones:

- ***TOKEN*** = Token de la API de Notion.
- ***DATABASE*** = ID de la Database.
- ***Nombre del proyecto*** = Nombre del Proyecto que irá en el campo ***Proyecto** en la database de Notion.
- ***Nombre de la prueba*** = Nombre que daremos a la prueba y que irá en el campo ***Prueba*** en la database de Notion.

---
## 2. Estructura. 
---

Hay que crear primero la ***Database*** y para este ejemplo se ha dispuesto la siguiente estructura:
- ***Proyecto:*** Nombre del Proyecto que se incluye en la configuración.
- ***Prueba:*** Nombre que se le puede dar a la prueba y que incluye en la configuración
- ***Fecha:*** Fecha que se crea automáticamente cuando se realiza la prueba.
- ***Pasado:*** Según el resultado obtenido se marcará el check o no.
- ***Resultado:*** Este campo no se transmite en la integración y se deja para que el usuario lo pueda modificar cuando se revisa la prueba en Notion.

La estructura está incluida en el fichero ***notion.py*** por lo que es fácilmentes modificable según las necesidades.

---
## 3. Utilización. 
---

Pasos a seguir para utilizar el script:
- Copiar los ficheros ***config.py***, ***notion.py*** (al ejecutar el scritp por primera vez se creará el fichero ***out.xml***)
- Añadirlos ***.gitignore*** si fuera necesario.
- Poner los datos de configuración el fichero ***config.py*** 
- Realizar las prueba con ***PyTest*** con las siguientes opciones (pueden añadirse más según requiera el usuario):
   ```
   pytest -q --junitxml== out.xml || python notion.py
   ```

[url]:https://debonair-owl-43c.notion.site/PyTest-9b4a37c58c2c45f6b3b232deb2869d5e
Mi página de Notion con las pruebas de este scritp se encuentra en la siguiente direccion [aquí][url]

