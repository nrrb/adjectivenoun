from collections import defaultdict
import random
import json
import re
import sys

word_pattern = re.compile('^[a-z]+$')

with open('terms_by_pos.json', 'rb') as f:
    data = json.loads(f.read())

suitable_nouns = map(lambda w: w.lower(), filter(lambda word: re.match(word_pattern, word), data['Noun']))
suitable_adjectives = map(lambda w: w.lower(), filter(lambda word: re.match(word_pattern, word), data['Adjective']))
nouns_by_initial = defaultdict(lambda: [])
adjectives_by_initial = defaultdict(lambda: [])
for noun in suitable_nouns:
    nouns_by_initial[noun[0]].append(noun)
for adjective in suitable_adjectives:
    adjectives_by_initial[adjective[0]].append(adjective)

acronym = sys.argv[1].lower()
adjective_initials = [c for c in acronym[:-1]]
noun_initial = acronym[-1]

adjectives = [random.choice(adjectives_by_initial[c]) for c in adjective_initials]
noun = random.choice(nouns_by_initial[noun_initial]) 
words = adjectives + [noun]

print "{0} = {1}".format(acronym.upper(), ' '.join(map(lambda w: w.capitalize(), words)))

