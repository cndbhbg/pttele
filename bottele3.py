import telebot
import csv

API_KEY = "6129259234:AAH6aqvleysBxb-h_iwC9g1qUMxZgwHnPfs"

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Chào bạn, tôi có thể giúp gì.")

@bot.message_handler(commands=['Trợ giúp'])
def help(message):
    bot.reply_to(message, "Tôi hỗ trợ bạn theo các lệnh sau: \n /start \n /info \n /Trợ giúp: \n /status \n /news <2>: tin tức <số bài viết>")

@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message, "Tôi là 1 robot thông tin, tạo bởi Phòng Công nghiệp, sở KHĐT Điện Biên.")

@bot.message_handler(commands=['status'])
def status(message):
    bot.reply_to(message, "Tôi đang sẵn sàng.")
    
#---------Tin tức
def laytin():
    tin=[]
#     reader=()
    with open("tintuc.csv",mode="r",encoding="utf-8") as file:
        reader=csv.reader(file)
        for row in reader:
            tin.append(", ".join(row))
    return tin
    #          print(", ".join(row))

@bot.message_handler(commands=['news'])
def news(message):
    args = message.text.split()[1:]
    count = 10  # Giá trị mặc định của biến j
    if len(args) > 0:  # Nếu có argument được truyền vào
        try:
            count = int(args[0])  # Thử chuyển đổi giá trị argument thành số nguyên
        except ValueError:
            pass  # Nếu không thành công thì giá trị của j vẫn là 10
    j = 0
    for i in laytin():
        bot.reply_to(message, "Tin tức mới nhất: " + i)
        j += 1
        if j >= count:
            break
bot.polling()