from src.preprocessor import Preprocessor
import json
from os import walk
# Preprocessor().parse_all_bible_books_to_json_lists()

# Preprocessor().resolveSOP()

print(len(Preprocessor().get_all_words_in_jsons()))