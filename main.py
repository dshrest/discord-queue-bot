import discord
from discord.ext import commands
import random


bot = commands.Bot(command_prefix='>', description="")

queue = []

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def d():
	"""Display the current queue"""
	await bot.say(stringify_queue())

@bot.command(pass_context=True)
async def r(ctx):
	"""Remove yourself or others from the queue
	>r to remove yourself
	>r [n] where [n] is the number to remove others"""
	rem = ctx.message.content.split(" ")
	print("rem:" + str(rem))
	if len(rem) == 2:
		index = int(rem[1])
		if index > 0 and index <= len(queue):
			del queue[index-1]
			msg = "Removed\n" + stringify_queue()
		else:
			msg = "Invalid number"
	else:
		print("remove:" + ctx.message.content)
		member = ctx.message.author.name
		queue.remove(member)
		msg = "Removed\n" + stringify_queue()

	await bot.say(msg)

@bot.command(pass_context=True)
async def q(ctx):
	"""Add yourself to the queue"""
	member = ctx.message.author
	print(ctx.message.author)
	msg = ""
	if member.name in queue:
		msg = "You're already in the queue"
	else:
		queue.append(member.name)
		print(queue)
		msg = "Added {0} to queue".format(member.name)
	await bot.say(msg)


def stringify_queue():
	if not queue:
		return "Queue is empty!"

	s = "The current queue is:\n------------------------------------------------------\n"
	for index, item in enumerate(queue):
		s += str(index+1) +": " + item + "\n"
	s += "------------------------------------------------------"
	return s


# @bot.event
# async def on_message(message):
# 	# we do not want the bot to reply to itself
# 	if message.author == bot.user:
# 		return

# 	if message.content.startswith('>q'):
		

bot.run('Mjk2MzY5Mjg2OTA4MzQ2MzY4.C7xO6g.wLFy-zgaGMSurPWgI6GhgTqObts')