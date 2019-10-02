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
    """
    Takes a message as a string and

    Returns
    -------
    the entropy of the message as bits
    """
    counter = letter_freq(message)
    total_nmb_letters = sum(counter.values())
    freq_of_letter_in_message = {
        ord(char): chr_amount/total_nmb_letters for char, chr_amount in counter.items()}
    calculated_entropy = -1 * sum([
        freq_of_char * log2(freq_of_char) for freq_of_char in freq_of_letter_in_message.values()
    ])
    return calculated_entropy


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
