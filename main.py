VER = "1.0"
print("Версия бота:", VER)

#####################################################################

print("Запуск бота...")
import discord
import os
from discord.ext import commands

TOKEN = 'NzczMzgwMzAyODQzMjgxNDM4.X6IYiA.vhijupbAFovnSVsY_2JVOxwgjF8'
bot = commands.Bot(command_prefix='!')
@bot.command()
async def ban(ctx, user:discord.User):
	config = configparser.ConfigParser()
	author = ctx.author.name
	path = str(author + ".ini")
	config.read(path)
	login_cfg = config.get(ctx.author.name, "Login")
	type_cfg = config.get(ctx.author.name, "Type")
	if login_cfg == "True":
		if type_cfg == "root":
			await ctx.guild.ban(user)
			await ctx.send("Пользователь забанен.")
		elif type_cfg == "Admin":
			await ctx.guild.ban(user)
			await ctx.send("Пользователь забанен.")
		elif type_cfg == "Console":
			await ctx.guild.ban(user)
			await ctx.send("Пользователь забанен.")			
		else:
			await ctx.send("Недостаточно прав!")
	else:
		await ctx.send("Вы не авторизированы!")
@bot.command()
async def info(ctx):
	await ctx.send("Версия ядра:")
	await ctx.send(VER)
@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument ):
		await ctx.send("Отстутствуют аргументы!")
	elif isinstance(error, commands.CommandNotFound ):
		await ctx.send("Команды не существует!")

print("Подключение бота по токену")    
bot.run(TOKEN)