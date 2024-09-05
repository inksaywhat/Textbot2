# TextBot2

## Overview

**TextBot2** is a Python-based text analysis tool designed to process and analyze text files, such as books, and provide detailed insights. The tool counts words and sentences, calculates average word length, identifies the most frequently used words, and tracks character frequency across the entire text. 

The purpose of **TextBot2** is to give users a comprehensive view of textual data while serving as a learning project for Python programming concepts such as file handling, string manipulation, and basic data analysis.

## Features

TextBot2 includes the following features:
- **Word Count**: Counts the total number of words in the provided text.
- **Sentence Count**: Counts the number of sentences based on punctuation (periods, exclamation points, question marks).
- **Average Word Length**: Calculates the average length of words in the text.
- **Character Frequency Count**: Tracks how often each letter (A-Z) appears in the text.
- **Top N Frequent Words**: Displays the most frequent words in the text, excluding common stop words like "the", "and", and "of".

## How It Works

TextBot2 operates by reading a text file and performing the following analyses:
1. **Reads the text**: Loads the entire content of the text file into memory.
2. **Counts words**: Splits the text into words and counts the total number.
3. **Counts sentences**: Splits the text by sentence-ending punctuation and counts how many sentences exist.
4. **Character frequency**: Tracks how often each alphabetic character (case insensitive) appears in the text.
5. **Top N frequent words**: Identifies and displays the top N most frequently used words, filtering out common words (e.g., "the", "and").
6. **Generates a report**: Outputs the results of the analysis to the console.

## Setup

### Prerequisites

- **Python 3.x**: Ensure you have Python 3 installed on your machine.

### How to Run

1. Download or clone the repository.
2. Place the text file you want to analyze inside a directory named `books`. For example, `books/frankenstein.txt`.
3. Run the script in your terminal or command prompt:

```bash
python textbot2.py

