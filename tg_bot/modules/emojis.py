import html
import random
import time
from typing import List

from telegram import Bot, Update, ParseMode
from telegram.ext import run_async

from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler
from tg_bot.modules.helper_funcs.chat_status import is_user_admin, user_admin
from tg_bot.modules.helper_funcs.extraction import extract_user

#sleep how many times after each edit in 'love' 
EDIT_SLEEP = 1
#edit how many times in 'love' 
EDIT_TIMES = 10





#sleep how many times after each edit in 'bombs' 
EDIT_SLEEP = 1
#edit how many times in 'bombs' 
EDIT_TIMES = 9







#sleep how many times after each edit in 'hack' 
EDIT_SLEEP = 1
#edit how many times in 'hack' 
EDIT_TIMES = 10




#sleep how many times after each edit in 'moonanimation' 
EDIT_SLEEP = 1
#edit how many times in 'earthanimation' 
EDIT_TIMES = 18


#sleep how many times after each edit in 'moonanimation' 
EDIT_SLEEP = 1
#edit how many times in 'moonanimation' 
EDIT_TIMES = 32



#sleep how many times after each edit in 'moonanimation' 
EDIT_SLEEP = 1
#edit how many times in 'clockanimation' 
EDIT_TIMES = 11


EDIT_TIMES = 11



love_siren = [
            "❤️❤️❤️🧡🧡🧡💚💚💚\n💙💙💙💜💜💜🖤🖤🖤",
            "🖤🖤🖤💜💜💜💙💙💙\n❤️❤️❤️🧡🧡🧡💚💚💚",
            "💛💛💛💙💙💙❤️❤️❤️\n💜💜💜❤️❤️❤️🧡🧡🧡",
            "❤️❤️❤️🧡🧡🧡💚💚💚\n💙💙💙💜💜💜🖤🖤🖤",
            "🖤🖤🖤💜💜💜💙💙💙\n❤️❤️❤️🧡🧡🧡💚💚💚",
            "💛💛💛💙💙💙❤️❤️❤️\n💜💜💜❤️❤️❤️🧡🧡🧡",
            "❤️❤️❤️🧡🧡🧡💚💚💚\n💙💙💙💜💜💜🖤🖤🖤",
            "🖤🖤🖤💜💜💜💙💙💙\n❤️❤️❤️🧡🧡🧡💚💚💚",
            "💛💛💛💙💙💙❤️❤️❤️\n💜💜💜❤️❤️❤️🧡🧡🧡"
]


hack_you = [
            "Looking for WhatsApp databases in targeted person...",
            " User online: True\nTelegram access: True\nRead Storage: True ",
            "Hacking... 20.63%\n[███░░░░░░░░░░░░░░░░░]",    
            "Hacking... 86.21%\n[███████████████░░░░░]",
            "Hacking... 93.50%\n[█████████████████░░░]",
            "hacking....  100%\n[████████████████████]",
]




bomb_ettu = [
             "▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️",
             "💣💣💣💣\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️", 
             "▪️▪️▪️▪️\n💣💣💣💣\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️",
             "▪️▪️▪️▪️\n▪️▪️▪️▪️\n💣💣💣💣\n▪️▪️▪️▪️\n▪️▪️▪️▪️",
             "▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n💣💣💣💣\n▪️▪️▪️▪️",
             "▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n💣💣💣💣",
             "▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n💥💥💥💥",
             "▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n💥💥💥💥\n💥💥💥💥",
             "▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n😵😵😵😵",
]



moon_ani = [
            "🌗",
            "🌘",    
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",    
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",    
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",    
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖"
 ]



clock_ani = [
            "🕙",
            "🕘",    
            "🕗",
            "🕖",
            "🕕",
            "🕔",
            "🕓",
            "🕒",
            "🕑",
            "🕐",
            "🕛"

]








earth_ani = [
            "🌍",
            "🌎",
            "🌏",
            "🌍",
            "🌎",
            "🌏",
            "🌍",
            "🌎",
            "🌏",
            "🌍",
            "🌎",
            "🌏",
            "🌍",
            "🌎",
            "🌏",
            "🌍",
            "🌎",
            "🌏"
]







@user_admin
@run_async
def clockanimation(bot: Bot, update: Update):
    msg = update.effective_message.reply_text('🕛') 
    for x in range(EDIT_TIMES):
        msg.edit_text(clock_ani[x%11])
        time.sleep(EDIT_SLEEP)
    msg.edit_text('🕚')



@user_admin
@run_async
def earthanimation(bot: Bot, update: Update):
    msg = update.effective_message.reply_text('🌏') 
    for x in range(EDIT_TIMES):
        msg.edit_text(earth_ani[x%18])
        time.sleep(EDIT_SLEEP)
    msg.edit_text('🌍')




@user_admin
@run_async
def moonanimation(bot: Bot, update: Update):
    msg = update.effective_message.reply_text('🌚') 
    for x in range(EDIT_TIMES):
        msg.edit_text(moon_ani[x%32])
        time.sleep(EDIT_SLEEP)
    msg.edit_text('🌙')









@user_admin
@run_async
def bombs(bot: Bot, update: Update):
    msg = update.effective_message.reply_text('💣') 
    for x in range(EDIT_TIMES):
        msg.edit_text(bomb_ettu[x%9])
        time.sleep(EDIT_SLEEP)
    msg.edit_text('RIP PLOX...')











@user_admin
@run_async
def hack(bot: Bot, update: Update):
    msg = update.effective_message.reply_text('Target selected') 
    for x in range(EDIT_TIMES):
        msg.edit_text(hack_you[x%5])
        time.sleep(EDIT_SLEEP)
    msg.edit_text('successful hacked')








@user_admin
@run_async
def love(bot: Bot, update: Update):
    msg = update.effective_message.reply_text('❣️') 
    for x in range(EDIT_TIMES):
        msg.edit_text(love_siren[x%5])
        time.sleep(EDIT_SLEEP)
    msg.edit_text('പ്രണയം  😂 ')





__help__ = """

- /love ❣️

- /hack 👨‍💻

- /bombs 💣

- /moonanimation 🌚

- /clockanimation 🕛

- /earthanimation 🌍
"""



LOVE_HANDLER = DisableAbleCommandHandler("love", love)
HACK_HANDLER = DisableAbleCommandHandler("hack", hack)
BOMBS_HANDLER =DisableAbleCommandHandler("bombs",bombs)
MOONANIMATION_HANDLER =DisableAbleCommandHandler("moonanimation",moonanimation)
CLOCKANIMATION_HANDLER =DisableAbleCommandHandler("clockanimation",clockanimation)
EARTHANIMATION_HANDLER =DisableAbleCommandHandler("earthanimation",earthanimation)
dispatcher.add_handler(LOVE_HANDLER)
dispatcher.add_handler(HACK_HANDLER)
dispatcher.add_handler(BOMBS_HANDLER)
dispatcher.add_handler(EARTHANIMATION_HANDLER)
dispatcher.add_handler(MOONANIMATION_HANDLER)
dispatcher.add_handler(CLOCKANIMATION_HANDLER)


__mod_name__ = "EMOJIS"
__command_list__ = ["love", "hack", "bombs", "moonanimation", "clockanimation", "earthanimation"]
__handlers__ = [LOVE_HANDLER, HACK_HANDLER, BOMBS_HANDLER, MOONANIMATION_HANDLER, CLOCKANIMATION_HANDLER, EARTHANIMATION_HANDLER]
