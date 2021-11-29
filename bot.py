import telebot
from telebot.types import InputMediaPhoto
import time
import random
import requests
from temp_data import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import config
import base64
#***************************************
# from Youtube_src import y_srcs
# from Insta_src import i_srcs

# from get_photo_video import parse_photo

import in_out
#***************************************
from COMMANDS import cmds
# **************************************

# driver = webdriver.Chrome()
 
bot = telebot.TeleBot(config.token)

# @bot.message_handler(commands = ['debug'])
# def debugging(message):
#     link = input()
#     parse_photo_video(message, link)

def xpath_exists(xpath, link):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    try:
        driver.get('https://www.instagram.com')
        time.sleep(random.randrange(3, 5))
        time.sleep(10)
        username_input = driver.find_element_by_name('username')
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(2)

        password_input = driver.find_element_by_name('password')
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(10)
        
        driver.execute_script("window.open('about:blank', 'tab2');")
        driver.switch_to.window("tab2")
        driver.get(link)
        try:
            image = driver.find_element_by_xpath(xpath)
            exist = True
        except NoSuchElementException:
            exist = False
        time.sleep(10)
        driver.close()
        driver.quit()
        print(exist)
        return exist
    except Exception as ex:
        print(ex)
        driver.close()
        driver.quit()

# def parse_photo_video(message, link):
#     chrome_options = Options()
#     chrome_options.add_argument("--start-maximized")
#     driver = webdriver.Chrome(chrome_options=chrome_options)
#     driver.get('https://www.instagram.com')
#     time.sleep(random.randrange(3, 5))
#     time.sleep(10)
#     username_input = driver.find_element_by_name('username')
#     username_input.clear()
#     username_input.send_keys(username)

#     time.sleep(2)

#     password_input = driver.find_element_by_name('password')
#     password_input.clear()
#     password_input.send_keys(password)

#     password_input.send_keys(Keys.ENTER)
#     time.sleep(10)
        
#     driver.execute_script("window.open('about:blank', 'tab2');")
#     driver.switch_to.window("tab2")
#     driver.get(link)
    
#     image_xpath = "//div[@class = 'KL4Bh']/img"

#     video_xpath = "//div[@class = '_5wCQW']/video"
#     time.sleep(10)
#     # print(driver.find_element_by_xpath(image_xpath).get_attribute('src'))
#     # if xpath_exists(image_xpath, link) == True:
#     #     image = driver.find_element_by_xpath(image_xpath)
        
#     #     src = image.get_attribute('src')
        
#     #     print(src)

#     #     driver.close()
#     #     get_img = requests.get(src)
#     #     with open("temp_photo.img", "wb") as img_file:
#     #         img_file.write(get_img.content)
            
#     #     file = open('temp_photo.img', 'rb')
#     #     bot.send_message(message.chat.id, 'Working with photo')
#     #     bot.send_photo(message.chat.id, file)
#     # elif xpath_exists(video_xpath, link) == True:
#     video = driver.find_element_by_xpath(video_xpath)
#     print("VIDEO!!!")
#     src = video.get_attribute('src')
#         # hrefs = src.split("blob:")
        
#     print(src)
#     driver.close()
#     get_video = requests.get(src, stream=True)
#     # get_video = get_file_content_chrome(driver, src)
#     with open("temp_video.mp4", "wb") as video_file:
#         for chunk in get_video.iter_content(chunk_size=2048 * 2048):
#             if chunk:
#                 video_file.write(chunk)

#     file = open('temp_video.mp4', 'rb')
#     bot.send_message(message.chat.id, 'Working with video')
#     bot.send_video(message.chat.id, file)

#     # else:
#     #     bot.send_message(message.chat.id, 'Something wrong with page.')
#     driver.quit()
#     # bot.send_message(message.chat.id, image)
    
