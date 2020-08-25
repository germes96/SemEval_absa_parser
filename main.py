from utils import *
from data_process import *
base_path = ''
raw_train_path = os.path.join(base_path, 'data/test.xml')
test_data = parse_sentence_term_for_sentiment(raw_train_path)
data = get_sentence_vector(test_data)
print(test_data[3]['sentence'])
print(data[3])
