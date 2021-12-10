REGEX_ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def cypher(msg):
    msg = msg.lower()
    trans_map = msg.maketrans(REGEX_ALPHABET, REGEX_ALPHABET[::-1])
    return
    sent = input()
    print(cypher(sent))
