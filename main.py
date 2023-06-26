import discord
from discord.ext import commands
import openai
import requests

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

openai.api_key = "YOUR_OPENAI_API_KEY"

def get_random_joke():
    url = 'https://api.jokes.one/jod'
    response = requests.get(url)
    try:
        response.raise_for_status()  # Raise an exception if the request was unsuccessful
        data = response.json()
        joke = data['contents']['jokes'][0]['joke']['text']
        return joke
    except (requests.exceptions.HTTPError, KeyError, IndexError, ValueError) as e:
        print(f"Error occurred while retrieving a joke: {e}")
        return "Sorry, I couldn't fetch a joke at the moment."


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

#!ASK Command
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.lower() == '!ask':
        await message.channel.send("Sure! What's your question?")
        response = await bot.wait_for('message', check=lambda m: m.author == message.author)
        question = response.content

        try:
            answer = openai.Completion.create(
                engine='davinci',
                prompt=question,
                max_tokens=100
            )
            await message.channel.send(answer.choices[0].text.strip())
        except Exception as e:
            await message.channel.send("I'm sorry, I couldn't answer your question at the moment.")
    
    await bot.process_commands(message)

#!JOKE Command
@bot.command()
async def joke(ctx):
    joke = get_random_joke()
    await ctx.send(joke)

#!POLL Command
@bot.command()
async def poll(ctx, question, *options):
    if len(options) < 2 or len(options) > 9:
        await ctx.send("Please provide at least 2 and at most 9 options for the poll.")
        return

    formatted_options = [f"{index + 1}. {option}" for index, option in enumerate(options)]
    options_text = "\n".join(formatted_options)

    poll_embed = discord.Embed(title="Poll", description=question, color=discord.Color.blue())
    poll_embed.add_field(name="Options", value=options_text, inline=False)
    poll_message = await ctx.send(embed=poll_embed)

    for i in range(len(options)):
        await poll_message.add_reaction(chr(127462 + i))  # Adds number emojis as reactions

@poll.error
async def poll_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please provide a question and at least 2 options for the poll.")

#!CAT Command
@bot.command()
async def cat(ctx):
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    data = response.json()
    image_url = data[0]['url']
    await ctx.send(image_url)

#!DOG Command
@bot.command()
async def dog(ctx):
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    data = response.json()
    image_url = data['message']
    await ctx.send(image_url)

#!MEME Command
@bot.command()
async def meme(ctx):
    response = requests.get("https://meme-api.herokuapp.com/gimme")
    data = response.json()
    meme_url = data['url']
    meme_title = data['title']
    meme_upvotes = data['ups']

    embed = discord.Embed(title=meme_title, color=discord.Color.orange())
    embed.set_image(url=meme_url)
    embed.set_footer(text=f"👍 {meme_upvotes} upvotes")

    await ctx.send(embed=embed)

#!SAY Command
@bot.command()
async def say(ctx, *, message):
    await ctx.send(message)

#!USERINFO Command
@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author
    
    embed = discord.Embed(title="User Information", color=discord.Color.blue())
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="Name", value=member.name, inline=True)
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(name="Nickname", value=member.display_name, inline=True)
    embed.add_field(name="Created At", value=member.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
    embed.add_field(name="Joined At", value=member.joined_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
    embed.add_field(name="Roles", value=', '.join(role.name for role in member.roles[1:]), inline=False)  # Exclude @everyone role

    await ctx.send(embed=embed)

#!SERVERINFO Command
@bot.command()
async def serverinfo(ctx):
    server = ctx.guild
    
    embed = discord.Embed(title="Server Information", color=discord.Color.green())
    embed.set_thumbnail(url=server.icon_url)
    embed.add_field(name="Name", value=server.name, inline=True)
    embed.add_field(name="ID", value=server.id, inline=True)
    embed.add_field(name="Owner", value=server.owner, inline=True)
    embed.add_field(name="Region", value=server.region, inline=True)
    embed.add_field(name="Members", value=server.member_count, inline=True)
    embed.add_field(name="Created At", value=server.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
    embed.add_field(name="Verification Level", value=server.verification_level, inline=True)
    embed.add_field(name="Roles", value=', '.join(role.name for role in server.roles[1:]), inline=False)  # Exclude @everyone role

    await ctx.send(embed=embed)

# Remove the default help command
bot.remove_command('help')
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Bot Commands", description="List of available commands:", color=discord.Color.blue())

    # Add commands and their descriptions to the embed
    embed.add_field(name="!meme", value="Fetches a random meme.", inline=False)
    embed.add_field(name="!cat", value="Shows a random picture of a cat.", inline=False)
    embed.add_field(name="!dog", value="Shows a random picture of a dog.", inline=False)
    embed.add_field(name="!poll", value="Starts a poll. Usage: `!poll <question>`", inline=False)
    embed.add_field(name="!say", value="Bot repeates what is written.", inline=False)
    embed.add_field(name="!userinfo", value="Displays user info.", inline=False)
    embed.add_field(name="!serverinfo", value="Displays server info.", inline=False)
    embed.add_field(name="!help", value="Shows this help message.", inline=False)


    await ctx.send(embed=embed)


TOKEN = "YOUR-TOKEN"

bot.run(TOKEN)
