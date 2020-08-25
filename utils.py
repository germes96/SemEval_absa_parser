import os
from xml.etree.ElementTree import parse

split_char = '__split__'
def parse_sentence_term(path, lowercase=False):
    tree = parse(path)
    sentences = tree.getroot()
    print(sentences)
    data = []
    for sentence in sentences:
        text = sentence.find('text')
        if text is None:
            continue
        text = text.text
        if lowercase:
            text = text.lower()
        aspect_terms = sentence.find('aspectTerms')
        if aspect_terms is None:
            continue
        for aspectTerm in aspect_terms:
            term = aspectTerm.get('term')
            if lowercase:
                term = term.lower()
            polarity = aspectTerm.get('polarity')
            start = aspectTerm.get('from')
            end = aspectTerm.get('to')
            piece = text + split_char + term + split_char + polarity + split_char + start + split_char + end
            data.append(piece)
    return data


def parse_sentence_term_for_sentiment(path, lowercase=False):
    representations = parse_sentence_term(path, lowercase=lowercase)
    data = []
    for representation in representations:
        raw = str(representation).split(split_char)
        sentence = {'sentence': raw[0], 'aspect': raw[1], 'polarity': raw[2], 'start': raw[3], 'end': raw[4]}
        data.append(sentence)
    return data

