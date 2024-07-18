from typing import List, Dict
import os
from collections import Counter

class UserData:
    """
    A class to represent user data containing sentences.
    
    Attributes:
    - sentences (List[str]): A list of sentences provided by the user.
    """

    def __init__(self, data_source: List[str]):
        """
        Initialize the UserData object.

        Parameters:
        - data_source (List[str]): Either a list of sentences or a file path containing sentences.

        Raises:
        - ValueError: If the data source is not a list or a valid file path.
        """
        if isinstance(data_source, list):
            self.sentences = data_source
        elif isinstance(data_source, str) and os.path.isfile(data_source):
            with open(data_source, 'r') as file:
                self.sentences = file.readlines()
        else:
            raise ValueError("Invalid data source provided.")

    @property
    def num_sentences(self) -> int:
        """
        Get the number of sentences.

        Returns:
        - int: The number of sentences.
        """
        return len(self.sentences)

    def _word_frequency_in_sentence(self, sentence: str) -> Counter:
        """
        Calculate the frequency of each unique word in a single sentence.

        Parameters:
        - sentence (str): The input sentence.

        Returns:
        - Counter: A Counter object representing the word frequencies.
        """
        words = sentence.split()
        return Counter(words)

    def _word_frequency_in_corpus(self) -> Counter:
        """
        Calculate the frequency of each unique word in the whole corpus (all sentences).

        Returns:
        - Counter: A Counter object representing the word frequencies in the entire corpus.
        """
        corpus_frequency = Counter()
        for sentence in self.sentences:
            corpus_frequency += self._word_frequency_in_sentence(sentence)
        return corpus_frequency

    def word_frequency(self) -> Counter:
        """
        Get the frequency of each unique word in the whole corpus (all sentences).

        Returns:
        - Counter: A Counter object representing the word frequencies in the entire corpus.
        """
        return self._word_frequency_in_corpus()


