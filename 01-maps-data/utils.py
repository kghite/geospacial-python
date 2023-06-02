"""
Basic data utils
"""

import os

data_folder = 'data'
output_folder = 'output'
results_folder = 'images'


for path in [data_folder, output_folder, results_folder]:
    if not os.path.exists(path):
        os.mkdir(path)


def download(url):
    filename = os.path.join(data_folder, os.path.basename(url))
    if not os.path.exists(filename):
        from urllib.request import urlretrieve
        local, _ = urlretrieve(url, filename)
        print('Downloaded ' + local)
