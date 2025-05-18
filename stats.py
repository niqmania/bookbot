def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_characters(book_text):
    character_count = {}    # Convert the text to lowercase to make the count case-insensitive
    lowered = book_text.lower()
    #split = list(lowered)
    for char in lowered:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return(character_count)

def sort_list(character_count):
    sorting = []
    for char, count in character_count.items():
        if char.isalpha():
            sorting.append({'char': char, 'num': count})
            sorting.sort(key=lambda x: x['num'], reverse=True)
    return sorting