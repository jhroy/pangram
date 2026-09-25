# ©2024 Jean-Hugues Roy. GNU GPL v3.
# coding : utf-8

import json, csv, time
from openai import OpenAI

cle = <CLÉ API OPENAI>

client = OpenAI(api_key=cle)

fichIn = "départ-2-moitié.csv"
fichOut = "corpus-2-moitié.csv"

f = open(fichIn)
textes = csv.reader(f)
next(textes)

for texte in textes:
	print(texte[:-1])
	
	commande = f"Complétez, pour un journal du Québec, {texte[1]} en français dont le titre est «{texte[4]}» et qui commence ainsi: «{texte[5]}». Votre ajout doit faire environ 1500 à 2500 caractères. Vous êtes journaliste, donc, ne prenez pas position, sauf s'il s'agit d'une chronique d'opinion. Ne pas répéter les mêmes concepts (mots, verbes, idées) d'une phrase à l'autre. Ne me fournissez que votre ajout. Faites des phrases complètes."
	# print(commande)
	reponse = client.chat.completions.create(
		model="gpt-6-luna",
		messages=[
		{"role": "system", "content": "Vous êtes un journaliste francophone du Québec. Vous écrivez en français dans un style journalistique, sans détours."},
		{"role": "user", "content": f"Bonjour. {commande}"}
	  ]
	)

	rep = json.loads(reponse.json())

	articleGPT = rep["choices"][0]["message"]["content"]

	articleFinal = texte[5] + " | " + articleGPT

	articleFinal = articleFinal.replace("\n", " ").replace("\xa0", " ")
	while "  " in articleFinal:
		articleFinal = articleFinal.replace("  ", " ")

	infos = ["2 moitié",texte[0],texte[1],texte[2],texte[3],texte[4],articleFinal,len(articleFinal)]

	print(infos)
	print("~"*50)

	he = open(fichOut,"a")
	ho = csv.writer(he)
	ho.writerow(infos)
	he.close()

	time.sleep(1)

he.close()