# def get_file_content_chrome(driver, uri):
#   result = driver.execute_async_script("""
#     var uri = arguments[0];
#     var callback = arguments[1];
#     var toBase64 = function(buffer){for(var r,n=new Uint8Array(buffer),t=n.length,a=new Uint8Array(4*Math.ceil(t/3)),i=new Uint8Array(64),o=0,c=0;64>c;++c)i[c]="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".charCodeAt(c);for(c=0;t-t%3>c;c+=3,o+=4)r=n[c]<<16|n[c+1]<<8|n[c+2],a[o]=i[r>>18],a[o+1]=i[r>>12&63],a[o+2]=i[r>>6&63],a[o+3]=i[63&r];return t%3===1?(r=n[t-1],a[o]=i[r>>2],a[o+1]=i[r<<4&63],a[o+2]=61,a[o+3]=61):t%3===2&&(r=(n[t-2]<<8)+n[t-1],a[o]=i[r>>10],a[o+1]=i[r>>4&63],a[o+2]=i[r<<2&63],a[o+3]=61),new TextDecoder("ascii").decode(a)};
#     var xhr = new XMLHttpRequest();
#     xhr.responseType = 'arraybuffer';
#     xhr.onload = function(){ callback(toBase64(xhr.response)) };
#     xhr.onerror = function(){ callback(xhr.status) };
#     xhr.open('GET', uri);
#     xhr.send();
#     """, uri)
#   if type(result) == int :
#     raise Exception("Request failed with status %s" % result)
#   return base64.b64decode(result)
 

@bot.message_handler(commands=['start'])
def start(message):
    # a = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "Привет! Этот бот поможет тебе получить информацию с конкретного источника! Для помощи - /help")
        
@bot.message_handler(commands = ['help'])
def help_user(message):
    for cmd in cmds:
        bot.send_message(message.chat.id, f"{cmd} - {cmds[cmd]}")

# *************************************************
@bot.message_handler(commands=['Youtube_parsing'])
def search_channel(message):
    bot.send_message(message.chat.id, "Что вы хотите сделать?")
    bot.send_message(message.chat.id, """ 
    /search_existing_youtube_src - Поиск по всем существующим источникам YouTube
/add_new_youtube_source - Добавить новый источник YouTube
/view_youtube_sources - Просмотеть источники YouTube
    """)

@bot.message_handler(commands = ['view_youtube_sources'])
def viewinging_youtube(message):
    y_srcs = in_out.read_from_file('youtube')
    for i in range(len(y_srcs)):
        if y_srcs[i] == '':
            continue
        keyboard = telebot.types.InlineKeyboardMarkup(row_width = 2)
        keyboard.add(telebot.types.InlineKeyboardButton(text = 'Удалить источник', callback_data = 'delete_y'))
        keyboard.add(telebot.types.InlineKeyboardButton(text = 'Поиск по данному источнику', callback_data = 'search_y'))
        bot.send_message(message.chat.id, f"{y_srcs[i]}", reply_markup = keyboard)

@bot.callback_query_handler(func = lambda call: call.data == 'delete_y' or call.data == 'search_y')
def deleting_y_srcr(call):
    y_srcs = in_out.read_from_file('youtube')
    if call.data == 'delete_y':
        y_srcs.remove(call.message.text)
        bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.id, text = f"""Источник успешно удален
            {call.message.text}""")
        str = y_srcs[0]
        for i in range(len(y_srcs)):
            if i == 0:
                continue
            if y_srcs[i] == '':
                continue
            str += f', {y_srcs[i]}'
        in_out.write_to_file('youtube', str)
        # bot.send_message(call.message.chat.id, "Источник успешно удален")
    if call.data == 'search_y':
        searching_from_channel(call.message, call.message.text)

@bot.message_handler(commands = ['search_existing_youtube_src'])
def search_exist_youtube(message):
    y_srcs = in_out.read_from_file('youtube')
    print(y_srcs)
    if not y_srcs:
        bot.send_message(message.chat.id, 'Список источников пуст. /add_new_youtube_source - Для добавления нового источника.')
    else:
        for i in range(len(y_srcs)):
            if y_srcs[i] == '':
                continue
            searching_from_channel(message, y_srcs[i])

@bot.message_handler(commands = ['add_new_youtube_source'])
def ask_youtube_src(message):
    mssg = bot.send_message(message.chat.id, "Введите ссылку на YouTube канал.")
    bot.register_next_step_handler(mssg, add_youtube)

