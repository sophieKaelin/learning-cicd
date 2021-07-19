from __future__ import print_function
import random

# List inputs.
buzz = ('continuous testing', 'continuous integration', 'continuous deployment', 'continuous improvement', 'devops')
adjectives = ('complete', 'modern','self-service','integrated','end-to-end')
adverbs = ('remarkably', 'enormously', 'substantially', 'significantly', 'seriously')
verbs = ('accelerates', 'improves', 'enhances', 'revamps', 'boosts')

# Take a _list input and choose n random items from that list.
def selectRandom(_list, n=1):
	result = random.sample(_list, n)
	if n == 1:
		return result[0]
	return result

# Function that creates a buzzword phrase
def generateBuzz():
	buzz_terms = selectRandom(buzz, 2)
	phrase = ' '.join([selectRandom(adjectives), buzz_terms[0], selectRandom(adverbs), selectRandom(verbs), buzz_terms[1]])
	return phrase

if __name__ == "__main__":
	print(generateBuzz())