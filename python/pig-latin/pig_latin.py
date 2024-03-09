VOWELS = {"a", "e", "i", "o", "u"}
VOWELS_Y = {"a", "e", "i", "o", "u", "y"}
SPECIALS = {"xr", "yt"}

def translate(text):
    piglatined = []
    
    for word in text.split():
        if word[0] in VOWELS or word[0:2] in SPECIALS:
            piglatined.append(word + 'ay')
            continue
            
        for pos in range(1, len(word)):
            if word[pos] in VOWELS_Y:
                pos += 1 if word[pos] == 'u' and word[pos - 1] == "q" else 0
                piglatined.append(word[pos:] + word[:pos] + "ay")
                break
                    
    return " ".join(piglatined)