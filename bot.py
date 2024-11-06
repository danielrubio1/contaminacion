import discord
from discord.ext import commands
import random


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


datos_contaminacion = [
    "La contaminación del aire es responsable de millones de muertes prematuras cada año.",
    "Cada año se vierten 8 millones de toneladas de plástico en los océanos.",
    "La deforestación contribuye al aumento de dióxido de carbono en la atmósfera.",
    "Los vehículos emiten gases como CO2 que contribuyen al calentamiento global.",
    "Reciclar ayuda a reducir la cantidad de residuos que van a parar a los vertederos."
]


@bot.event
async def on_ready():
    print(f'{bot.user} está listo y conectado en Discord!')


@bot.command()
async def info(ctx):
    """Envía información general sobre la contaminación."""
    await ctx.send("La contaminación es el proceso por el cual el ambiente se llena de sustancias perjudiciales, afectando la salud de los seres vivos y el equilibrio natural.")


@bot.command()
async def dato(ctx):
    """Envía un dato aleatorio sobre la contaminación."""
    dato = random.choice(datos_contaminacion)
    await ctx.send(dato)


@bot.command()
async def consejo(ctx):
    """Envía un consejo para reducir la contaminación."""
    consejos = [
        "Usa menos plástico y opta por materiales reutilizables.",
        "Camina, usa la bicicleta o transporte público en lugar de vehículos privados.",
        "Ahorra energía apagando luces y dispositivos eléctricos que no utilices.",
        "Recicla y separa correctamente tus residuos.",
        "Apoya iniciativas de reforestación y cuida el medio ambiente."
    ]
    consejo = random.choice(consejos)
    await ctx.send(consejo)


@bot.command()
async def pregunta(ctx, *, pregunta):
    """Responde preguntas básicas sobre contaminación."""
    if "aire" in pregunta.lower():
        await ctx.send("La contaminación del aire proviene de la quema de combustibles fósiles y afecta la salud respiratoria.")
    elif "agua" in pregunta.lower():
        await ctx.send("La contaminación del agua es causada por vertidos industriales, plásticos y desechos agrícolas.")
    else:
        await ctx.send("Lo siento, aún no tengo información sobre eso. ¡Puedes preguntar sobre aire o agua!")
        

bot.run("pon tu token aqui")
