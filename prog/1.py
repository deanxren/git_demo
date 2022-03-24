def find_most_frequent(text):
    words = text.lower().split()
    clean_words = [word.rstrip(',.:;!?') for word in words]
    frequent = []
    max_count = 0
    for word in set(clean_words):
        count_of_occurences = clean_words.count(word)
        if count_of_occurences > max_count:
            max_count = count_of_occurences
            frequent = [word]
        elif count_of_occurences == max_count:
            frequent.append(word)
    frequent.sort()
    print(frequent)



find_most_frequent('to understand recursion you need first to understand recursion...')