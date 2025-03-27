# этот пример показывает как можно сформировать и изменить совокупный контент

from maxbotapi import BotHandler
import time

token = 'access_token_masterbot'  # токен, полученный при создании бота в @MasterBot

bot = BotHandler(token)

def main():
    while True:
        last_update = bot.get_updates()  # получаем внутреннее представление сообщения (контента) отправленного боту (сформированного ботом)
        # тут можно вставить любые действия которые должны выполняться во время ожидания события
        if last_update:
            chat_id = bot.get_chat_id(last_update)

            cont_img = 'test.png'     # тестовый файл изображения в рабочем каталоге
            cont_video = 'movie.mp4'  # тестовый файл видео в рабочем каталоге

            button1 = bot.button_link('Открыть mail.ru', 'http://mail.ru') # готовим первую кнопку
            button2 = bot.button_link('Открыть ok.ru', 'http://ok.ru') # готовим вторую кнопку
            buttons = [button1, button2] # формируем кнопки в строку

            image = bot.attach_image(cont_img)    # подготовка изображения к совокупной отправке
            video = bot.attach_video(cont_video)  # подготовка видео к совокупной отправке
            key = bot.attach_buttons(buttons)     # подготовка кнопки к совокупной отправке

            attach = image + video + key

            upd = bot.send_message('текст начальный', chat_id, attachments=attach) # совокупная отправка контента
            mid = bot.get_message_id(upd) # получаем идентификатор отправленного контента

            upd = bot.send_message('Через 5 сек. всё изменится...', chat_id)
            mid1 = bot.get_message_id(upd)
            time.sleep(2)
            bot.delete_message(mid1)
                # готовим контент к изменению
            cont_img = 'test2.png' # файл должен быть в рабочем каталоге
            cont_video = 'voko.mkv' # файл должен быть в рабочем каталоге

            button1 = bot.button_callback('Новая кнопка 1', 'short')
            button2 = bot.button_callback('Новая кнопка 2', 'long')
            buttons = [[button1], [button2]] # формируем кнопки в колонку

            image = bot.attach_image(cont_img)
            video = bot.attach_video(cont_video)
            key = bot.attach_buttons(buttons)

            attach = image + video + key

            bot.edit_message(mid, 'ТЕКСТ ИЗМЕНЁННЫЙ', attachments=attach) # изменяем загруженный контент
        continue


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
