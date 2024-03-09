def is_isogram(string):
    "Compare scrubbed list to unscrubbed string"
    scrubbed = [l.lower() for l in string if l.isalpha()]
    return len(set(scrubbed)) == len(scrubbed)