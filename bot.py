import discord
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
    
    
    
    #Remove unnecessary roles
    await ctx.send('Removing unnecessary roles:')

    for role in guild.roles:
        if role.name!='BuilderBot' and role.id!=guild.default_role.id:
            await role.delete()
            await ctx.send("Deleted Role: {}".format(role.name))

    #Create Roles
    await ctx.send('Creating Roles')
    #Owner
    owner = await guild.create_role(name="Owner",colour=discord.Colour.dark_gold())
    
    #Admin
    admin = await guild.create_role(name="Admin",colour=discord.Colour.red())
    #Moderator
    moderator = await guild.create_role(name="Moderator",colour=discord.Colour.dark_green())
    #Member
    member = await guild.create_role(name="Member",colour=discord.Colour.blue())
    
    
    #Setup Permissions for Roles
    defaultPerms = discord.Permissions.none()

    memberPerms=defaultPerms
    memberPerms.update(view_channel = True)
    memberPerms.update(create_instant_invite = True)
    memberPerms.update(send_messages = True)
    memberPerms.update(add_reactions = True)
    memberPerms.update(use_external_emojis = True)
    memberPerms.update(external_stickers = True)
    memberPerms.update(external_stickers = True)
    memberPerms.update(read_message_history = True)
    memberPerms.update(connect = True)
    memberPerms.update(speak = True)

    moderatorPerms=memberPerms
    moderatorPerms.update(manage_emojis = True)
    moderatorPerms.update(view_audit_log =True)
    moderatorPerms.update(view_guild_insights =True)
    moderatorPerms.update(change_nickname = True)
    moderatorPerms.update(manage_nicknames = True)
    moderatorPerms.update(embed_links = True)
    moderatorPerms.update(attach_files = True)
    moderatorPerms.update(mention_everyone = True)
    moderatorPerms.update(manage_messages = True)
    moderatorPerms.update(use_slash_commands = True)
    moderatorPerms.update(stream = True)
    moderatorPerms.update(mute_members = True)
    moderatorPerms.update(deafen_members = True)
    moderatorPerms.update(move_members = True)

    adminPerms=moderatorPerms
    adminPerms.update(manage_channels = True)
    adminPerms.update(manage_roles = True)
    adminPerms.update(manage_webhooks = True)
    adminPerms.update(ban_members = True)
    adminPerms.update(kick_members = True)
        
    ownerPerms=adminPerms
    ownerPerms.update(manage_guild = True)

    #Edit Roles
    await ctx.send('Editing Role Permissions')
    await owner.edit(permissions=ownerPerms)
    await admin.edit(permissions=adminPerms)
    await moderator.edit(permissions=moderatorPerms)
    await member.edit(permissions=memberPerms)
    await guild.default_role.edit(permissions=defaultPerms)


    #Remove unneccessary channels
    await ctx.send('Removing unneccessary channels:')
    for channel in guild.text_channels:
        if channel.name!='welcome':
            await channel.delete()

    #Remove unneccessary categories
    await ctx.send('Removing unneccessary categories:')
    for category in guild.categories:
        await category.delete()

    #Creating Categories and Channels
    await ctx.send('Creating Categories and Channels')
    
    #Server Stats
    category = await guild.create_category('______SERVER STATS______')
    await guild.create_text_channel('|available', category=category)
    await guild.create_text_channel('|members', category=category)

    #Mod Channels

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