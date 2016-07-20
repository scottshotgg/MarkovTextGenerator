import random


sample = open('WarAndPeaceRemoved')

sampleText = sample.read()

#print sampleText

#sampleText = sampleText.replace('\n', ' ')
#WarAndPeaceRemoved = open('WarAndPeaceRemoved', "w")
#WarAndPeaceRemoved.write(sampleText)
#WarAndPeaceRemoved.close()

words = sampleText.split(' ')

i = 0
for word in words:
	words[i] = word.replace('\n', ' ')

	i += 1

#print words

dict = {}

i = 1
#print len(words)

state = 'post'

if state is 'post':
	for word in words:
		#print "word: " + word
		if i != len(words) - 1:
			if (words[i - 1], words[i]) in dict:
				dict[(words[i - 1], words[i])] += [words[i + 1]]
			else:
				dict[(words[i - 1], words[i])] = [words[i + 1]]
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
#print '\n\n' + '%s \n\n' % (word,)
wordSave = word[1]
print wordSave

word2 = None
strToPrint = ''
for x in range (0, 1000):
	strToPrint += '%s ' % (word[1],)
	#print word
	if word2 is not None:
		print "passed the if"
		try:
			array = dict[(word2, wordSave)]
		except KeyError as err:
			#strToPrint += " * RANDOM * " + "(" + word2 + ", " + wordSave + ")"
			array = dict[random.choice(dict.keys())] 
	else:
		print "didnt pass the if"
		array = dict[word]
	#print array
	randvar = random.randint(0, len(array) - 1)
	word2 = word[1]
	wordSave = array[randvar]
	print ("(" + word2 + ", " + wordSave + ")")
	word = (word2, wordSave)

print strToPrint
sample.close()