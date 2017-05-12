def load_data_label(data_path):
    '''
    Return data
    '''
    data = []
    for sentence in open(data_path, encoding='utf-8').read().strip().split('\n\n'):
        sent_data = []
        for line in sentence.strip().split('\n'):
            line = line.strip().split(' ')
            if line[0] == '-DOCSTART-':
                break
            sent_data.append([line[0], line[1], 0 if line[3] == 'O' else 1])
        if sent_data:
            data.append(sent_data)
    return data


def label_to_file(filename, data):
    with open(filename, 'w') as ofile:
        for sent_data in data:
            for i in range(len(sent_data)):
                tlabel = 'O'
                if sent_data[i][2] == 1:
                    if i > 0 and sent_data[i-1][2] == 1:
                        tlabel = 'I'
                    else:
                        tlabel = 'B'
                ofile.write(sent_data[i][0] + '\t' + tlabel + '\t' + sent_data[i][1] + '\n')
            ofile.write('\n')

def get_POS_tags(filename):
    pos_tag = set()
    for sentence in open(filename, encoding='utf-8').read().strip().split('\n\n'):
        sent_data = []
        for line in sentence.strip().split('\n'):
            pos_tag.add(line.strip().split('\t')[1])
    print(pos_tag)

# get_POS_tags('conll2003_train.txt')


data = []
data.extend(load_data_label('eng.train'))
data.extend(load_data_label('eng.testa'))
data.extend(load_data_label('eng.testb'))

label_to_file('conll2003_train.txt', data)
