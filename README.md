Description:
This code prompts the user to input a sentence and a word, then counts how many times the given word appears as a substring in the words of the sentence.
Both the sentence and the word are converted to lowercase to ensure case-insensitive comparison.

How it works:
The user enters a sentence.

The sentence is converted to lowercase.

The user enters a word, also converted to lowercase.

The sentence is split into individual words using .split().

For each word, the program checks if the input word is a substring of that word.

If it is, the counter is incremented.

Finally, the total number of matches is printed.
