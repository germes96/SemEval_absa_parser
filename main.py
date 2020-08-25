from utils import *
base_path = ''
raw_train_path = os.path.join(base_path, 'data/test.xml')
test_data = parse_sentence_term_for_sentiment(raw_train_path)
print(test_data[3])
