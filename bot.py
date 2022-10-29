# -*- coding: utf-8 -*-
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler)
from config import token
import user_interface as ui
import model_sum as sum
import model_sub as sub
import model_mult as mult
import model_div as div
import model_pow as pow
# import logger as log

select_main_menu = 0
num1 = 0
num2 = 0

def start(update, _):
    update.message.reply_text('1 - Рациональные числа; \n2 - Комплексные числа; \n3 - выход\n')
    return menu_digit

def menu_digit(update, context):
    set_menu_digit = update.message.text
    if set_menu_digit == '1':
        return request_rat_number_1(update, context)
    elif set_menu_digit == '2':
        return request_compl_number_1(update, context)
    elif set_menu_digit == '3':
        update.message.reply_text('До свидания!')
        return ConversationHandler.END
    else:
        update.message.reply_text('Введено не верное значение')
        return ConversationHandler.END

def request_rat_number_1(update, context):
    update.message.reply_text('Введите первое рациональное число ')
    return input_rat_number_1

def input_rat_number_1(update, context):
    global num1
    num_1 = update.message.text
    if num_1.isdigit() == False:
        update.message.reply_text('Введено не верное значение')
        return ConversationHandler.END
    num1 = float(num_1)
    return request_rat_number_2(update, context)

def request_rat_number_2(update, context):
    update.message.reply_text('Введите второе рациональное число ')
    return input_rat_number_2

def input_rat_number_2(update, context):
    global num2
    num_2 = update.message.text
    if num_2.isdigit() == False:
        update.message.reply_text('Введено не верное значение')
        return ConversationHandler.END
    num2 = float(num_2)
    ui.print_menu(update, 'Меню операций', ui.load_menu_operation())
    update.message.reply_text('Выберите действие ')
    return operations

def request_compl_number_1(update, context):
    update.message.reply_text('Введите первое комплексное число в виде X+Yj')
    return input_compl_number_1

def input_compl_number_1(update, context):
    global num1
    num_1 = update.message.text
    num1 = complex(num_1)
    return request_compl_number_2(update, context)

def request_compl_number_2(update, context):
    update.message.reply_text('Введите второе комплексное число в виде X+Yj')
    return input_compl_number_2

def input_compl_number_2(update, context):
    global num2
    num_2 = update.message.text
    num2 = complex(num_2)
    ui.print_menu(update, 'Меню операций', ui.load_menu_operation())
    update.message.reply_text('Выберите действие ')
    return operations

def operations(update, context):
    set_operations = update.message.text
    if set_operations.isdigit() == False:
        update.message.reply_text('Введено не верное значение')
        return ConversationHandler.END
    if set_operations == '1':
        result = sum.sum(num1, num2)
        update.message.reply_text(f'{num1} + {num2} = {result}')
    elif set_operations == '2':
        result = sub.sub(num1, num2)
        update.message.reply_text(f'{num1} - {num2} = {result}')   
    elif set_operations == '3':
        result = mult.mult(num1, num2)
        update.message.reply_text(f'{num1} * {num2} = {result}')
    elif set_operations == '4':
        ui.print_menu(update, 'Меню операций', ui.load_menu_operation_div())
        update.message.reply_text('Выберите действие ')
        return operation_div
    elif set_operations == '5':
        result = pow.pow(num1, num2)
        update.message.reply_text(f'{num1} ** {num2} = {result}')
    else:
        update.message.reply_text('Введено не верное значение')
        return ConversationHandler.END
    
def operation_div(update, context):
    set_operations = update.message.text
    if set_operations == '1':
        result = div.div(num1, num2)
        update.message.reply_text(f'{num1} / {num2} = {result}')
    if set_operations == '2':
        result = div.int_div(num1, num2)
        update.message.reply_text(f'{num1} // {num2} = {result}')
    if set_operations == '3':
        result = div.rem_div(num1, num2)
        update.message.reply_text(f'{num1} % {num2} = {result}')

if __name__ == '__main__':
    updater = Updater(token)
    dispatcher = updater.dispatcher
    conversation_handler = ConversationHandler(  
        entry_points=[CommandHandler('start', start)],
        states={menu_digit: [MessageHandler(Filters.text, menu_digit)],
                request_rat_number_1: [MessageHandler(Filters.text, request_rat_number_1)], 
                input_rat_number_1: [MessageHandler(Filters.text, input_rat_number_1)],
                request_rat_number_2: [MessageHandler(Filters.text, request_rat_number_2)], 
                input_rat_number_2: [MessageHandler(Filters.text, input_rat_number_2)],
                request_compl_number_1: [MessageHandler(Filters.text, request_compl_number_1)], 
                input_compl_number_1: [MessageHandler(Filters.text, input_compl_number_1)],
                request_compl_number_2: [MessageHandler(Filters.text, request_compl_number_2)], 
                input_compl_number_2: [MessageHandler(Filters.text, input_compl_number_2)],
                operations: [MessageHandler(Filters.text, operations)],
                operation_div: [MessageHandler(Filters.text, operation_div)]}, fallbacks=[])
    dispatcher.add_handler(conversation_handler)
    updater.start_polling()
    updater.idle()
