import unittest
import text_processing as Text_Processing


text = """The inflated style itself is a a kind of euphemism. A mass of Latin words falls upon the facts like soft snow, blurring the outline
 and covering up all the details. The great enemy of clear language is insincerity. When there is a gap between one’s real and one’s declared aims,
  one turns as it were instinctively to long words and exhausted idioms, like a cuttlefish spurting out ink. In our age there is no such thing as 
  ‘keeping out of politics.’ All issues are political issues, and politics itself is a mass of lies, evasions, folly, hatred, and schizophrenia. 
  When the general atmosphere is bad, language must suffer. I should expect to find — this is a guess which I have not sufficient knowledge to verify — 
  that the German, Russian and Italian languages have all deteriorated in the last ten or fifteen years, as a result of dictatorship."""


class SimpleTest(unittest.TestCase):
	TP = Text_Processing.IWordFrequencyAnalyzer()

	def test_output(self):
		self.assertEqual(self.TP.CalculateHighestFrequency(text), 8)
		self.assertEqual(self.TP.CalculateFrequencyForWord(text, 'languages'), 1)
		self.assertEqual(self.TP.CalculateMostFrequentNWords(text, 3), [('a', 8), ('the', 8), ('is', 7)])


	def test_types(self):
		self.assertRaises(TypeError, Text_Processing.IWordFrequencyAnalyzer, 5454)

		self.assertRaises(TypeError, self.TP.CalculateHighestFrequency, 456)
		self.assertRaises(TypeError, self.TP.CalculateHighestFrequency, 3+5j)
		self.assertRaises(TypeError, self.TP.CalculateHighestFrequency, True)

		self.assertRaises(TypeError, self.TP.CalculateFrequencyForWord, text, 56)
		self.assertRaises(TypeError, self.TP.CalculateFrequencyForWord, text, 3+5j)
		self.assertRaises(TypeError, self.TP.CalculateFrequencyForWord, text, True)

		self.assertRaises(TypeError, self.TP.CalculateMostFrequentNWords, text, 'abcd')
		self.assertRaises(TypeError, self.TP.CalculateMostFrequentNWords, text, 3+5j)
		self.assertRaises(TypeError, self.TP.CalculateMostFrequentNWords, text, True)


	def test_values(self):
		self.assertRaises(ValueError, self.TP.CalculateHighestFrequency, " ")
		self.assertRaises(ValueError, self.TP.CalculateFrequencyForWord, " "," ")
		self.assertRaises(ValueError, self.TP.CalculateMostFrequentNWords, " ", 65)
		self.assertRaises(ValueError, self.TP.CalculateMostFrequentNWords, text, -65)
	
		

if __name__ == '__main__':
    unittest.main()