from bot import dp, bot
import commands

commands.register_handlers(dp)

if __name__ == '__main__':
    dp.run_polling(bot, skip_updates=True)