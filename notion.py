import json
from notion_client import Client
from config import TOKEN, DATABASE_ID, PROYECTO, PRUEBAS
from datetime import datetime, timezone
import pytz
import xmltodict


#open the file
fileptr = open("out.xml","r")
 
#read xml content from the file
xml_content = fileptr.read() #xml_content= fileptr.read()
 
#change xml format to ordered dict
xml_formated=xmltodict.parse(xml_content)
salida = json.dumps(xml_formated, indent=3)

if (xml_formated["testsuites"]["testsuite"]["@errors"] == "0") and (xml_formated["testsuites"]["testsuite"]["@failures"] == "0") and (xml_formated["testsuites"]["testsuite"]["@skipped"] == "0"):
    checkbox = True
else:
    checkbox = False

# Variables de configuración del fichero "config.py"
token = TOKEN
database_id = DATABASE_ID
proyecto = PROYECTO
pruebas = PRUEBAS

notion = Client(auth=token)

published_date = datetime.now().astimezone(pytz.timezone('Europe/Madrid')).isoformat()

parent = {"database_id": database_id}

page_tags = {
   "Proyecto": {
            "type": "title",
            "title": [
                {
                    "type": "text",
                    "text": {
                        "content": proyecto,
                        "link": None
                    },
                    "annotations": {
                        "bold": False,
                        "italic": False,
                        "strikethrough": False,
                        "underline": False,
                        "code": False,
                        "color": "default"
                    },
                    "plain_text": "Primera prueba",
                    "href": None
                }
            ]
        },
   "Prueba":{
            "type": "rich_text",
            "rich_text": [
                {
                    "text": {
                        "content" : pruebas
                    }
                }
            ]  
   },
    "Fecha": {
            "type": "date",
            "date": {
                "start": published_date,
                "end": None,
                "time_zone": None
            }
    },
    "Pasado":{
            "type": "checkbox",
            "checkbox": checkbox
    }
}

children = [
    {
        "object": "block",
        "type": "code",
        "code": {
            "caption": [],
            "rich_text": [
              {
                "type": "text",
                "text": {
                  "content": salida, #"============================= test session starts =============================\nplatform win32 -- Python 3.11.3, pytest-7.3.1, pluggy-1.0.0\nrootdir: C:\\Users\\sauri\\Documents\\Proyectos\\python\\PyTest-Notion\nplugins: anyio-3.6.2, notion-1.0.1\ncollected 1 item\ntest_main.py .\n============================== 1 passed in 0.01s ==============================",
                  "link": None
                },
                "annotations": {
                  "bold": False,
                  "italic": False,
                  "strikethrough": False,
                  "underline": False,
                  "code": True,
                  "color": "default"
                },
                "plain_text": salida, #"============================= test session starts =============================\nplatform win32 -- Python 3.11.3, pytest-7.3.1, pluggy-1.0.0\nrootdir: C:\\Users\\sauri\\Documents\\Proyectos\\python\\PyTest-Notion\nplugins: anyio-3.6.2, notion-1.0.1\ncollected 1 item\ntest_main.py .\n============================== 1 passed in 0.01s ==============================",
                "href": None
              }
            ],
            "language": "json"
        },
    },
]

results = notion.pages.create(parent=parent, properties = page_tags, children = children)