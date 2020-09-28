if user_can_changeinfo(chat, user, context.bot.id) == False: message.reply_text("You are missing the following rights to use this command:\n" "CanChangeInfo") return ""
