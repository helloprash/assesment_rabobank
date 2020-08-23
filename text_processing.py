import re

class IWordFrequency:

    def __init__(self, Word=None):
        self.Word = Word
        self.Frequency = 0

class IWordFrequencyAnalyzer(IWordFrequency):

	def __init__(self):
		IWordFrequency.__init__(self)


	def __CalculateFrequency(self, text):
		"Returns a dictionary containing words as keys and their frequencies as values"

		if type(text) is not str:
			raise TypeError("The input should be a string")

		wordList = text.split(" ") #Splitting the string into individual words
		wordList = list(map(lambda x: x.lower(), wordList)) #Converting the words to lowercase
		wordList = list(map(lambda x: re.sub('[^A-Za-z]', '', x), wordList)) #Removing symbols from the words
		wordList = [word for word in wordList if len(word)] #Removing empty strings
		uniqueWords = set(wordList) #Getting unique words
		WordFreqDict = dict()

		for word in uniqueWords:
			freq = wordList.count(word)
			WordFreqDict[word] = freq

		WordFreqDictSorted = {k: v for k, v in sorted(WordFreqDict.items(), reverse=True, key=lambda item: item[1])} #Sprting the dictionary by value

		return WordFreqDictSorted


	def CalculateHighestFrequency(self, text):
		"Returns an integer of the highest frequency word"

		if len(re.sub('[^A-Za-z]', '', text)) == 0:
			raise ValueError("The input string should not be empty")

		WordFrequencyDictSorted = self.__CalculateFrequency(text)

		self.Word = list(WordFrequencyDictSorted.items())[0][0]  #Most Frequent Word
		self.Frequency = list(WordFrequencyDictSorted.items())[0][1] #Most frequent word value

		return self.Frequency


	def CalculateFrequencyForWord(self, text, Word):
		"Returns an integer of the frequency of the given word"

		if type(Word) is not str or type(text) is not str:
			raise TypeError("The input should be a string")

		if len(re.sub('[^A-Za-z]', '', Word)) == 0 or len(re.sub('[^A-Za-z]', '', text)) == 0:
			raise ValueError("The input string should not be empty")

		WordFrequencyDictSorted = self.__CalculateFrequency(text)
		
		return WordFrequencyDictSorted[Word.lower()]


	def CalculateMostFrequentNWords(self, text, n):
		"Returns a list of tuple of length n"

		if type(n) is not int:
			raise TypeError("n value should be an integer")

		if type(text) is not str:
			raise TypeError("The text should be a string")

		if n < 0:
			raise ValueError("n value should be an positive")

		if len(re.sub('[^A-Za-z]', '', text)) == 0:
			raise ValueError("The text should not be empty")


		WordFrequencyDictSorted = self.__CalculateFrequency(text)
		sliced_result = list(WordFrequencyDictSorted.items())[0:n] #Slicing the list by length n
		sliced_result_dict = dict(sliced_result)

		result_dict = dict()

		for i, v in sliced_result_dict.items():
			result_dict[v] = [i] if v not in result_dict.keys() else sorted(result_dict[v] + [i]) #Grouping the words by its frequency with sorting in ascending order

		result_list = list()

		for key, val in result_dict.items():
			for item in val:
				result_list.append((item, key)) #Creating a list of tuples

		return result_list

'''

text = """The inflated style itself is a a kind of euphemism. A mass of Latin words falls upon the facts like soft snow, blurring the outline
 and covering up all the details. The great enemy of clear language is insincerity. When there is a gap between one’s real and one’s declared aims,
  one turns as it were instinctively to long words and exhausted idioms, like a cuttlefish spurting out ink. In our age there is no such thing as 
  ‘keeping out of politics.’ All issues are political issues, and politics itself is a mass of lies, evasions, folly, hatred, and schizophrenia. 
  When the general atmosphere is bad, language must suffer. I should expect to find — this is a guess which I have not sufficient knowledge to verify — 
  that the German, Russian and Italian languages have all deteriorated in the last ten or fifteen years, as a result of dictatorship."""


TP = IWordFrequencyAnalyzer()

#print(A.__CalculateFrequency())
print(TP.CalculateHighestFrequency(text))
print(TP.CalculateFrequencyForWord(text, 'languages'))
print(TP.CalculateMostFrequentNWords(text, 6))

'''