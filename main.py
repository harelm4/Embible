from src.preprocessor import Preprocessor
import json
from os import walk
# Preprocessor().parse_all_bible_books_to_json_lists()
for w in Preprocessor().get_all_words_in_jsons():
    if '־' in w:
        print(w)
print(len(Preprocessor().get_all_words_in_jsons()))#262762

