import nltk

def evaluate(query):
    tokens = nltk.word_tokenize(query)
    tagged = nltk.pos_tag(tokens)
    entities = nltk.chunk.ne_chunk(tagged)
    print(entities)
    action = tokens[0]
    event = ' '.join(tokens[1:-1])


    return(action, event)
