# Code-Challenge 

Date: 30.07.2022

NOTE: To keep private
TODO: (View this file in row format to see the files tree)
xx@xx CodeChallenge % tree
.
├── Infos.md
├── app.py
├── components
│   ├── __pycache__
│   │   └── components.cpython-39.pyc
│   └── components.py
├── prj_structure.py
├── prj_structure.txt
├── requirements.txt
└── utils
    ├── API_request.py
    ├── __pycache__
    │   ├── API_request.cpython-39.pyc
    │   └── methods.cpython-39.pyc
    └── methods.py

Code Challenge Impuls

Integration von öffentlicher Wettervorhersage über API mit Python

Aufgabe: · Erstelle ein Tool, dass Prognosedaten von der https://www.weatherapi.com/ API abgreift und lokal als Zeitreihe in einer csv Datei oder einer Datenbank abspeichert.

· Benötigte Daten:

o Windgeschwindigkeit (Kmh)

o Temperatur (Celsius)

o Cloud coverage (Percent)

· An diesen Orten:

o Köln, München, Berlin

· Die Prognose soll die nächsten 3 Tage abdecken und in stündlicher Auflösung erfolgen


Tipps und Hinweise:

· Wir haben bereits einen API Key für dich erstellt: bea853d469e0444dbe7152331220507

· Example API Request (einfach mal in den Browser kopieren): o http://api.weatherapi.com/v1/forecast.json?key=bea853d469e0444dbe7152331220507&q=Cologne

· Also Python Bibliotheken zur Einbindung von APIs sind zum Beispiel request oder aiohttp geeignet · API-Dokumentation: https://www.weatherapi.com/docs/

Übergabe:

· Entweder kannst du uns deinen Ordner als .zip Datei schicken oder mit uns ein Github Repository teilen