def add_youtube(message):
    y_srcs = in_out.read_from_file('youtube')
    if not 'www.youtube.com' in message.text:
        bot.send_message(message.chat.id, """Данное сообщение не является ссылкой на YouTube-канал!
/add_new_youtube_source - для добавления нового источника. Удостоверьтесь в правильности ссылки!
        """)
    else:
        flag = 0
        for i in y_srcs:
            if message.text == i:
                flag = 1
                bot.send_message(message.chat.id, "Данный источник уже существует!")
                break
        if flag == 0:
            y_srcs.append(message.text)
            print(y_srcs)
            bot.send_message(message.chat.id, "Источник сохранен, /search_existing_youtube_src - Для поиска по всем существующим источникам YouTube")
            str = y_srcs[0]
            for i in range(len(y_srcs)):
                if i == 0:
                    continue
                if y_srcs[i] == '':
                    continue
                print(y_srcs[i])
                str += f', {y_srcs[i]}'
            in_out.write_to_file('youtube', str)

def searching_from_channel(message, link):
    bot.send_message(message.chat.id, "Начинаю поиск")
    href = SFY(link)
    for i in href:
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text = 'Отправить сообщение в канал', callback_data = 'send_y'))
        bot.send_message(message.chat.id, i, reply_markup = keyboard)


    """
    driver.get(message.text + "/videos")
    videos = driver.find_elements_by_id("video-title")
    for i in range(len(videos)):
        bot.send_message(message.chat.id, videos[i].get_attribute('href'))
        if i == 10:
            break
    """

@bot.callback_query_handler(func = lambda call: call.data == 'send_y')
def send_news_to_channel(call):
    print(call)
    if call.data == 'send_y':
        # mssg = bot.send_message(call.message.chat.id, 'Введите описание для видео, если необходимо. Введите \"0\",если описание не требуется')
        
        result = channel_send(call.message.text, 'youtube')
        print(result)
        
        if result == 1:
            bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.id, text = f"""Сообщение отправлено 
            {call.message.text}""")
        else:
            print('Error')



def SFY(message_text):
    driver = webdriver.Chrome()
    driver.get(message_text + "/videos")
    videos = driver.find_elements_by_id("video-title")
    href = []
    for i in range(len(videos)):
        href.append(videos[i].get_attribute('href'))
        if i == 9:
            break
    driver.close()
    return href


# *************************************************

# def get_description(message):
#     return message.text

