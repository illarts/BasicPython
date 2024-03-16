text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO

# delete , and . from text
text = text.replace(',', '')
text = text.replace('.', '')

text_str = text.split()

int_list = list(map(len,text_str))#文字数を数えたリストを作る

pi = [str(a) for a in int_list]#文字列に変換

pi = " ".join(pi)

answer = pi.replace(' ','')
print(answer)
