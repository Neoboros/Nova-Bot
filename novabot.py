from setup import *

client = commands.Bot(command_prefix="+", intents=discord.Intents.all())
@client.event
async def on_ready():
    print('Logged on as {0}!')

@client.command()
async def ping(ctx):
    latency = round(client.latency * 1000)
    await ctx.send(f"Pong! {latency} ms.")

@client.command()
async def about(ctx):
    embed_message = discord.Embed(title='Sobre: ', description='Aqui vai um descritivo sobre o projeto: ', color=discord.Color.blue())
    embed_message.add_field(name="O que é?", value="Nós somos uma startup criada por 3 pessoas que visa auxiliar pessoas que não possuem o conhecimento essencial para a construção de um computador que supra as necessidades primárias delas, home officing ou destinado a jogos, constamos com a funcionalidade de selecionar peças e analisar a compatibilidade entre elas, além do gasto de energia e preço total do PC.", inline=True)
    embed_message.set_author(name=f"Pedido por {ctx.author.mention}", icon_url=ctx.author.avatar)
    embed_message.set_image(url=ctx.guild.icon)
    embed_message.set_thumbnail(url=ctx.guild.icon)
    embed_message.set_footer(text="NovaTech © 2023 • Todos os direitos reservados.", icon_url=ctx.author.avatar)
    await ctx.send(embed = embed_message)

client.run(TOKEN)