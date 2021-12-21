from botapitamtam import BotHandler
import time

token = 'vIdhiW6OX2qYfcwoKaatxqiEDdjeqRgxgj56v-8I9ws'  # токен, полученный при создании бота в @PrimeBot

bot = BotHandler(token)


def main():
    n = 0
    chat_id = bot.get_chat_id()  # Получаем chat_id последнего активного диалога с ботом
    bot.send_message("Напишите любое сообщение", chat_id)
    while True:
        last_update = bot.get_updates()  # получаем внутреннее представление сообщения (контента) отправленного боту (сформированного ботом)
        # тут можно вставить любые действия которые должны выполняться во время ожидания события
        if last_update:  # проверка на пустое событие, если пусто - возврат к началу цикла
            chat_id = bot.get_chat_id(last_update)  # получаем chat_id диалога с ботом
            type = bot.get_update_type(last_update)
            callback_id = bot.get_callback_id(last_update)
            if type == 'message_created':
                buttons = bot.button_callback('\U0001F44D[0]', 'like')  # готовим кнопку
                #buttons2 = bot.button_callback('\U0001F44E[0]', 'dislike')
                bot.send_buttons('text test', buttons, chat_id)
            if type == 'message_callback':
                if callback_id:
                    n += 1
                    key = bot.button_callback('\U0001F44D[{}]'.format(n), 'ok')  # готовим кнопку
                    attach = bot.attach_buttons(key)  # при необходимости можно добавить еще attach путем сложения
                    text = time.ctime()
                    bot.send_answer_callback(callback_id, 'test well...',
                                             attachments=attach)  # выводим кратковременное уведомление и
                    # скорректированное событие по его callback_id


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
