import json
from notion_client import Client
from config import TOKEN, DATABASE_ID
from datetime import datetime, timezone
import pytz

#f = open("out.txt", "r")
#salida = str(f.read())
#f.close()
#print(salida)

salida = "Hello World"

f = open("out.xml", "r")
salida = str(f.read())
f.close()

token = TOKEN
database_id = DATABASE_ID

notion = Client(auth=token)
json_object = notion.blocks.children.list(database_id)
json_formatted_str = json.dumps(json_object, indent=2)

published_date = datetime.now().astimezone(pytz.timezone('Europe/Madrid')).isoformat()

parent = {"database_id": database_id}

page_tags = {
   "Name": {
            "type": "title",
            "title": [
                {
                    "type": "text",
                    "text": {
                        "content": "Primera prueba",
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
    "Date": {
            "type": "date",
            "date": {
                "start": published_date,
                "end": None,
                "time_zone": None
            }
        },
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
                  "code": False,
                  "color": "default"
                },
                "plain_text": salida, #"============================= test session starts =============================\nplatform win32 -- Python 3.11.3, pytest-7.3.1, pluggy-1.0.0\nrootdir: C:\\Users\\sauri\\Documents\\Proyectos\\python\\PyTest-Notion\nplugins: anyio-3.6.2, notion-1.0.1\ncollected 1 item\ntest_main.py .\n============================== 1 passed in 0.01s ==============================",
                "href": None
              }
            ],
            "language": "xml"
        },
    },
]

results = notion.pages.create(parent=parent, properties = page_tags, children = children)