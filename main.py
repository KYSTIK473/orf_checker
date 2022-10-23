import docx
import enchant
doc = docx.Document('778dc422632e4c0f89b65d3c09e6a661.docx')
text = []
for paragraph in doc.paragraphs:
    text.append(paragraph.text)
arr = []
for i in text:
    i = i.replace(';', ',')
    i = i.replace(' – ', ', ')
    i = i.split(', ')
    arr_v = []
    for j in i:
        if '_' in j or '..' in j:
            if len(arr) == 0:
                k = j.replace('_', 'и')
            else:
                k = j.replace('..', 'и')
            arr_v.append(k.lower())
        else:
            arr_v.append(j.lower())
    arr.extend(arr_v)

d = enchant.Dict("ru_RU")
for i in arr:
    if len(i) != 0:
        if ',' in i:
            k = i.replace(',', '')
            if d.check(k):
                print(f'{k}')
            else:
                print(f"{k[0:2]}e{k[3:]}")
        else:
            if d.check(i):
                print(f'{i}')
            else:
                print(f"{i[0:2]}e{i[3:]}")