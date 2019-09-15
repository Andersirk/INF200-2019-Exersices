def letter_freq(text):
    counter = {}
    lowered_text = text.lower()
    sorted_lowered_text = sorted(lowered_text)

    for character in sorted_lowered_text:
        if character in counter:
            counter[character] += 1
        else:
            counter[character] = 1
    return counter


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))
