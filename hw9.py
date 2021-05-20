address_book={}

def error_func(func):
    def inner(*args):
        try:
            result=func(*args)
            return result
        except:
            result=input_error()
            return result
    return inner   

#Приветствие по команде
def greeting():
    return 'How can I help you?'

#Выход из программы
def exit():
    print('Good bye, my lord!')
    esc=False
    return esc

#Распознает команды
@error_func
def handler(user_input):
    global user_list
    user_list=user_input.split()
    user_list[0]=user_list[0].lower()
    if user_list[0] in COMANDS.keys():
        return COMANDS[user_list[0]]()
    else:
        return input_error()

#Главная функция, ожидается ввод команды
def main():
    global user_input, user_list
    esc=True
    while esc:
        user_input=input('Enter your comand, please: \n')
        user_input=user_input.lower()
        result=handler(user_input)
        if result:
            print(result)
        elif result==None:
            pass
        else:
            break

#Ответная реакция на неизвестную команду
def input_error():
    return print('What`s going on?.. Enter correct comand or name. Or use "exit/close/good_bye" for exit')

#Показывает все контакты
@error_func       
def show_all():
    return print(f'Your contacts are: {address_book}')

#Показывает номер по имени
@error_func
def show_phone():
    return f'{user_list[1]}\'s number is {address_book[user_list[1]]}.'

#Добавляет контакт
@error_func
def add_contact():
    address_book[user_list[1]]=user_list[2]
    return f'{user_list[1]}\'s number {address_book[user_list[1]]} was added.'

#Вносит изменения в контакт
@error_func
def contact_change():
    address_book.update({user_list[1]: user_list[2]})
    return f"You've changed {user_list[1]}\'s number for {address_book[user_list[1]]}."     


#Набор команд, которые умеет выполнять бот
COMANDS={'hello': greeting,
          'add': add_contact,
          'change': contact_change,
          'phone': show_phone,
          'show_all': show_all,
          'good_bye': exit, 'close': exit, 'exit': exit,}

    
if __name__ =='__main__':
    main()
