
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import hi_command
from bot_commands import time_command
from bot_commands import help_command
from bot_commands import sum_command

app = ApplicationBuilder().token("5924736461:AAHyjUG9LH3WdWrY9SIPRAxScaXYx4GsqQE").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

print('server start')
app.run_polling()



