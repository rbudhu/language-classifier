from __future__ import unicode_literals

import nltk
import json


def language_features(content):
    '''Simple feature for language specific keywords'''
    features = {}
    keywords = ['def', 'java', 'throws', 'struct',
                'void', 'sizeof', 'py', 'catch',
                'html', 'background', 'begin', 'end',
                'and', '#', '//', 'isset', 'var',
                '<', '/>', 'python', 'c++', 'php', 'html',
                'ruby', '?>', 'in', 'yield', '<?',
                '#!', 'sh', 'bash', 'print', 'include',
                'require', 'main', 'public', 'private',
                'protected', '`', 'function', 'import',
                'exit', 'die', ]
    for word in keywords:
        features['contains({})'.format(word)] = word in content.lower()
    return features

with open('dataset.json', 'r') as f:
    data = json.load(f)
    print('Loaded {} samples'.format(len(data)))
    featureset = [(language_features(sample['content']),
                   sample['language'])
                  for sample in data]
    size = int(len(featureset) * 0.1)
    train_set, test_set = featureset[size:], featureset[:size]
    classifier = nltk.DecisionTreeClassifier.train(train_set)
    print(nltk.classify.accuracy(classifier, test_set))
