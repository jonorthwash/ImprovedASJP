"""
A phoneme encoding based on the ALINE algorithm and ASJP encodings.
Questions:
1. I deleted the 'syllabic' feature, because I don't know how it works to distinguish sounds.
2. I don't know how to deal with lan-tense distinguishment.
"""
multivalued_features = {'place': {
							'bilabial': 100,
							'labiodental': 95,
							'dental': 90,
							'alveolar': 85,
							'retroflex': 80,
							'palato-alveolar': 75,
							'palatal': 70,
							'velar': 60,
							'uvular': 50,
							'pharyngeal': 30,
							'glottal': 10},
						'manner': {
							'stop': 100,
							'affricate': 90,
							'fricative': 80,
							'approximant': 60,
							'trill': 50,
							'high vowel': 40,
							'mid vowel': 20,
							'low vowel': 0},
						'high': {
							'high': 100,
							'mid': 50,
							'low': 0},
						'back': {
							'front': 100,
							'central': 50,
							'back': 0}}

ipa_symbols = { u'i': {'place': multivalued_features['place']['palatal'],
		       		'manner': multivalued_features['manner']['vowel'],
		       		'high': multivalued_features['high']['high'],
		       		'back': multivalued_features['back']['front'],
                    'vowel': 1,
		       		'round': 0,   
		       		'voice': 100, 
		       		'nasal': 0,
		       		'retroflex': 0,
		       		'lateral': 0},
		       	u'y': {'place': multivalued_features['place']['palatal'],
		       		'manner': multivalued_features['manner']['vowel'],
		       		'high': multivalued_features['high']['high'],
		       		'back': multivalued_features['back']['front'],
                    'vowel': 1,
		       		'round': 100,
		       		'voice': 100, 
		       		'nasal': 0,
		       		'retroflex': 0,
		       		'lateral': 0},
		       	u'ɪ': {'place': multivalued_features['place']['palatal'],
		       		'manner': multivalued_features['manner']['vowel'],
		       		'high': multivalued_features['high']['high'],
		       		'back': multivalued_features['back']['front'],
                    'vowel': 1,
		       		'round': 0,
		       		'voice': 100, 
		       		'nasal': 0,
		       		'retroflex': 0,
		       		'lateral': 0},
		       	u'ʏ': {'place': multivalued_features['place']['palatal'],
		       		'manner': multivalued_features['manner']['vowel'],
		       		'high': multivalued_features['high']['high'],
		       		'back': multivalued_features['back']['front'],
                    'vowel': 1,
		       		'round': 100,
		       		'voice': 100, 
		       		'nasal': 0,
		       		'retroflex': 0,
		       		'lateral': 0},
		       	u'ɨ': {'place': multivalued_features['place']['palatal'],
		       		'manner': multivalued_features['manner']['vowel'],
		       		'high': multivalued_features['high']['high'],
		       		'back': multivalued_features['back']['central'],
                    'vowel': 1,
		       		'round': 0,   
		       		'voice': 100, 
		       		'nasal': 0,
		       		'retroflex': 0,
		       		'lateral': 0},
		       	u'ʉ': {'place': multivalued_features['place']['velar'],
		       		'manner': multivalued_features['manner']['vowel'],
		       		'high': multivalued_features['high']['high'],
		       		'back': multivalued_features['back']['central'],
                    'vowel': 1,
		       		'round': 0,   
		       		'voice': 100, 
		       		'nasal': 0,
		       		'retroflex': 0,
		       		'lateral': 0},
		       	u'ʊ': {'place': multivalued_features['place']['velar'],
		       		'manner': multivalued_features['manner']['vowel'],
		       		'high': multivalued_features['high']['high'],
		       		'back': multivalued_features['back']['back'],
                    'vowel': 1,
		       		'round': 100,   
		       		'voice': 100, 
		       		'nasal': 0,
		       		'retroflex': 0,
		       		'lateral': 0},
		       	u'ɯ': {'place': multivalued_features['place']['velar'],
		       		'manner': multivalued_features['manner']['vowel'],
		       		'high': multivalued_features['high']['high'],
		       		'back': multivalued_features['back']['back'],
                    'vowel': 1,
		       		'round': 0,   
		       		'voice': 100, 
		       		'nasal': 0,
		       		'retroflex': 0,
		       		'lateral': 0},
		       	u'u': {'place': multivalued_features['place']['velar'],
		       		'manner': multivalued_features['manner']['vowel'],
		       		'high': multivalued_features['high']['high'],
		       		'back': multivalued_features['back']['back'],
                    'vowel': 1,
		       		'round': 100,   
		       		'voice': 100, 
		       		'nasal': 0,
		       		'retroflex': 0,
		       		'lateral': 0},
		       	u'e': {'place': multivalued_features['place']['palatal'],
		       		'manner': multivalued_features['manner']['vowel'],
		       		'high': multivalued_features['high']['mid'],
		       		'back': multivalued_features['back']['front'],
                    'vowel': 1,
		       		'round': 0,   
		       		'voice': 100, 
		       		'nasal': 0,
		       		'retroflex': 0,
		       		'lateral': 0},
		       	u'ø': {'place': multivalued_features['place']['palatal'],
		       		'manner': multivalued_features['manner']['vowel'],
		       		'high': multivalued_features['high']['mid'],
		       		'back': multivalued_features['back']['front'],
                    'vowel': 1,
		       		'round': 100,   
		       		'voice': 100, 
		       		'nasal': 0,
		       		'retroflex': 0,
		       		'lateral': 0},
		       	u'ɘ': {'place': multivalued_features['place']['palatal'],
		       		'manner': multivalued_features['manner']['vowel'],
		       		'high': multivalued_features['high']['mid'],
		       		'back': multivalued_features['back']['central'],
                    'vowel': 1,
		       		'round': 0,   
		       		'voice': 100, 
		       		'nasal': 0,
		       		'retroflex': 0,
		       		'lateral': 0},
		       	u'ɵ': {'place': multivalued_features['place']['velar'],
		       		'manner': multivalued_features['manner']['vowel'],
		       		'high': multivalued_features['high']['mid'],
		       		'back': multivalued_features['back']['central'],
                    'vowel': 1,
		       		'round': 100,   
		       		'voice': 100, 
		       		'nasal': 0,
		       		'retroflex': 0,
		       		'lateral': 0},
		       	#0xc7 0x9d
		       	u'ǝ': {'place': multivalued_features['place']['velar'],
		       		'manner': multivalued_features['manner']['vowel'],
		       		'high': multivalued_features['high']['mid'],
		       		'back': multivalued_features['back']['central'],
                    'vowel': 1,
		       		'round': 50,   
		       		'voice': 100, 
		       		'nasal': 0,
		       		'retroflex': 0,
		       		'lateral': 0},
		       	#0xc9 0x99
		       	u'ə': {'place': multivalued_features['place']['velar'],
		       		'manner': multivalued_features['manner']['vowel'],
		       		'high': multivalued_features['high']['mid'],
		       		'back': multivalued_features['back']['central'],
                    'vowel': 1,
		       		'round': 50,   
		       		'voice': 100, 
		       		'nasal': 0,
		       		'retroflex': 0,
		       		'lateral': 0},
		       	u'ɤ': {'place': multivalued_features['place']['velar'],
		       		'manner': multivalued_features['manner']['vowel'],
		       		'high': multivalued_features['high']['mid'],
		       		'back': multivalued_features['back']['back'],
                    'vowel': 1,
		       		'round': 0,   
		       		'voice': 100, 
		       		'nasal': 0,
		       		'retroflex': 0,
		       		'lateral': 0},
		       	u'o': {'place': multivalued_features['place']['velar'],
		       		'manner': multivalued_features['manner']['vowel'],
		       		'high': multivalued_features['high']['mid'],
		       		'back': multivalued_features['back']['back'],
                    'vowel': 1,
		       		'round': 100,   
		       		'voice': 100, 
		       		'nasal': 0,
		       		'retroflex': 0,
		       		'lateral': 0},
		       	u'ɛ': {'place': multivalued_features['place']['palatal'],
		       		'manner': multivalued_features['manner']['vowel'],
		       		'high': multivalued_features['high']['mid'],
		       		'back': multivalued_features['back']['front'],
                    'vowel': 1,
		       		'round': 0,   
		       		'voice': 100, 
		       		'nasal': 0,
		       		'retroflex': 0,
		       		'lateral': 0},
		       	u'œ': {'place': multivalued_features['place']['palatal'],
		       		'manner': multivalued_features['manner']['vowel'],
		       		'high': multivalued_features['high']['mid'],
		       		'back': multivalued_features['back']['front'],
                    'vowel': 1,
		       		'round': 100,   
		       		'voice': 100, 
		       		'nasal': 0,
		       		'retroflex': 0,
		       		'lateral': 0},
		       	u'æ': {'place': multivalued_features['place']['palatal'],
		       		'manner': multivalued_features['manner']['vowel'],
		       		'high': multivalued_features['high']['mid'],
		       		'back': multivalued_features['back']['front'],
                    'vowel': 1,
		       		'round': 0,   
		       		'voice': 100, 
		       		'nasal': 0,
		       		'retroflex': 0,
		       		'lateral': 0},
		       	u'ɜ': {'place': multivalued_features['place']['palatal'],
		       		'manner': multivalued_features['manner']['vowel'],
		       		'high': multivalued_features['high']['mid'],
		       		'back': multivalued_features['back']['central'],
                    'vowel': 1,
		       		'round': 0,   
		       		'voice': 100, 
		       		'nasal': 0,
		       		'retroflex': 0,
		       		'lateral': 0},
		       	u'ɞ': {'place': multivalued_features['place']['velar'],
		       		'manner': multivalued_features['manner']['vowel'],
		       		'high': multivalued_features['high']['mid'],
		       		'back': multivalued_features['back']['central'],
                    'vowel': 1,
		       		'round': 100,   
		       		'voice': 100, 
		       		'nasal': 0,
		       		'retroflex': 0,
		       		'lateral': 0},
		       	u'ɐ': {'place': multivalued_features['place']['velar'],
		       		'manner': multivalued_features['manner']['vowel'],
		       		'high': multivalued_features['high']['mid'],
		       		'back': multivalued_features['back']['central'],
                    'vowel': 1,
		       		'round': 50,   
		       		'voice': 100, 
		       		'nasal': 0,
		       		'retroflex': 0,
		       		'lateral': 0},
		       	u'ʌ': {'place': multivalued_features['place']['velar'],
		       		'manner': multivalued_features['manner']['vowel'],
		       		'high': multivalued_features['high']['mid'],
		       		'back': multivalued_features['back']['back'],
                    'vowel': 1,
		       		'round': 0,   
		       		'voice': 100, 
		       		'nasal': 0,
		       		'retroflex': 0,
		       		'lateral': 0},
		       	u'ɔ': {'place': multivalued_features['place']['velar'],
		       		'manner': multivalued_features['manner']['vowel'],
		       		'high': multivalued_features['high']['mid'],
		       		'back': multivalued_features['back']['back'],
                    'vowel': 1,
		       		'round': 100,   
		       		'voice': 100, 
		       		'nasal': 0,
		       		'retroflex': 0,
		       		'lateral': 0},
		       	u'a': {'place': multivalued_features['place']['palatal'],
		       		'manner': multivalued_features['manner']['vowel'],
		       		'high': multivalued_features['high']['low'],
		       		'back': multivalued_features['back']['front'],
                    'vowel': 1,
		       		'round': 0,   
		       		'voice': 100, 
		       		'nasal': 0,
		       		'retroflex': 0,
		       		'lateral': 0},
		       	u'ɶ': {'place': multivalued_features['place']['palatal'],
		       		'manner': multivalued_features['manner']['vowel'],
		       		'high': multivalued_features['high']['low'],
		       		'back': multivalued_features['back']['front'],
                    'vowel': 1,
		       		'round': 100,   
		       		'voice': 100, 
		       		'nasal': 0,
		       		'retroflex': 0,
		       		'lateral': 0},
		       	u'ɑ': {'place': multivalued_features['place']['velar'],
		       		'manner': multivalued_features['manner']['vowel'],
		       		'high': multivalued_features['high']['low'],
		       		'back': multivalued_features['back']['back'],
                    'vowel': 1,
		       		'round': 0,   
		       		'voice': 100, 
		       		'nasal': 0,
		       		'retroflex': 0,
		       		'lateral': 0},
		       	u'ɒ': {'place': multivalued_features['place']['velar'],
		       		'manner': multivalued_features['manner']['vowel'],
		       		'high': multivalued_features['high']['low'],
		       		'back': multivalued_features['back']['back'],
                    'vowel': 1,
		       		'round': 100,   
		       		'voice': 100, 
		       		'nasal': 0,
		       		'retroflex': 0,
		       		'lateral': 0},
		       	}