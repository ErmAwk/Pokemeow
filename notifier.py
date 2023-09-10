from playsound import playsound
from discord.ext import commands
from discord.ext.commands import CommandNotFound

bot = commands.Bot(command_prefix=';', self_bot=True, help_command=None)
meowid = 664508672713424926

@bot.listen('on_message')
async def on_message(message):
      if message.author.id == meowid and message.channel.id == 884302290314473503:
            if f"captcha" in message.content:
                  repeat = 0
                  while repeat != 3:
                        playsound('notification.mp3')
                        repeat += 1

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

bot.run('mfa.QNRIpaka3y0KWBflPwZWk6gZ0DDaZCt96rV_5DsG00uVhcZ_WM1urf_ma2wHd4Tj4Hy58v3BXYuOCS4M3vvK')