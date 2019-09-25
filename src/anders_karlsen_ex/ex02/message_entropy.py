from math import log2


def letter_freq(txt):
    counter = {}
    lowered_text = txt.lower()
    sorted_lowered_text = sorted(lowered_text)

    for character in sorted_lowered_text:
        if character in counter:
            counter[character] += 1
        else:
            counter[character] = 1
    return counter


def entropy(message):
    counter = letter_freq(message)
    total_number_of_letters = sum(counter.values())
    freq_of_letter_in_message = {}
    entropy = 0
    for key, value in counter.items():
        freq_of_letter_in_message[ord(key)] = value/total_number_of_letters
    for value in freq_of_letter_in_message.values():
        entropy += value * log2(value)
    entropy2 = -1 * entropy
    return entropy2


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
