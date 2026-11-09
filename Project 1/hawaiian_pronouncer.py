"""
Author: Robert Thomas Kohn
Date: October 28, 2026
Description: CSI 109 Project 1 -- prints a pronunciation guide for a Hawaiian word.
Code of honesty: I have not copied from any source without proper citation.
"""

# --- Constants ---
# Defining these once, at the top, means the rest of your program never has to
# spell out the alphabet or the sound tables again.

VALID_CHARS = "aeiouhklmnpw' "      # the 13 letters (including the 'okina) and a space
VOWELS = "aeiou"
CONSONANTS = "hklmnpw"

SINGLE_VOWEL_SOUNDS = {
    'a': 'ah', 'e': 'eh', 'i': 'ee', 'o': 'oh', 'u': 'oo'
}
VOWEL_GROUPS = {
    'ai': 'eye', 'ae': 'eye', 'ao': 'ow', 'au': 'ow',
    'ei': 'ay', 'eu': 'eh-oo', 'iu': 'ew', 'oi': 'oy',
    'ou': 'ow', 'ui': 'ooey'
}


# --- Functions ---

def is_valid_word(word):
    """Return True if word uses only Hawaiian letters, the 'okina, and spaces,
    and contains at least one letter. Capitalisation is ignored.
    """
    word_lower = word.lower()
    has_letter = False

    for char in word_lower:
        if char not in VALID_CHARS:
            return False
        if char in VOWELS or char in CONSONANTS:
            has_letter = True

    return has_letter


def get_valid_hawaiian_word():
    """Ask for a word until the user enters a valid one, then return it."""
    word = input("Enter a Hawaiian word to pronounce ==> ")
    while not is_valid_word(word):
        print("That is not a valid Hawaiian word. Please try again.")
        word = input("Enter a Hawaiian word to pronounce ==> ")
    return word


def get_vowel_sound(word, index):
    """Return (sound, characters_consumed) for the vowel at word[index].
    A vowel group is checked first and consumes two characters;
    otherwise a single vowel consumes one.
    """
    pair = word[index:index + 2].lower()
    if pair in VOWEL_GROUPS:
        return (VOWEL_GROUPS[pair], 2)

    single = word[index].lower()
    if single in SINGLE_VOWEL_SOUNDS:
        return (SINGLE_VOWEL_SOUNDS[single], 1)

    return (single, 1)


def pronounce(word):
    """Return the hyphenated pronunciation of a valid Hawaiian word or phrase."""
    word_lower = word.lower()
    words = []
    current_syllables = []
    i = 0

    while i < len(word_lower):
        char = word_lower[i]

        if char == " ":
            # Space marks the end of the current word
            if current_syllables:
                words.append("-".join(current_syllables))
                current_syllables = []
            i += 1
        elif char == "'":
            # The 'okina separates syllables and is not pronounced
            i += 1
        elif char in VOWELS:
            # Standalone vowel sound
            sound, consumed = get_vowel_sound(word_lower, i)
            current_syllables.append(sound)
            i += consumed
        elif char in CONSONANTS:
            # w is pronounced v when it comes right after an i or an e
            if char == "w" and i > 0 and word_lower[i - 1] in ("i", "e"):
                consonant_sound = "v"
            else:
                consonant_sound = char

            # Check if followed by a vowel sound
            if i + 1 < len(word_lower) and word_lower[i + 1] in VOWELS:
                vowel_sound, consumed = get_vowel_sound(word_lower, i + 1)
                current_syllables.append(consonant_sound + vowel_sound)
                i += 1 + consumed
            else:
                # Consonant with no following vowel is pronounced on its own
                current_syllables.append(consonant_sound)
                i += 1
        else:
            i += 1

    # Append any remaining syllables from the last word
    if current_syllables:
        words.append("-".join(current_syllables))

    return " ".join(words)


# ------------------------------------------------------------------
# Everything below this line is already written for you.
# Do not change it. Run the program after each function you finish
# and watch the FAILs turn into PASSes.
# ------------------------------------------------------------------

def check(test, result, expected):
    """Print PASS if result matches expected, otherwise print FAIL."""
    if result == expected:
        print("PASS", test, "gave", result)
    else:
        print("FAIL", test, "gave", result, "but should give", expected)


def main():
    """Test each of your functions, then pronounce a word you type in."""

    print("--- Testing is_valid_word ---")
    check("is_valid_word('aloha')", is_valid_word("aloha"), True)
    check("is_valid_word('ALOHA')", is_valid_word("ALOHA"), True)
    check("is_valid_word('Mele Kalikimaka')", is_valid_word("Mele Kalikimaka"), True)
    check("is_valid_word('Hello!')", is_valid_word("Hello!"), False)
    check("is_valid_word('')", is_valid_word(""), False)
    check("is_valid_word('   ')", is_valid_word("   "), False)

    print()
    print("--- Testing get_vowel_sound ---")
    check("get_vowel_sound('aloha', 0)", get_vowel_sound("aloha", 0), ("ah", 1))
    check("get_vowel_sound('kai', 1)", get_vowel_sound("kai", 1), ("eye", 2))
    check("get_vowel_sound('hawaii', 3)", get_vowel_sound("hawaii", 3), ("eye", 2))
    check("get_vowel_sound('hawaii', 5)", get_vowel_sound("hawaii", 5), ("ee", 1))

    print()
    print("--- Testing pronounce ---")
    check("pronounce('aloha')", pronounce("aloha"), "ah-loh-hah")
    check("pronounce('mahalo')", pronounce("mahalo"), "mah-hah-loh")
    check("pronounce('kai')", pronounce("kai"), "keye")
    check("pronounce('hawaii')", pronounce("hawaii"), "hah-weye-ee")
    check("pronounce('iwi')", pronounce("iwi"), "ee-vee")
    check("pronounce(\"humuhumunukunukuapua'a\")", pronounce("humuhumunukunukuapua'a"),
          "hoo-moo-hoo-moo-noo-koo-noo-koo-ah-poo-ah-ah")
    check("pronounce('Mele Kalikimaka')", pronounce("Mele Kalikimaka"),
          "meh-leh kah-lee-kee-mah-kah")

    print()
    print("--- Now try get_valid_hawaiian_word yourself ---")
    print("Type an invalid word first (like Hello!) to check that it asks again.")
    word = get_valid_hawaiian_word()
    print(pronounce(word))


main()
