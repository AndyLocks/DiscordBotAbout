from random import randint
from discord.ext import commands
from discord import app_commands 
import discord 

from basa import *

bot = commands.Bot(command_prefix = '.', intents = discord.Intents.all())
a = Basa("basa.json")

@bot.hybrid_command(name = "about", description = "about user")
async def about(ctx, user = ""):
    if user == "": user = str(ctx.author.id)
    else:
        try:
            user = user.replace("<@", "")
            user = user.replace(">", "")
        except:
            emb = discord.Embed(title = "error", colour = 11110385)
            await ctx.send(embed = emb, ephemeral = True)
    if a.user_in(user=user):
        emb = discord.Embed(title = a.get_title(user=user), colour = a.get_color(user=user), url = a.get_url(user=user), description=a.get_description(user=user))
        if a.get_author(user=user) != None:    
            emb.set_author(name=a.get_author(user=user), url=a.get_author_url(user=user), icon_url=a.get_author_icon(user=user))
        emb.set_thumbnail(url=a.get_image_thumbnail(user=user))
        emb.set_footer(text=a.get_footer(user=user), icon_url=a.get_footer_icon(user=user))
        emb.set_image(url=a.get_image(user=user))
        await ctx.send(embed = emb, ephemeral = True)
    else:
        emb = discord.Embed(title = "You are not in database", colour = 11110385)
        await ctx.send(embed = emb, ephemeral = True)

@bot.command()
async def setTitle(ctx, *text):
    user = str(ctx.author.id)
    if not a.user_in(user=user):
        a.make_new(user=user)
    a.set_title(user=user, mean=" ".join(list(text)))
    await ctx.message.add_reaction("✅")

@bot.command()
async def setText(ctx, *text):
    user = str(ctx.author.id)
    if not a.user_in(user=user):
        a.make_new(user=user)
    a.set_description(user=user, mean=" ".join(list(text)))
    await ctx.message.add_reaction("✅")

@bot.command()
async def setUrl(ctx, *text):
    user = str(ctx.author.id)
    if not a.user_in(user=user):
        a.make_new(user=user)
    a.set_url(user=user, mean=" ".join(list(text)))
    await ctx.message.add_reaction("✅")

@bot.command()
async def setAuthor(ctx, *text):
    user = str(ctx.author.id)
    if not a.user_in(user=user):
        a.make_new(user=user)
    a.set_author(user=user, mean=" ".join(list(text)))
    await ctx.message.add_reaction("✅")

@bot.command()
async def setAuthorIcon(ctx, *text):
    user = str(ctx.author.id)
    if not a.user_in(user=user):
        a.make_new(user=user)
    a.set_author_icon(user=user, mean=" ".join(list(text)))
    await ctx.message.add_reaction("✅")

@bot.command()
async def setAuthorUrl(ctx, *text):
    user = str(ctx.author.id)
    if not a.user_in(user=user):
        a.make_new(user=user)
    a.set_author_url(user=user, mean=" ".join(list(text)))
    await ctx.message.add_reaction("✅")

@bot.command()
async def setImage(ctx, url = ""):
    user = str(ctx.author.id)
    if url == "" and len(ctx.message.attachments) == 0:
        url = None
    elif len(ctx.message.attachments) != 0:
        url = ctx.message.attachments[0].url
    if not a.user_in(user=user):
        a.make_new(user=user)
    a.set_image(user=user, mean=url)
    await ctx.message.add_reaction("✅")

@bot.command()
async def setImageThumbnail(ctx, url = ""):
    user = str(ctx.author.id)
    if url == "" and len(ctx.message.attachments) == 0:
        url = None
    elif len(ctx.message.attachments) != 0:
        url = ctx.message.attachments[0].url
    if not a.user_in(user=user):
        a.make_new(user=user)
    a.set_image_thumbnail(user=user, mean=url)
    await ctx.message.add_reaction("✅")

@bot.command()
async def setFooter(ctx, *text):
    user = str(ctx.author.id)
    if not a.user_in(user=user):
        a.make_new(user=user)
    a.set_footer(user=user, mean=" ".join(list(text)))
    await ctx.message.add_reaction("✅")

@bot.command()
async def setFooterIcon(ctx, url = ""):
    user = str(ctx.author.id)
    if url == "" and len(ctx.message.attachments) == 0:
        url = None
    elif len(ctx.message.attachments) != 0:
        url = ctx.message.attachments[0].url
    if not a.user_in(user=user):
        a.make_new(user=user)
    a.set_footer_icon(user=user, mean=url)
    await ctx.message.add_reaction("✅")


@bot.command()
async def clearAll(ctx):
    user = str(ctx.author.id)
    if a.user_in(user=user): 
        a.clear_all(user=user)
        await ctx.message.add_reaction("✅")


bot.run('MTAxNTUzOTM5MjM5MzI1MjkyNA.GL8JGL.045TyGMtkSAPFLSBC5w61u1lyCg67mf44nAp-c')