import random


sample = open('WarAndPeace')

sampleText = sample.read()

#print sampleText

sampleText = sampleText.replace('\n', ' ')

words = sampleText.split(' ')

i = 0
for word in words:
	words[i] = word.replace('\n', ' ')

	i += 1

#print words

dict = {}

word = 'me'
word2 = 'you'

dict[word + word2] = 'this'

print dict



i = 0
#print len(words)

state = 'post'

if state is 'post':
	for word in words:
		#print "word: " + word
		if i != len(words) - 1:
			if word in dict:
				dict[word] += [words[i + 1]]
			else:
				dict[word] = [words[i + 1]]
			i += 1
			#print i

		#else:
			#dict[word] = ['']

elif state is 'pre':
	for word in words:
		if i != 0:
			if word in dict:
				dict[word] += [words[i - 1]]
			else:
				dict[word] = [words[i - 1]]
		i += 1

#print dict

	#print dict[word]
word = random.choice(dict.keys())
print '\n\n' + word + '\n\n'

strToPrint = ''
for x in range (0, 50):
	strToPrint += word + ' '
	#print word
	array = dict[word]
	#print array
	randvar = random.randint(0, len(array) - 1)
	word = array[randvar]


print strToPrint