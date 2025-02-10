def isPangram_inefficient(s):
    s = s.lower()

    letters = []
    for ch in s:
        if ch.isalpha():
            if ch not in letters:
                letters.append(ch)
    if len(letters) == 26:
        return "Pangram"
    else:
        return "Not a pangram"

def isPangram(s):
    s = s.lower()
    letters = {}

    for ch in s:
        if ch.isalpha():
            if ch not in letters:
                letters[ch] = 1
    
    if len(letters) == 26:
        return "Pangram"
    else:
        return "Not a pangram"

# main
print(isPangram("We promptly judged antique ivory buckles for the prize"))