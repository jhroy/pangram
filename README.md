README

# Pangram est-il fiable?

Test de l'outil de détection d'IA générative [Pangram](https://www.pangram.com/) avec un corpus utilisé dans deux expériences antérieures.

## Fiabilité discutable des outils de détection de l'IA

En 2023, j'avais fait un premier test avec [GPTZero](https://gptzero.me/fr). Mes résultats ont été publiés dans *La Conversation* sous le titre évocateur de [«&nbsp; J’ai testé un outil de détection de ChatGPT : j’ai perdu mon temps&nbsp;»](https://theconversation.com/jai-teste-un-outil-de-detection-de-chatgpt-jai-perdu-mon-temps-201745).

Pour faire cette expérience, j'avais utilisé un corpus de 900 textes&nbsp;:

* 300 textes en français

* 300 textes en anglais

* 300 textes traduits du français vers l’anglais à l’aide de l’API de [DeepL](https://www.deepl.com/fr).

Tous ces groupes de 300 textes étaient structurés de la même manière&nbsp;:

* **[100 articles écrits par des journalistes](corpus-1-humain.csv)**, publiés au cours des cinq dernières années et moissonnés dans les sites web de différents médias canadiens.

* **100 articles générés en partie par GPT-3** (à l'époque). J’ai pris **[la première partie d’autres articles](départ-2-moitié.csv)** et j’ai demandé à GPT de les compléter avec une commande (*prompt*) ressemblant à : *«&nbsp;Voici le début d’un article, dont le titre est X. Complétez-le avec 1500 à 2500 caractères, pour publication dans un journal canadien.&nbsp;»*

* **100 articles générés entièrement par GPT-3** à partir de **[titres d'autres articles encore](départ-3-ia.csv)** avec une commande qui ressemblait à : *«&nbsp;Rédigez, pour publication dans un journal canadien, un article de 4500 à 5000 caractères dont le titre est X.&nbsp;»*

Le [code et les données de cette expérience sont accessibles sur un autre de mes répertoires Github](https://github.com/jhroy/auditGPTZero).

## Même constat en 2024

L'année suivante, à l'occasion de la conférence *«&nbsp;Les opportunités pédagogiques de l’IA générative en enseignement supérieur : mirage et réalités&nbsp;»*, organisée en avril 2024 à l'UQAM, j'ai présenté les résutats d'une deuxième expérience qui ressemblait à la première à ces différences près&nbsp;:

* J'ai testé trois outils, GPTZero, [ZeroGPT](https://www.zerogpt.com/) et [Winston](https://gowinston.ai/).

* J'ai utilisé un corpus en français seulement (pas de textes en anglais, ni de traductions du français vers l'anglais), donc de 300 textes.

* J'ai utilisé **GPT-4**, fraîchement sorti du four d'OpenAI pour générer les **[100 textes «&nbsp;moitié moitié&nbsp;»](corpus-2-moitié-GPT4.csv)** et les **[100 textes «&nbsp;IA&nbsp;»](corpus-3-ia-GPT4.csv)**, en plus d'utiliser les mêmes **[100 textes humains](corpus-1-humain.csv)**.

Les [résultats, accessibles via Archipel](https://archipel.uqam.ca/19854/1/JHRoy-OutilsDe%CC%81tectionIA.pdf), ne permettaient pas d'accroître la confiance envers ces outils.

## Qu'en est-il en 2026 avec Pangram?

Quand [toute la controverse](https://www.ledevoir.com/lire/1011020/thelyson-orelien-accuse-x-avoir-genere-roman-c-etait-ou-mourir-ia?) [entourant](https://www.lapresse.ca/arts/litterature/2026-09-23/ia-et-litterature/l-affaire-thelyson-orelien-en-six-questions.php) [l'auteur Thélyson Orélien](https://fr.wikipedia.org/wiki/Th%C3%A9lyson_Or%C3%A9lien) [a éclaté](https://www.journaldemontreal.com/2026/09/24/le-salon-du-livre-de-lestrie-retire-a-thelyson-orelien-son-titre-dinvite-dhonneur), [j'ai voulu tester la fiabilité de Pangram](https://www.ledevoir.com/economie/techno/1011257/intelligence-artificielle-detecter-ia-roman-est-ce-fiable?). Mon hypothèse?

> [!NOTE]
> ### HYPOTHÈSE : Pangram est aussi 💩 que les autres.

J'ai donc repris mon corpus de 2024 et l'ai soumis à l'[API de Pangram](https://www.pangram.com/solutions/api).

Cet outil donne plusieurs résultats après avoir analysé un texte. Il le classe dans l'une ou l'autre de trois catégories&nbsp;: *Human*; *Mixed*; *AI*.

Il donne aussi des probabilités que le texte ait été généré par l'IA (le paramètre est *`fraction_ai`*), écrit avec l'assistance de l'IA (*`fraction_ai_assisted`*) ou rédigé par un être humain (*`fraction_human`*).

Le script **[orelien.py](orelien.py)** analyse chacun des 300 textes, un corpus à la fois, et produit un fichier avec, notamment, la catégorie dans laquelle il a classé chaque texte. J'ai mis les résultats bruts dans le fichier **[pangram_gpt-4.csv](pangram_gpt-4.csv)**. Mais voici un tableau résumant ces résultats&nbsp;:

| Corpus ⬇️ \ Catégorie ➡️       | Human | Mixed | AI  | Fiabilité |
|----------------|-------:|-------:|-----:|-----------:|
| 1 journaliste  | 100   |       |     | 100%      |
| 2 moitié       | 3     | 97    |     | 97%       |
| 3 GPT-4        |       |       | 100 | 100%      |

## Pangram est-il aussi fiable avec des modèles contemporains?

J'avoue avoir été bluffé! Mais si c'était parce que Pangram avait analysé des texte générés avec un vieux modèle? GPT-4 date de 2024, après tout. Cela fait des millénaires en années d'IAG.

J'ai donc généré de nouveaux corpus en utilisant le modèle GPT-6-Luna&nbsp;:

* **[100 textes «&nbsp;moitié moitié&nbsp;» avec GPT-6](corpus-2-moitié-GPT6.csv)** et
* **[100 textes «&nbsp;IA&nbsp;» avec GPT-6](corpus-3-ia-GPT6.csv)**

Les résultats bruts se trouvent dans le fichier **[pangram_gpt-6.csv](pangram_gpt-6.csv)** et sont tout aussi bons&nbsp;:

| Corpus ⬇️ \ Catégorie ➡️       | Human | Mixed | AI  | Fiabilité |
|----------------|-------:|-------:|-----:|-----------:|
| 1 journaliste  | 100   |       |     | 100%      |
| 2 moitié (GPT-6)      | 2     | 98    |     | 98%       |
| 3 GPT-6        |       |       | 100 | 100%      |

Impressionnant, certes. Mais il ne faut jamais perdre de vue que de faux positifs sont toujours possibles, comme l'a constaté [François Cardinal](https://www.lapresse.ca/actualites/chroniques/2026-09-23/dans-le-calepin-de-l-editeur-adjoint/thelyson-orelien-la-presse-poursuit-son-enquete.php).
