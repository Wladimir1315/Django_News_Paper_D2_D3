from django import template
import os

register = template.Library()

@register.filter(name='Censor')
def Censor(value):
    BASE_DIR=os.getcwd()


    with open(os.path.join(BASE_DIR, 'news/templatetags/Censor_words.txt'), 'r', encoding='UTF8') as censor_words:
        censor_words = censor_words.readlines()[0].split(',')

    if isinstance(value, str):
        for word in censor_words:
            value = value.replace(word, '***CENSOR***')
        return str(value)



if __name__ == '__main__':
    pass