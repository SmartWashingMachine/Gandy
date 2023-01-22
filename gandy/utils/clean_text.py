import re

# TODO: Optimize
def clean_text(sentence):
    # deescape-special-chars
    new_sentence = re.sub(r'&bar;', '|', sentence)
    new_sentence = re.sub(r'&#124;', '|', new_sentence)
    new_sentence = re.sub(r'&lt;', '<', new_sentence)
    new_sentence = re.sub(r'&gt;', '>', new_sentence)
    new_sentence = re.sub(r'&bra;', '[', new_sentence)
    new_sentence = re.sub(r'&ket;', ']', new_sentence)
    new_sentence = re.sub(r'&quot;', '"', new_sentence)
    new_sentence = re.sub(r'&apos;', "'", new_sentence)
    new_sentence = re.sub(r'&#91;', '[', new_sentence)
    new_sentence = re.sub(r'&#93;', ']', new_sentence)
    new_sentence = re.sub(r'&amp;', '&', new_sentence)

    # replace-unicode-punctuation
    new_sentence = re.sub(r'，', ',', new_sentence)
    new_sentence = re.sub(r'。 *', '. ', new_sentence)
    new_sentence = re.sub(r'、', ',', new_sentence)
    new_sentence = re.sub(r'”', '"', new_sentence)
    new_sentence = re.sub(r'“', '"', new_sentence)
    new_sentence = re.sub(r'∶', ':', new_sentence)
    new_sentence = re.sub(r'：', ':', new_sentence)
    new_sentence = re.sub(r'？', '?', new_sentence)
    new_sentence = re.sub(r'《', '"', new_sentence)
    new_sentence = re.sub(r'》', '"', new_sentence)
    new_sentence = re.sub(r'）', ')', new_sentence)
    new_sentence = re.sub(r'！', '!', new_sentence)
    new_sentence = re.sub(r'（', '(', new_sentence)
    new_sentence = re.sub(r'；', ';', new_sentence)
    new_sentence = re.sub(r'１', '1', new_sentence)
    new_sentence = re.sub(r'」', '"', new_sentence)
    new_sentence = re.sub(r'「', '"', new_sentence)
    new_sentence = re.sub(r'０', '0', new_sentence)
    new_sentence = re.sub(r'３', '3', new_sentence)
    new_sentence = re.sub(r'２', '2', new_sentence)
    new_sentence = re.sub(r'５', '5', new_sentence)
    new_sentence = re.sub(r'６', '6', new_sentence)
    new_sentence = re.sub(r'９', '9', new_sentence)
    new_sentence = re.sub(r'７', '7', new_sentence)
    new_sentence = re.sub(r'８', '8', new_sentence)
    new_sentence = re.sub(r'４', '4', new_sentence)
    new_sentence = re.sub(r'． *', '. ', new_sentence)
    new_sentence = re.sub(r'～', '~', new_sentence)
    new_sentence = re.sub(r'’', "'", new_sentence)
    new_sentence = re.sub(r'…', '...', new_sentence)
    new_sentence = re.sub(r'━', '-', new_sentence)
    new_sentence = re.sub(r'〈', '<', new_sentence)
    new_sentence = re.sub(r'〉', '>', new_sentence)
    new_sentence = re.sub(r'【', '[', new_sentence)
    new_sentence = re.sub(r'】', ']', new_sentence)
    new_sentence = re.sub(r'％', '%', new_sentence)

    new_sentence = new_sentence.replace('\u200b', '')
    new_sentence = new_sentence.replace('\ufeff', '')
    new_sentence = new_sentence.replace('\u2060', '')
    new_sentence = new_sentence.replace('\u3000', '')

    return new_sentence
