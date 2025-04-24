def count_words(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count


def count_chars(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def sort_character_counts(char_counts):
    filtered_counts = {char: count for char, count in char_counts.items() if char.isalpha()}
    char_list = [{"char": char, "num": count} for char, count in filtered_counts.items()]
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list