def channel_send(chat_id, message_text, socialnet):
    channel_id = "@mmtlgkasdf"
    
    if socialnet == 'youtube':
        # driver = webdriver.Chrome()
        # driver.get(message_text)
        # dscrptn = driver.find_element_by_xpath("//span[@class = 'style-scope yt-formatted-string']")
        # print(dscrptn)
        # print(dscrptn.text)

        # mssg = bot.send_message(chat_id, 'Введите описание для видео, если необходимо. Введите \"0\",если описание не требуется')
        # description = bot.register_next_step_handler(mssg, get_description)

        # bot.send_message(channel_id, description)
        bot.send_message(channel_id, message_text)
        return 1
        # driver.close()
    if socialnet == 'instagram':
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(chrome_options=chrome_options)

        try:
            driver.get('https://www.instagram.com')
            time.sleep(random.randrange(3, 5))

            username_input = driver.find_element_by_name('username')
            username_input.clear()
            username_input.send_keys(username)

            time.sleep(2)

            password_input = driver.find_element_by_name('password')
            password_input.clear()
            password_input.send_keys(password)

            password_input.send_keys(Keys.ENTER)
            time.sleep(15)
                
            driver.execute_script("window.open('about:blank', 'tab2');")
            driver.switch_to.window("tab2")
            driver.get(message_text)
            time.sleep(5)
            xpath = "//div[@class = 'C4VMK']/span"
            elem = driver.find_element_by_xpath(xpath)

            content = elem.text
            print(elem)
            print("\n")
            print(content)

            # driver.execute_script("window.open('about:blank', 'tab3');")
            # driver.switch_to.window("tab3")
            
            # driver.get(message_text)
            time.sleep(10)        
            
            image_xpath = "//div[@class = 'KL4Bh']/img"

            video_xpath = "//div[@class = '_5wCQW']/video"
            # img_exist = False
            # video_exist = False
            # print(f"IMG {driver.find_element_by_xpath(image_xpath)}")
            # print(f"VIDEO {driver.find_element_by_xpath(video_xpath)}")
            # if driver.find_element_by_xpath(image_xpath) != None:
            # # try:
            # #     image = driver.find_element_by_xpath(image_xpath)
            #     img_exist = True
            # # except NoSuchElementException:
            # #     img_exist = False
            # if driver.find_element_by_xpath(video_xpath) != None:
            # # try:
            # #     video = driver.find_element_by_xpath(video_xpath)
            #     video_exist = True
            # # except NoSuchElementException:
            # #     video_exist = False

            # print(img_exist)
            # print(video_exist)
            
        
                    
            # print(driver.find_element_by_xpath(image_xpath).get_attribute('src'))
            if xpath_exists(image_xpath, message_text) == True:
            # if img_exist == True:
                driver.execute_script("window.open('about:blank', 'tab3');")
                driver.switch_to.window("tab3")

                driver.get(message_text)
                images = driver.find_elements_by_xpath(image_xpath)
                
                media_files = []
                i = 0

                for image in images:
                    src = image.get_attribute('src')
                    
                    print(src)

                    driver.close()
                    get_img = requests.get(src)
                    with open("temp_photo.img", "wb") as img_file:
                        img_file.write(get_img.content)
                        
                    file = open('temp_photo.img', 'rb')
                    if i == 0:
                        media_files.append(InputMediaPhoto(file, caption = content))
                        i += 1
                    else:
                        media_files.append(InputMediaPhoto(file))
                        i += 1
                    bot.send_message(chat_id, 'Working with photo')
                    # bot.send_photo(chat_id, file)
                bot.send_media_group(channel_id, media_files)
                    # bot.send_photo(channel_id, file, caption = content)
                driver.quit()
            # elif xpath_exists(video_xpath, message_text) == True:
            else: 
                bot.send_message(channel_id, f"""
                {content}
                {message_text}
                """)
            # # elif video_exist == True:
            #     driver.execute_script("window.open('about:blank', 'tab3');")
            #     driver.switch_to.window("tab3")
            
            #     driver.get(message_text)
            #     video = driver.find_element_by_xpath(video_xpath)
            #     print("VIDEO!!!")
            #     src = video.get_attribute('src')

            #     print(src)
            #     get_video = requests.get(src, stream=True)

            #     with open("temp_video.mp4", "wb") as video_file:
            #         for chunk in get_video.iter_content(chunk_size=1024 * 1024):
            #             if chunk:
            #                 video_file.write(chunk)

            #     file = open('temp_video.mp4', 'rb')
            #     bot.send_message(chat_id, 'Working with video')
            #     # bot.send_video(chat_id, file)
            #     bot.send_video(channel_id, file, caption = content)
            #     driver.quit()

            # else:
            #     bot.send_message(chat_id, 'Something wrong with page.')
            #     driver.quit()
        # driver.close()
        # driver = webdriver.Chrome()
        # driver.get(message_text)
        # dscrptn = driver.find_element_by_xpath("//div[@class = 'C4VMK']/span")
        # print(dscrptn)
        # print(dscrptn.get_attribute("textContent"))
        # bot.send_message(channel_id, message_text)
        # driver.close()
            return 1
        except Exception as ex:
            print(ex)
            # driver.close()
            driver.quit()
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
        
    """
    try:
        url = "https://api.telegram.org/bot" + config.token + "/sendMessage"
        channel_name = '@mmtlgkasdf'

        r = requests.post(url, data = {
            "chat_id": channel_name,
            "text": message_text
        })
        return 1
    except:
        print("Error")
        return 0
    """

# *************************************************


@bot.message_handler(commands=['Instagram_parsing'])
def search_channel(message):
    bot.send_message(message.chat.id, "Что вы хотите сделать?")
    bot.send_message(message.chat.id, """ 
    /search_existing_instagram_src - Поиск по всем существующим источникам Instagram
/add_new_instagram_source - Добавить новый источник Instagram
/view_instagram_sources - Просмотр существующих источников Instagram
    """)

@bot.message_handler(commands = ['view_instagram_sources'])
def viewing_instagram(message):
    i_srcs = in_out.read_from_file('instagram')
    for i in range(len(i_srcs)):
        if i_srcs[i] == '':
            break
        keyboard_ = telebot.types.InlineKeyboardMarkup()
        keyboard_.add(telebot.types.InlineKeyboardButton(text = 'Удалить источник', callback_data = 'delete_i'))
        keyboard_.add(telebot.types.InlineKeyboardButton(text = 'Поиск по данному источнику', callback_data = 'search_i'))
        bot.send_message(message.chat.id, f"{i_srcs[i]}", reply_markup = keyboard_)

