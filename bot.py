#discordのライブラリをインポート
import discord
#自分のトークンにしてね
TOKEN = 'YB8Xpomxfh6zIOURWmX6wtBnfbnfKgLC'

# 接続に必要なオブジェクトを作る
client = discord.Client()

#BOTが起動したとき
@client.event
async def on_ready():
    print('起動しました！(\'◇\')ゞ')

#メッセージを受け取ったとき
@client.event
async def on_message(message):
    # Botだったらは無視
    if message.author.bot:
        return
    if message.content == '/hello':
        await message.channel.send('hello')

#BOTの起動
client.run(TOKEN)
