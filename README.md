# Scrapper_Youtube
TP Noté Architecture Microservices

Mise en place de l'environnement python et installation des packages requis:

- python3.8 -m venv .venv
- source .venv/bin/activate
- pip install --upgrade pip
- pip install -r requirements.txt

Execution du scrapper : ATTENTION !!! Si une erreur s'affiche lors de l'execution essayez de le reéxecuter une deuxième fois ça peut marcher !

- python scrapper.py --input input.json --output output.json

Executer les tests :

- pytest -q test_fonctions.py
