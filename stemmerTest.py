import pandas as pd

data = pd.read_csv('abcnews-date-text.csv', error_bad_lines=False);
data_text = data[['headline_text']]
data_text['index'] = data_text.index
documents = data_text

import treetaggerwrapper
from pprint import pprint

#tagger = treetaggerwrapper.TreeTagger(TAGLANG='it')
tagger = treetaggerwrapper.TreeTagger(TAGLANG="it", TAGDIR='/Applications/TreeTagger')
tags = tagger.tag_text("L'altro ieri sono caduto in una buca profonda e ho incontrato il bianconiglio")

pprint(treetaggerwrapper.make_tags(tags))


#   Extract lemmas
tags = treetaggerwrapper.make_tags(tags)
lemmas = []
for tag in tags:
    lemmas.append(tag.lemma)
lemmas
# Thanks, this worked. On linux the path where the scripts are installed could be specified directly in the python code e.g. treetaggerwrapper.TreeTagger(TAGLANG="it", TAGDIR='/abs-path/to/tree-tagger-linux-3.2.1/'), or as an environment variable as explained here treetaggerwrapper.readthedocs.io/en/latest/#configuration Also to get just the lemmas from the Tag named tuples: tags_str = tagger.tag_text(it_string) then tags = treetaggerwrapper.make_tags(tags_str) then lemmas = map((lambda x: x.lemma), tags)


# Per installare treetagger:
#   http://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/#parfiles
#   scaricare i file
#   Su OSX NON eseguire lo script sh di intallazione; invece:
#   scompattare tree-tagger-MacOSX-3.2.2.tar e spostare il contenuto nella cartella dove c'è l'archivo appena scompattato
#   scompattare tagger-scripts.tar e spostare il contenuto nella cartella dove c'è l'archivo appena scompattato
#   spostare file dei parametri dentro lib