import json
import requests

api = 'https://api.github.com/gists'
# Your github username
username = ''
# Your github password
passwd = ''

# Number of github gist pages to request
max_pages = 40
# Holds the language and the content of the gist
data = []
for i in xrange(max_pages):
    res = requests.get('{}/public'.format(api), auth=(username, passwd))
    pub_gists = res.json()
    for pub_gist in pub_gists:
        try:
            files = pub_gist['files']
            for fname, prop in files.iteritems():
                language = prop['language']
                if language and language is not 'null':
                    id = pub_gist['id']
                    f = requests.get('{}/{}'.format(api, id),
                                     auth=(username, passwd))
                    gist = f.json()
                    for _, obj in gist['files'].iteritems():
                        content = obj['content']
                        print('Appending {} gist sample...'.format(language))
                        data.append({'language': language, 'content': content})
        except KeyError as e:
            print(str(e))

with open('dataset.json', 'w') as out:
    out.write(json.dumps(data))
