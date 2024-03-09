def response(hey_bob):
    hey_bob = hey_bob.rstrip()
    if not hey_bob:
        return "Fine. Be that way!"
    question = hey_bob.endswith("?")
    shout = hey_bob.isupper()
    if question and shout:
        return "Calm down, I know what I'm doing!"
    if question:
        return "Sure."
    if shout:
        return "Whoa, chill out!"
    if hey_bob.isspace():
        return "Fine. Be that way!"
    return "Whatever."
