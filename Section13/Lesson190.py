from translate import Translator
translator= Translator(to_lang="he")
try:
    with open('textTranslate.txt',mode='r') as my_file:
        text= my_file.read()
        print(translator.translate(text))
except FileNotFoundError:
    print("OOPS")