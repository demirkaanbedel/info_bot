import discord
from discord.ext import commands
import os
import random
import requests
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=';', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir bilgilendirme botuyum!')

@bot.command()
async def info(ctx):
    await ctx.send(f'Hava Kirliliği hakkında bilgi için a tuşuna bas.Yol açtığı sorunlar için b tuşuna bas. Video için c tuşuna bas.Çözümler için d tuşuna bas.')

@bot.command()
async def a(ctx):
    await ctx.send("Hava kirliliği, canlıların sağlığını olumsuz yönde etkileyen ve havadaki yabancı maddelerin, normalin üzerinde miktar ve yoğunluğa ulaşmasıdır.Hava kirliliği; havada katı, sıvı ve gaz şeklindeki yabancı maddelerin insan sağlığına, canlı hayatına ve ekolojik dengeye zarar verecek miktar, yoğunluk ve uzun sürede atmosferde bulunmasıdır. İnsanların çeşitli faaliyetleri sonucu meydana gelen üretim ve tüketim aktiviteleri sırasında ortaya çıkan atıklarla hava tabakası kirlenerek, yeryüzündeki canlı hayatını olumsuz yönde etkilemektedir.Yazın güneş ışığından dolayı ozon dumanı üretir. Ağaçlar uçucu hidrokarbon yayar.")

@bot.command()
async def b(ctx):
    await ctx.send("Kirli hava, insanlarda solunum yolu hastalıklarının artmasına sebep olmaktadır. Örneğin; kurşunun kan hücrelerinin gelişmesini ve olgunlaşmasını engellediği, kanda ve idrarda birikerek sağlığı olumsuz yönde etkilediği, karbon monoksit (CO)'in ise, kandaki hemoglobin ile birleşerek oksijen taşınmasını aksattığı bilinmektedir. Bununla birlikte kükürt dioksit (SO2)'in, üst solunum yollarında keskin, boğucu ve tahriş edici etkileri vardır. Özellikle duman akciğerden alveollere kadar girerek olumsuz etki yapmaktadır. Cilt hastalıkları, saç dökülmesi, akciğer hastalıkları ve kansere yol açtığı somut bir gerçektir. Ayrıca kükürt dioksit ve ozon bitkiler için zararlı olup; özellikle ozon, ürün kayıplarına sebep olmakta ve ormanlara zarar vermektedir. Kirli hava kilo yapar ve genleri etkiler. Azot dioksit(NO2) çocuklarda astım ve akciğer hastalıklarına yol açabiliyor.")

@bot.command()
async def c(ctx):
    await ctx.send("https://www.youtube.com/watch?v=Wd0FzQTDM90")

@bot.command()
async def d(ctx):
    await ctx.send("Enerji tüketimini azaltın. Hava kirliliğini önlemenin ilk adımı enerji tüketimini azaltmaktır.Araç emisyonlarını azaltın. Sürdürülebilir tarım uygulayın. Atık üretimini azaltın. Hava kirliliğini azaltan destek politikaları.")

bot.run("put token here")
