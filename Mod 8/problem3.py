'''
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into
it. Write a Python program that:
- Reads the file
- Requests 5 inputs from the user: 5 words the user would like to count the frequency of
- Counts how many times each word appears
- Creates a dictionary of the words and their counts
- Print the dictionary to the console
'''

file = open("song_lyrics.txt", "r")
lyrics = file.read()
file.close()


lyrics = lyrics.lower()


words_to_count = []
for i in range(5):
    word = input(f"Enter word {i + 1} to count: ").lower()
    words_to_count.append(word)


word_counts = {}
for word in words_to_count:
    count = lyrics.count(word)
    word_counts[word] = count


print("\nWord Frequency Dictionary:")
print(word_counts)


