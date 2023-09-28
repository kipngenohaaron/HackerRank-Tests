# You are given  words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

# Note: Each input line ends with a "\n" character.

# Constraints:

# The sum of the lengths of all the words do not exceed 
# All the words are composed of lowercase English letters only.

# Input Format

# The first line contains the integer, .
# The next  lines each contain a word.

# Output Format

# Output  lines.
# On the first line, output the number of distinct words from the input.
# On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

# Sample Input

# 4
# bcdef
# abcdefg
# bcde
# bcdef
# Sample Output

# 3
# 2 1 1
# Explanation

# There are  distinct words. Here, "bcdef" appears twice in the input at the first and last positions. The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.

#solutions
from collections import OrderedDict

# Function to count word occurrences while preserving input order
def count_word_occurrences(n, words):
    word_count = OrderedDict()
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

# Input
n = int(input())
words = [input().strip() for _ in range(n)]

# Count word occurrences
word_occurrences = count_word_occurrences(n, words)

# Output the number of distinct words
print(len(word_occurrences))

# Output the number of occurrences for each distinct word
print(*word_occurrences.values())


def count_word_occurrences():
    # Read the total number of words
    n = int(input())

    # Initialize dictionary to store word counts
    word_count = {}

    # Iterate over the input words
    for _ in range(n):
        word = input().strip()

        # Update the word count in the dictionary
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Output the number of distinct words
    print(len(word_count))

    # Output the count of occurrences for each distinct word
    occurrences = ' '.join(str(count) for count in word_count.values())
    print(occurrences)


# Call the function
count_word_occurrences()