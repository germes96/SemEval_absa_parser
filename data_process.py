
import nltk
nltk.download('punkt')

#retourne la distance du mot par rapport a l'aspect
def get_word_aspect_distance(aspect_start_position,aspect_end_position, word_position):
    if word_position < aspect_start_position:
        return - (aspect_start_position - word_position)
    elif word_position > aspect_end_position:
        return - (aspect_end_position - word_position)
    else:
        return 0

#returne la liste des mots d'une phrase et la position de chaque mot
def get_word_with_indice(sentence):
    # tokens = ['je', 'mange', 'la', 'banane']
    tokens = nltk.word_tokenize(sentence)
    data = []
    i = 0
    for token in tokens:
        data.append({'word': token, 'position': i})
        i = i+1
    return data

#deternime les coordonnee de l'aspet dans la phrase
def get_aspect_position(sentence, aspect):
    tokens = nltk.word_tokenize(sentence)
    aspect_token = nltk.word_tokenize(aspect)
    aspect_length = len(aspect_token)
    start_positio = 0
    end_positio = 0
    for i in range(len(tokens)):
        # print(tokens[i], aspect_token[0])
        if tokens[i] == aspect_token[0]:
            match = True
            for j in range(len(aspect_token)):
                # print(tokens[i+j], aspect_token[j])
                if tokens[i+j] != aspect_token[j]:
                    match = False
            if match:
                start_positio = i
                end_positio = aspect_length+i-1
    return start_positio, end_positio



# Sentence reprensentation contain sentence, aspect, polarity, start and end
def get_sentence_vector(sentence_representatio):
    result = []
    for sent_rep in sentence_representatio:
        sentence = sent_rep['sentence']
        aspect = sent_rep['aspect']
        data = get_word_with_indice(sentence)
        start, end = get_aspect_position(sentence, aspect)
        oneElmt = []
        for elm in data:
            oneElmt.append(get_word_aspect_distance(aspect_start_position=start, aspect_end_position=end,
                                           word_position=elm['position']))
        result.append(oneElmt)
    return result