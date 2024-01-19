import discord

# Bu kod parçacığı bir metin dosyasının tamamını okumamızı sağlar
f = open('metin.txt', 'r', encoding='utf-8')
text = f.read()
print(text)
f.close()

# Ve işte bir metin dosyasının tamamını nasıl yeniden yazabileceğimiz:
f = open('metinbelgesi.txt', 'w', encoding='utf-8')
text = 'Yeni Yazi'
f.write(text)
f.close()

# Daha kısa bir versiyonu:
with open('metin.txt', 'r', encoding='utf-8') as f:
    print(f.read())

with open(f'images/{My Mwmw3.jpg}', 'rb') as f:
            picture = discord.File(f)
