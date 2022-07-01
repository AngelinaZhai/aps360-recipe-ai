from data_cleaner import data

import requests

# print(data[1][1])
with open('pic1.jpg', 'wb') as handle:
    response = requests.get(data[1][1], stream=True)

    if not response.ok:
        print(response)

    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)
        