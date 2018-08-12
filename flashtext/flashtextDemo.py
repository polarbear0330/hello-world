from flashtext import KeywordProcessor

keywordProcessor = KeywordProcessor()

keywordProcessor.add_keyword_from_file("keywords.txt")
keywordProcessor.add_keyword("orange", "watermelon")

print(" ")

print(keywordProcessor.get_all_keywords())

print(keywordProcessor.extract_keywords("I like apple and Banana!"))

print(keywordProcessor.replace_keywords("I like orange!"))