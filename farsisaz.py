import re

def slug_fa(text):
    text = re.sub(r'[^\w\s\u0600-\u06FF-]' ,'' , text)
    text = re.sub(r'\s+','-',text)
    text = text.strip('-')
    return text