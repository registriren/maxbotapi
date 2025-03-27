from maxbotapi import BotHandler

token = 'access_token_masterbot'  # токен, полученный при создании бота в @MasterBot

bot = BotHandler(token)


def main():
    while True:  # цикл ожидания взаимодействия с ботом, в данном примере необходимо ввести любой текст
        last_update = bot.get_updates()  # получаем внутреннее представление сообщения (контента) отправленного боту (сформированного ботом)
        # тут можно вставить любые действия которые должны выполняться во время ожидания события
        if last_update:  # проверка на пустое событие, если пусто - возврат к началу цикла
            text = bot.get_text(last_update)  # получаем текст сообщения.
            chat_id = bot.get_chat_id(last_update)  # получаем chat_id в чате (или канале)
            link_user_id = bot.get_link_user_id(
                last_update)  # получаем link_user_id сообщения пользователя из чата (или канала), если он там был.
            if text == '/ban':
                bot.ban_member(chat_id, user_id=link_user_id)
                bot.send_message('Пользователь был удален и забанен.', chat_id)
        continue


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
