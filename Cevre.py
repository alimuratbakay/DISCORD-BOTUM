import discord


# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirecek
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaracak
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptik.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('$Atiklarimi Nasil Ayristiririm'):
        await message.channel.send("Öncelikle Evde başlica dort cop kovasi olustur birinde cam birinde metal birinde plastik birinde de plastik yazin"
            "ardindan Bu Cop Kovalarina Atiklari duzgun bir sekilde ayristir ve bir cop kutusu dolunca yakinlardaki bir geri donusum kutusuna "
            "gotur ve atiklarini disaridaki kutuya bosalt")
    elif message.content.startswith('$Beni Bilinçlendir'):
        await message.channel.send("Oncelikle Su Kirliliginden Baslamak Istiyorum Su kirliliğine genel olarak Denizlere attigimiz copler ve zehirli atiklar"
             "in denizi kirletmesidir sonuclari denizdeki eko sistemin bozulmasi temiz su kaynaklarinin kirlenmesi verilebilir"
             "onlem olarak fabrikalar da denettimler arttirilmali ve sahillere cop kovalari konmali eger var ama az sayida ise sayilari arttirilmali "
             "2.Toprak Kirliliği: Yerlere attigimiz plastik metal cam vb maddelerin bagzilari içlerinde zehirli atiklar bulunur biz bu atiklari yere atinca "
             "Bu zehirli maddeler topraga karisir ve uzun sure orada kalir bu hem tarimi hem hayvanciligi hem de insan sagligini olumsuz etkiler"
             "cozum olarak insanlari bilinclendirmek geri donusum kutularinin sayisini arttirmak gibi seyler verilebilir"
             "3.Hava Kirliligi: Bu kirlilik türü havaya salinan CO2(Karbondiyoksit) SO3(kükürtdioksit) ve NO2(azotdioksit) gazlarininhavaya salinmasi ile olusan"
             "kirlilik turudur bu kirlilik turu havadaki zehirli gazlar nedeni ile insan sagligini olumsuz etkiler ve sera etkisini arttirarak kuresel isinmayi arttirir"
             "bagzenleri ise bu gazlar havadaki su molekülleri ile tepkimeye girerek  sülfüroz asit, sülfürik asit ve nitrik asit gibi asitleri oluştururlar"
             "bu gazlar yer yuzune inerek topraklari verimsizlestirir insanlara MADDI HASAR verir ve bitkileri tahrip ederler"
             "bunu onlemek icin ise fabrikalara filtre takmali ve deodorant kullamini azaltmaliyiz bununla beraber insanlari daha cok bilinclendirmeliyiz ayni bu botun yaptigi gibi")
  
    elif message.content.startswith('$Plastik Atiklari Nasil Degerlendiririm'):
        await message.channel.send("Bu durum Sizin Hayal Gücünüze Kalmistir ama yine de bir örnek vermek gerekir ise pet şişe den saksi yapmak verilebilir")




client.run("MTE4OTk5NTYxNDIwNTkyMzQ2MQ.GqLlpq.9oDTgXt4-cVMxSBXV10wt4Ton_-5eaD7317JFo")