@bot.callback_query_handler(func = lambda call: call.data == 'delete_i' or call.data == 'search_i')
def deleting_i_srcr(c):
    i_srcs = in_out.read_from_file('instagram')
    if c.data == 'delete_i':
        i_srcs.remove(c.message.text)
        bot.edit_message_text(chat_id = c.message.chat.id, message_id = c.message.id, text = f"""Источник успешно удален
            {c.message.text}""")
        str = i_srcs[0]
        for i in range(len(i_srcs)):
            if i == 0:
                continue
            if i_srcs[i] == '':
                continue
            str += f', {i_srcs[i]}'
        in_out.write_to_file('instagram', str)
        # bot.send_message(call.message.chat.id, "Источник успешно удален")
    if c.data == 'search_i':
        print(c.message.text)
        searching_from_instagram(c.message, c.message.text)

@bot.message_handler(commands = ['search_existing_instagram_src'])
def search_exist_instagram(message):
    i_srcs = in_out.read_from_file('instagram')
    print(i_srcs)
    if not i_srcs:
        bot.send_message(message.chat.id, 'Список источников пуст. /add_new_instagram_source - Для добавления нового источника')
    else:
        for i in range(len(i_srcs)):
            if i_srcs[i] == '':
                break
            searching_from_instagram(message, i_srcs[i])

@bot.message_handler(commands = ['add_new_instagram_source'])
def ask_insta_src(message):
    mssg = bot.send_message(message.chat.id, "Введите ссылку на страницу Instagram")
    bot.register_next_step_handler(mssg, add_instagram)
    
def add_instagram(message):
    i_srcs = in_out.read_from_file('instagram')
    if not 'www.instagram.com' in message.text:
        bot.send_message(message.chat.id, """Данное сообщение не является ссылкой на страницу Instagram! 
/add_new_instagram_source - для добавления нового источника. Удостоверьтесь в правильности ссылки!
        """)
    else:
        flag = 0
        for i in i_srcs:
            if message.text == i:
                bot.send_message(message.chat.id, "Данный источник уже существует!")
                flag = 1
                break
        if flag == 0:    
            i_srcs.append(message.text)
            print(i_srcs)
            bot.send_message(message.chat.id, "Источник сохранен, /search_existing_instagram_src - Для поиска по всем существующим источникам Instagram")
            str = i_srcs[0]
            for i in range(len(i_srcs)):
                if i == 0:
                    continue
                if i_srcs[i] == '':
                    continue
                str += f', {i_srcs[i]}'
            in_out.write_to_file('instagram', str)

def searching_from_instagram(message, link):
    bot.send_message(message.chat.id, "Начинаю поиск")    
    href = SFI(link)
    for i in href:
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text = 'Отправить сообщение в канал', callback_data = 'send_i'))
        bot.send_message(message.chat.id, i, reply_markup = keyboard)


@bot.callback_query_handler(func = lambda call: call.data == 'send_i')
def send_news_to_channel(call):
    if call.data == 'send_i':
        bot.send_message(call.message.chat.id, "Пожалуйста, ожидайте. Чтобы инстаграм не воспринял меня, как бота, необходимо подождать некоторое время.")
        time.sleep(10)
        result = channel_send(call.message.chat.id, call.message.text, 'instagram')
        # print(result)
        
        if result == 1:
            bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.id, text = f"""Сообщение отправлено 
            {call.message.text}""")
        else:
            print('Error')
        
        

    

def SFI(message_text):
    driver = webdriver.Chrome()
    driver.get(message_text)  
    links = driver.find_elements_by_xpath("//div[@class = 'v1Nh3 kIKUG  _bz0w']/a")
    href = []
    for i in range(len(links)):
        href.append(links[i].get_attribute('href'))
    driver.close()
    return href

# *************************************************
        
        
 
 
@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, "Введите команду")
 
 
bot.polling()

"""
if __name__ == '__main__':
    bot.infinity_polling()
"""