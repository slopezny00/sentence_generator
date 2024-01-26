"""
Program: sentenceGenerator.py
Chapter 5 Case Study
1/8/2024

Application that generates and displays sentences using simple grammar and vocabulary. Words are chosen at random. Each small task will be its own function and user will enter the number of sentences to generate.
"""
import random

# Global variables consisting of the lists of vocabulary words.
articles = ("A", "THE", "AN")

nouns = ("BOY", "GIRL", "BAT", "BALL", "DOG", "CAT", "TURTLE", "ROCK", "PIZZA", "ABRAHAM LINCOLN", "TESLA", "TABLE", "SEAL", "HORSE", "BUG", "BEETLE", "LOG", "HOUSE", "SUN")

verbs = ("HIT", "SAW", "LIKED", "JUMPED", "RAN", "BUILT", "SNEEZED", "PARKED", "FELL", "TYPED", "TOOK", "BLEW", "BIT", "CHEWED", "BURIED", "RADIATED", "ATE")

prepositions = ("WITH", "BY", "FROM", "AT", "TO", "UNDER")

# Definition of the sentence() function
def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

# Definition of the nounPhrase() function
def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

# Definition of the verbPhrase() function
def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

# Definition of the prepositionalPhrase() function
def prepositionalPhrase():
    """Builds and returns a prepositional phrase"""
    return random.choice(prepositions) + " " + nounPhrase()

# Definition of the main() function
def main():
    """Allows the user to input the number of sentences."""
    number = int(input("Please tell me the number of sentences you would like >> "))
    for count in range(number):
        print(sentence())
    input("Sentences complete, press ENTER to exit...")

# Global call to the main() function for program entry
if __name__ == '__main__':
    main()