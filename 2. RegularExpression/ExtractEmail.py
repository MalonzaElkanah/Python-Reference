# Extract email
# elkanahmalonza@gmail.com

import re


def extract_email(text):
    pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}')
    return pattern.findall(text)


tw = "elkanahmalonza@gmail.com  elkanahm2321alonza@gmail.com delkanah32@gmail.com     wf r1 elkanahrth@kmss.co.me"
print(extract_email(tw))
