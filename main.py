import discord
import os
import random
import requests
from discord.ext import commands
from settings import settings

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_fox_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']

listeco = ["Посадить дерево.","Построить скворечник, синичник.","Повесить и своевременно наполнять кормушку, поилку для птиц.","Ездить волонтером на проекты по спасению, восстановлению, учету животных.","Поддерживать фонды помощи животным.","Реже пользоваться кондиционером.","Убавлять индивидуальное отопление.","Покупать энергосберегающие приборы.","Сажать деревья.","Выбрать электротранспорт.","Больше ездить на велосипеде и ходить пешком."," Сортировать мусор.","Раздавать и продавать ненужные вещи, уменьшая количество мусора.","Устраивать и посещать фримаркеты для обмена вещами.","Пустую пластиковую упаковку, остатки ткани и прочее пускать на поделки.","В походе ходить только по тропам.","Не повреждать и не рвать без нужды растения, не ломать ветки.","Не шуметь, не включать громкую музыку.","Не кормить диких животных.","Не трогать птиц, насекомых.","Не оставлять надписи на камнях и прочих природных объектах.","Для разведения костра использовать старые кострища.","Ненужный костер затушить и засыпать землей.","Не разводить костры там, где это запрещено.","Не использовать на природе бытовую химию.","Закапывать органические отходы. ","После отдыха на природе забирать с собой мусор.","Собирать мусор в любимых уголках отдыха - в одиночку или с коллективом единомышленников.","Отправиться волонтером на уборку мусора в популярных туристических местах.","Прививать детям и окружающим любовь к природе - как сделать это интересно и ненавязчиво, расскажем далее."]

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')


@bot.command()
async def eco(ctx):
    img_name = random.choice(os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def ecosovet(ctx):
    await ctx.send("Кратко о том, что можно сделать для экологии прямо сейчас: \n \n" + random.choice(listeco))

@bot.command()
async def help(ctx):
    await ctx.send("Список доступных команд: \n help - Все команды \n eco - Мем/фотография об экологии \n ecosovet - Советы как не вредить экологии")


bot.run(settings["TOKEN"])