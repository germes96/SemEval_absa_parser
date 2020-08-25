
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
    tokens = ['je', 'mange', 'la', 'banane']
    data = []
    i = 0
    for token in tokens:
        data.append({'word': token, 'position': i})
        i = i+1
    return data

#deternime les coordonnee de l'aspet dans la phrase
def get_aspect_position(sentence, aspect):
    tokens = ['je', 'mange', 'la', 'fausse', 'banane']
    aspect_token = ['la', 'fausse']
    i = 0
    aspect_length = len(aspect_token)
    start_positio = 0
    end_positio = 0
    for i in range(len(tokens)):
        print(tokens[i], aspect_token[0])
        if tokens[i] == aspect_token[0]:
            match = True
            for j in range(len(aspect_token)):
                print(tokens[i+j], aspect_token[j])
                if tokens[i+j] != aspect_token[j]:
                    match = False
            if match:
                start_positio = i
                end_positio = aspect_length+i-1
    return start_positio, end_positio



# Sentence reprensentation contain sentence, aspect, polarity, start and end
def get_sentence_vector(sentence_representatio):
    print('noting')


print(get_word_aspect_distance(aspect_start_position=2, aspect_end_position=3, word_position=6))
# print(get_aspect_position("je mange la banane", "la"))

# print(["yo","ya"] == ["yo","yy"])