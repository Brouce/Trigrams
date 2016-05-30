from nltk import FreqDist,trigrams,word_tokenize
from string import maketrans
symbols=",[]();:<>+=&+%!@#~?{}|1234567890'"
whitespace='                                 '

def common_tri(textt):
    word=word_tokenize(textt)
    fdist=FreqDist(trigrams(word))
    h=fdist.most_common(1)
    h=str(h)
    trans=maketrans(symbols,whitespace)
    x= h.translate(trans)
    x = x.strip()
    print(x)
    
##he function operates for trigrams, simple adjustment can be made to use whatever 
##number of terms (n grams)
    
    
    

    