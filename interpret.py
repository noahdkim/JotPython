import nltk

def evaluate(request):
    tokens = nltk.word_tokenize(request)
    tagged = nltk.pos_tag(tokens)
    entities = nltk.chunk.ne_chunk(tagged)
    print(entities)
    return("add", "event", "7pm")
