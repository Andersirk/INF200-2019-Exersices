from ..file_stats import char_counts
import os


def test_length_of_list_is_256():
    path = "C:/Users/ander/Documents"
    textfilename = os.path.join(path, "testt.txt")
    assert len(char_counts(textfilename)) == 256
    pass