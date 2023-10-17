import wikipedia as wiki



def wiki_output(word):
    result=wiki.summary(word,50)
    return result