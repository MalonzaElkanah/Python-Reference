# Kenya Phone Numbers
# (+254)718306114 | 0718-306-114 | 0722404045

import re


def extract_phone_num(text):
    kenya_pattern = r"(\(\+\d{3}\)\d{9})|(\d{4}-\d{3}-\d{3})|(\d{10})"
    matching = re.compile(kenya_pattern)
    return matching.findall(text)


my_text = "(+254)734423363 0714-134-941This is 0756464654 just a text with random 0756464654 Kenyan Phone Numbers " \
          "(+254)718306114 0718-306-114 blah 0756464654 blah 07013-213-311 0756464654"
print(extract_phone_num(my_text))
