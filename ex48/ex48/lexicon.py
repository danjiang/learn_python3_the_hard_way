vocabulary = {
    "direction": ["north", "south", "east", "west", "down", "up", "left", "right", "back"],
    "verb": ["go", "stop", "kill", "eat"],
    "stop": ["the", "in", "of", "from", "at", "it"],
    "noun": ["door", "bear", "princess", "cabinet"]
}

def scan(sentence):
    """docstring for scan"""
    words = sentence.split()
    result = []
    for word in words:
        type = "error"
        for key, values in vocabulary.items():
            for value in values:
                if word == value:
                    type = key
        if type == "error":
            number = convert_number(word)
            if number != None: 
                result.append(("number", number))
                continue
        result.append((type, word))
    return result
        
def convert_number(s):
    """docstring for convert_number"""
    try:
        return int(s)
    except ValueError:
        return None
    
