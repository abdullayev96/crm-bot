from telegram.ext import  Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup


BTN_TODAY, BTN_TOMORROW, BTN_MONTH, BTN_REGION, BTN_DUA  = ("⌛ Bugun "," ⏳ Ertaga ", "🗓 Toliq taqvim ","🌐 Mintaqa", "🤲 Duo ni korish ")
main_buttons = ReplyKeyboardMarkup([
    [BTN_TODAY], [BTN_TOMORROW,  BTN_MONTH], [BTN_REGION], [BTN_DUA]
], resize_keyboard=True)

STATE_REGION=1
STATE_CALENDAR=2

def start_handler(update, context):
    buttons = [
        [InlineKeyboardButton(text="Toshkent", callback_data="region_1"),InlineKeyboardButton(text="Andijon", callback_data="region_2")],
        [InlineKeyboardButton(text="Navoiy", callback_data="region_3"),InlineKeyboardButton(text="Samarqand", callback_data="region_4")],
        [InlineKeyboardButton(text="Jizzax", callback_data="region_5"),InlineKeyboardButton(text="Sirdaryo", callback_data="region_6")],
        [InlineKeyboardButton(text="Qashqadaryo", callback_data="region_7"),InlineKeyboardButton(text="Surxondaryo", callback_data="region_8")],


    ]
    user=update.message.from_user
    update.message.reply_html('Assalamu alaykum <b>{}!</b>\n \n<b>Ramozon oyi muborak bolsin</b>\n \n <b>Sizga qaysi mintaqa boyicha malumot beraylik 🌐 </b>'
                              .format(user.first_name),
                              reply_markup=InlineKeyboardMarkup(buttons))
    return STATE_REGION




def inline_button(update, context):
    try:
        query=update.callback_query
        query.message.delete()
        query.message.reply_html(text="<b>Ramozon taqvimi 2️⃣0️⃣2️⃣2️⃣\n \n Quyidagilardan birini tanlang 👇 </b>",
                                 reply_markup=main_buttons)
        return STATE_CALENDAR

    except Exception as e:
        print("error", str(e))


def calendar_today(update, context):
    update.message.reply_text("Bugun belgilandi")

def calendar_tomorrow(update, context):
    update.message.reply_text("Ertangi kun belgilandi")

def calendar_month(update, context):
    update.message.reply_text("Taqvim belgilandi")


def select_region(update, context):
    update.message.reply_text("Mintaqa belgilandi")

def select_dua(update, context):
    update.message.reply_text("Duo belgilandi")



def main():
    ## updater ni vazifasi telegram server bilan aloqa qiladi
    updater = Updater("5168783191:AAG_9O8wpy-pE5h-4o2qGoTXKeJYXxE-B30", use_context=True)
    ### dispatcher  hodisalrni aniqlash uchun ishlatiladi
    dispatcher = updater.dispatcher
    ###  start kamandasini  ushlab olish uchun
    #dispatcher.add_handler(CommandHandler('start', start_handler))
    #dispatcher.add_handler(CallbackQueryHandler(inline_button))

    conv_handler=ConversationHandler(
        entry_points=[CommandHandler('start', start_handler)],
        states={
            STATE_REGION:[CallbackQueryHandler(inline_button)],
            STATE_CALENDAR:[
                    MessageHandler(Filters.regex('^('+ BTN_TODAY +')$'),calendar_today),
                    MessageHandler(Filters.regex('^('+ BTN_TOMORROW +')$'), calendar_tomorrow),
                    MessageHandler(Filters.regex('^('+ BTN_MONTH +')$'), calendar_month),
                    MessageHandler(Filters.regex('^(' + BTN_REGION + ')$'),select_region),
                    MessageHandler(Filters.regex('^(' + BTN_DUA+ ')$'), select_dua)


            ],
        },
        fallbacks=[CommandHandler('start', start_handler)]

    )
    dispatcher.add_handler(conv_handler)


    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()