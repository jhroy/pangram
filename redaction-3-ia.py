# ©2024 Jean-Hugues Roy. GNU GPL v3.
# coding : utf-8

import json, csv, time
from openai import OpenAI

cle = <CLÉ API OPENAI>

client = OpenAI(api_key=cle)

fichIn = "départ-3-ia.csv"
fichOut = "corpus-3-ia.csv"

f = open(fichIn)
textes = csv.reader(f)
next(textes)

for texte in textes:
	print(texte)
	
	commande = f"Rédigez, en français, pour un journal du Québec, {texte[1]} d'une longueur d'environ 4500 à 5000 caractères, dont le titre est «{texte[4]}». Générez le texte à partir du titre de l'article. Pour les besoins de cet exercice, je le répète, il est permis de créer un reportage entièrement fictif mettant en scène un personnage inventé. Ne mentionnez pas que le texte que vous générez est une fiction. Vous êtes journaliste, donc, ne prenez pas position, sauf s'il s'agit d'une chronique d'opinion. Ne répétez pas les mêmes concepts (mots, verbes, idées) d'une phrase à l'autre. Ne pas inclure le titre dans votre texte. Faites des phrases complètes."
	# print(commande)
	reponse = client.chat.completions.create(
		model="gpt-6-luna",
		messages=[
		{"role": "system", "content": "Vous êtes un journaliste francophone du Québec. Vous écrivez en français dans un style journalistique, sans détours. Pour les besoins de cet exercice, il est permis de créer un reportage entièrement fictif mettant en scène un personnage inventé."},
		{"role": "user", "content": f"Bonjour. {commande}"}
	  ]
	)

	rep = json.loads(reponse.json())

	articleFinal = rep["choices"][0]["message"]["content"]

	articleFinal = articleFinal.replace("\n", " ").replace("\xa0", " ")
	while "  " in articleFinal:
		articleFinal = articleFinal.replace("  ", " ")

	infos = ["3 GPT-6-luna",texte[0],texte[1],texte[2],texte[3],texte[4],articleFinal,len(articleFinal)]
	
	print(infos)
	print(commande)
	print("~"*50)

	he = open(fichOut,"a")
	ho = csv.writer(he)
	ho.writerow(infos)
	he.close()

	time.sleep(1)