from discord.ext import commands
import info

API_TOKEN=info.TOKEN
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as {}'.format(bot.user.name))
    
@bot.command()
async def setup(ctx):
    
    guild = bot.guilds[0]
    await ctx.send('Setup start:')
    
    await ctx.send('Removing unneccessary channels:')
    for channel in guild.text_channels:
        if channel.name!='welcome':
            await channel.delete()

    await ctx.send('Removing unneccessary categories:')
    for category in guild.categories:
        await category.delete()

    #Server Stats
    category = await guild.create_category('______SERVER STATS______')
    await guild.create_text_channel('|available', category=category)
    await guild.create_text_channel('|members', category=category)

    #Important
    category = await guild.create_category('_______IMPORTANT________')
    await guild.create_text_channel('📍-roadmap', category=category)
    await guild.create_text_channel('🔗-official-links', category=category)
    await guild.create_text_channel('🎭-roles-info', category=category)
    await guild.create_text_channel('✅-verifiy-here', category=category)
    #Main
    category = await guild.create_category('__________MAIN__________')
    await guild.create_text_channel('📢-announcements', category=category)
    await guild.create_text_channel('🧠-sneak-peak', category=category)
    await guild.create_text_channel('💬-general', category=category)
    await guild.create_text_channel('⛔-online-safety', category=category)
    #Social
    category = await guild.create_category('_________SOCIAL_________')
    await guild.create_text_channel('🍙-anime', category=category)
    await guild.create_text_channel('🎵-music', category=category)
    await guild.create_text_channel('🎨-creative', category=category)
    #Collabs
    category = await guild.create_category('_________COLLABS________')
    await guild.create_text_channel('💳-shilling', category=category)
    #Support
    category = await guild.create_category('________SUPPORT_________')
    await guild.create_text_channel('🌿-mint-support', category=category)
    await guild.create_text_channel('💀-report-a-scam', category=category)
    await guild.create_text_channel('💡-suggestions', category=category)
    
bot.run(API_TOKEN)