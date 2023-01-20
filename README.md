# Kasutusjuhend

## Paigaldamine

Selles lahenduses kasutatakse [Python](https://www.python.org/downloads/release/python-380/) ja Pythoni rammastikud Flask, Jinja ja SQLAlchemy.

Rakendus töötab 5000 pordil.

Andmete säilitamiseks/töötlemiseks kasutatakse SQLite admebaas.

Projekti struktuur:
```
.
├── website
│   ├── static
│   │   ├── script.js
│   │   ├── style.css
│   ├── templates
│   │   ├── base.html
│   │   ├── create.html
│   │   ├── home.html
│   │   ├── update.html
│   │   └── view.html
│   ├── __init__.py  
│   ├── models.py
│   └── views.py
├── main.py
└── README.md
```

Proekti edukaks avamiseks on vaja kasutada pipenv.
Käsurea käsk Pipenvi installimiseks
```bash
pip install pipenv
```
Pärast seda proekti repos
```bash
pipenv install
```
Projekt on nüüd käivitamiseks valmis
```bash
pipenv run python main.py
```
