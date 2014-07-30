import random
import json
import re

word_pattern = re.compile('^[a-z]+$')

with open('terms_by_pos.json', 'rb') as f:
    data = json.loads(f.read())

suitable_nouns = filter(lambda word: re.match(word_pattern, word), data['Noun'])
suitable_adjectives = filter(lambda word: re.match(word_pattern, word), data['Adjective'])

for i in range(100):
    adjective1 = random.choice(suitable_adjectives)
    adjective2 = random.choice(suitable_adjectives)
    noun = random.choice(suitable_nouns)
    print '{} {} {}'.format(adjective1.capitalize(), adjective2.capitalize(), noun.capitalize())