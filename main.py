text="""Я вообще делаю, что хочу
Хочу импланты – звоню врачу
Кто меня не любит? Я вас не слышу
Вы просто мне завидуете, я молчу
Я не молчу, когда я хочу
Я не продаюсь, но за деньги – да
Мой продюсер говорит: "Ты – поп-звезда"
И, кстати, мой продюсер – это мой муж, да
Я не скажу в ответ ничего на хейт
И не скажу "Привет", если бабок нет
Слышу любимый звук, это звон монет
Они тянут сотни рук, это мой концерт
Не завожу подруг, но за деньги – да
Я не делаю фиты даже за деньги, да
Я подумаю потом, но скажу сразу "Да"
За деньги – да, за деньги – да
За деньги – да
За деньги – да
За деньги – да
За деньги – да
Это я в Дубае, я ща отдыхаю
Да, я так богата, и я это не скрываю
Все мои подруги за собой не замечают
Они видят мои шмотки и тупо повторяют
Пусть не забывают, кто тут королева
Я раскидываю бабки направо и налево
Это моя манера, жена миллионера
Мне платят за концерты, я читаю под фанеру
Эту сумку мне муж купил
Эти Ролексы муж купил
Кольцо с бриллиантом мне муж купил
Муж купил, мне муж купил
Не завожу подруг, но за деньги – да
Я не делаю фиты даже за деньги, да
Я подумаю потом, но скажу сразу "Да"
За деньги – да, за деньги – да
За деньги – да
За деньги – да
За деньги – да
За деньги – да"""
def prepare_text(text):
    text=text.lower()
    text=text.replace(':', '')
    text=text.replace('.', '')
    text=text.replace('-', '')
    text=text.replace(',', '')
    text=text.replace('\n', ' ')
    text=text.replace('?', '')
    text=text.replace('"', '')
    text=text.replace(' и ', ' ')
    return text

def split_text(prepared_text):
    return prepared_text.split()


def count_words(splitted_text):
  words={}
  for word in splitted_text:
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1
  return words

def generate_top(words) :
  top = []
  for i in range(10):
     max_value = 0
     max_key =''
     for k, v in words.items():
        if v > max_value:
          max_value = v
          max_key = k
     top.append(f'{max_key} :{max_value}')
     del words[max_key]
  return top
  
prepared_text = prepare_text(text)
splitted_text =split_text(prepared_text)
words=count_words(splitted_text)

#print(prepared_text)
#print(splitted_text)
#print(words)
print('Топ 10 слов:', generate_top(words))







