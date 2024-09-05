# TextBot2: A text analysis tool that expands on the original BookBot project

def main():
    # Path to the book file
    book_path = "books/frankenstein.txt"
    
    # Step 1: Read the entire book text from the file
    text = get_book_text(book_path)
    
    # Step 2: Perform various types of text analysis
    word_count = count_words(text)               # Count the total number of words
    sentence_count = count_sentences(text)       # Count the total number of sentences
    avg_word_len = average_word_length(text)     # Calculate the average word length
    character_counts = count_characters(text)    # Count the frequency of each character (A-Z)
    top_words = count_words_frequency(text)      # Find the top N most frequent words (excluding common words)

    # Step 3: Print the analysis report with all the collected data
    print_report(book_path, word_count, sentence_count, avg_word_len, character_counts, top_words)


def get_book_text(path):
    """
    Reads the text from the given file path.
    This function opens the file at the given 'path', reads the entire contents, 
    and returns it as a string.
    """
    with open(path, 'r') as f:  # 'r' means open the file in read-only mode
        return f.read()         # Read the whole file and return as a string


def count_words(text):
    """
    Counts the number of words in the text.
    Splits the text by spaces to get individual words and returns the length of the resulting list.
    """
    words = text.split()       # Split the text into words based on spaces
    return len(words)          # Return the total number of words


def count_sentences(text):
    """
    Counts the number of sentences in the text.
    Splits the text based on common sentence-ending punctuation ('.', '!', '?') 
    and returns the number of sentences.
    """
    sentences = text.split('. ')  # Split based on periods followed by a space
    sentences += text.split('! ') # Add sentences ending with '!'
    sentences += text.split('? ') # Add sentences ending with '?'
    
    return len(sentences)  # Return the total number of sentences


def average_word_length(text):
    """
    Calculates the average length of words in the text.
    Loops through the words, adds up their lengths, and divides by the total number of words.
    """
    words = text.split()  # Split text into words
    total_length = sum(len(word) for word in words)  # Calculate total length of all words
    return total_length / len(words)  # Return the average word length


def count_characters(text):
    """
    Counts the frequency of each character in the text.
    Converts the text to lowercase, loops through each character, and counts only alphabetic characters (A-Z).
    """
    text = text.lower()  # Convert text to lowercase to make the count case-insensitive
    char_count = {}      # Initialize an empty dictionary to store character counts

    # Loop through each character in the text
    for char in text:
        if char.isalpha():  # Check if the character is a letter (ignore punctuation, numbers, etc.)
            if char in char_count:
                char_count[char] += 1  # If the character is already in the dictionary, increment its count
            else:
                char_count[char] = 1   # If not, add it to the dictionary with an initial count of 1

    return char_count  # Return the dictionary containing character counts


def count_words_frequency(text, top_n=10):
    """
    Counts the frequency of words in the text and returns the top N most frequent words.
    Excludes common stop words like 'the', 'and', etc., and counts only alphabetic words.
    """
    common_words = ["the", "and", "a", "to", "of", "in", "that", "is", "it", "with"]  # List of common words to exclude
    words = text.lower().split()  # Convert text to lowercase and split into words
    word_count = {}  # Initialize an empty dictionary to store word counts

    # Loop through each word in the text
    for word in words:
        if word.isalpha() and word not in common_words:  # Check if the word is alphabetic and not a common word
            if word in word_count:
                word_count[word] += 1  # If the word is already in the dictionary, increment its count
            else:
                word_count[word] = 1   # If not, add it to the dictionary with an initial count of 1

    # Convert the word count dictionary to a sorted list of dictionaries
    word_list = [{"word": word, "count": count} for word, count in word_count.items()]
    word_list.sort(reverse=True, key=lambda x: x['count'])  # Sort the list by the count, in descending order

    return word_list[:top_n]  # Return the top N most frequent words


def print_report(path, word_count, sentence_count, avg_word_len, character_counts, top_words):
    """
    Prints a report of the text analysis, including:
    - The number of words and sentences
    - The average word length
    - The top N most frequent words
    - Character frequency counts
    """
    # Print the header of the report
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")         # Print the total number of words
    print(f"{sentence_count} sentences found in the document") # Print the total number of sentences
    print(f"Average word length: {avg_word_len:.2f}")          # Print the average word length, formatted to 2 decimal places

    # Print the top N most frequent words
    print("\nTop words in the document:")
    for item in top_words:
        print(f"The word '{item['word']}' appeared {item['count']} times")

    # Print character counts
    print("\nCharacter counts:")
    char_list = [{"char": char, "num": count} for char, count in character_counts.items()]  # Convert character counts to list
    char_list.sort(reverse=True, key=lambda x: x["num"])  # Sort the list by the number of occurrences (most frequent first)
    
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")

    # Print the footer of the report
    print("--- End report ---")


# This line makes sure the program runs when executed directly, not when imported
if __name__ == "__main__":
    main()
