import string
import json
import re

pos_key = {'Noun' : 'N',
        'Plural' : 'p',
        'Noun Phrase' : 'h',
        'Verb (usu participle)' : 'V',
        'Verb (transitive)' : 't',
        'Verb (intransitive)' : 'i',
        'Adjective' : 'A',
        'Adverb' : 'v',
        'Conjunction' : 'C',
        'Preposition' : 'P',
        'Interjection' : '!',
        'Pronoun' : 'r',
        'Definite Article' : 'D',
        'Indefinite Article' : 'I',
        'Nominative' : 'o'}
pos_key_by_abbrev = {v: k for k,v in pos_key.items()}

term_pattern = re.compile('^\w+$')
# acceptable_pos = set(['Noun', 'Adjective'])

with open('mobypos.txt', 'r') as f:
    data = map(string.strip, f.readlines())

terms_by_pos = {}
for line_number, line in enumerate(data):
    if (line_number+1)%10000 == 0:
        print line_number
    term, pos = line.split('\\')
    if not re.match(term_pattern, term):
        # This is not a term we want
        continue
    try:
        parts_of_speech = set([pos_key_by_abbrev[c] for c in pos])
    except KeyError:
        # We hit a part of speech abbreviation that doesn't exist, this is a bad egg
        continue
    # if len(parts_of_speech.intersection(acceptable_pos)) == 0:
    #     # None of this term's parts of speech are what we want
    #     continue
    for part_of_speech in parts_of_speech:
        terms_by_pos[part_of_speech] = terms_by_pos.get(part_of_speech, []) + [term]

with open('terms_by_pos.json', 'wb') as f:
    f.write(json.dumps(terms_by_pos))