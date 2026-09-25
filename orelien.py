import csv
from pangram import Pangram

cle = <CLÉ API PANGRAM>

# fichier = "corpus-1-humain.csv"
# fichier = "corpus-2-moitié.csv"
fichier = "corpus-3-ia.csv"
# fichierOUT = "pangram_gpt-4.csv"
fichierOUT = "pangram_gpt-6.csv"

f = open(fichier)
textes = csv.reader(f)
# next(textes)
textes = list(textes)

for texte in textes:
	print(len(texte[-2]))
	# print(texte[-2])

	pangram_client = Pangram(api_key=cle)
	result = pangram_client.predict(
		texte[-2],
		model="pangram-4",
		public_dashboard_link=False,
	)

	infos = []
	infos.append(fichier)
	infos.append(len(texte[-2]))
	for n in range(0,6):
		infos.append(texte[n])

	# print(result["prediction_short"])
	infos.append(result["prediction_short"])
	# print(result["fraction_ai"])
	infos.append(result["fraction_ai"])
	# print(result["fraction_ai_assisted"])
	infos.append(result["fraction_ai_assisted"])
	# print(result["fraction_human"])
	infos.append(result["fraction_human"])
	print(infos)

	he = open(fichierOUT,"a")
	ho = csv.writer(he)
	ho.writerow(infos)
	he.close()
