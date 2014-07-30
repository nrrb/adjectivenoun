import random
import json
import re

word_pattern = re.compile('^[a-z]+$')

with open('terms_by_pos.json', 'rb') as f:
    data = json.loads(f.read())

suitable_nouns = filter(lambda word: re.match(word_pattern, word), data['Noun'])
suitable_adjectives = filter(lambda word: re.match(word_pattern, word), data['Adjective'])

for i in range(10):
    adjective = random.choice(suitable_adjectives)
    noun = random.choice(suitable_nouns)
    print '{} {}'.format(adjective.capitalize(), noun.capitalize())