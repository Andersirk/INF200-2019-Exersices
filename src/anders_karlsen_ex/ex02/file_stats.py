from collections import Counter


def char_counts(textfilename):
    """ opens the file with the given filename
     using encoding utf-8 and reads the entire file content into a single string.
    then counts how often each character code (0–255) occurs in the string
    Returns
    -------
    return the result as a list, where result[i] gives the number
    of occurances of charactor code i.
    """
    with open(textfilename, encoding="utf-8") as file:
        file_as_string = file.read()
        freq_of_characters = Counter(file_as_string)
        list_character_freq_as_index = [0 for _ in range(256)]
        for key, value in freq_of_characters.items():
            if ord(key) < 256:
                list_character_freq_as_index[ord(key)] = value
    return list_character_freq_as_index


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
