import discord
from discord.ext import commands
import os
import sys
import io
import asyncio
import config

# Đảm bảo Encoding UTF-8 trên Windows Console
if hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def create_bot_intents(enable_privileged: bool = True):
    intents = discord.Intents.default()
    intents.voice_states = True
    if enable_privileged:
        intents.members = True
        intents.message_content = True
    return intents

class DiscordBot(commands.Bot):
    def __init__(self, intents: discord.Intents):
        super().__init__(
            command_prefix=["pu!", "PU!", "pu! "],
            intents=intents,
            help_command=None
        )

    async def setup_hook(self):
        """Tự động nạp tất cả các Cogs khi bot khởi động"""
        print(">> Đang nạp các cogs...")
        cog_files = ["cogs.owner", "cogs.moderation", "cogs.help", "cogs.voice_music", "cogs.love", "cogs.ai_gif"]
        for cog in cog_files:
            try:
                await self.load_extension(cog)
                print(f"  [+] Nạp thành công cog: {cog}")
            except Exception as e:
                print(f"  [-] Lỗi khi nạp cog {cog}: {e}")

        # Đồng bộ Slash Commands toàn cầu
        print(">> Đang đồng bộ Slash Commands ('/') toàn cầu...")
        try:
            synced = await self.tree.sync()
            print(f"  [+] Đã đồng bộ {len(synced)} lệnh Slash toàn cầu!")
        except Exception as e:
            print(f"  [-] Lỗi khi đồng bộ Slash Commands: {e}")

    async def on_ready(self):
        banner = f"""
===========================================================
  [BOT DISCORD ĐÃ SẴN SÀNG HOẠT ĐỘNG ONLINE!]
===========================================================
  • Tên Bot     : {self.user.name} ({self.user.id})
  • Prefix Lệnh : pu!play (Gửi file MP3 để phát Loa to + Bass Boost)
  • Lệnh Slash  : Đã đồng bộ tức thì vào các Server Discord
  • Quyền Owner : Đã nạp từ .env
===========================================================
"""
        print(banner)

        # Xóa bỏ trùng lặp lệnh bằng cách dọn sạch lệnh Guild cũ và chỉ dùng Lệnh Toàn Cầu (Global Commands)
        for guild in self.guilds:
            try:
                self.tree.clear_commands(guild=guild)
                await self.tree.sync(guild=guild)
                print(f"  [+] Đã dọn sạch trùng lặp lệnh cho Server: '{guild.name}' ({guild.id})")
            except Exception as e:
                print(f"  [-] Lỗi dọn trùng lặp lệnh cho server '{guild.name}': {e}")

        # Cài đặt trạng thái hiển thị của bot
        activity = discord.Activity(
            type=discord.ActivityType.listening,
            name="pu!play | /help | Bass Boost 🔊"
        )
        await self.change_presence(status=discord.Status.online, activity=activity)

async def main():
    token = config.DISCORD_TOKEN
    if not token or token == "THAY_TOKEN_CUA_BAN_VAO_DAY":
        print("\n[!] LỖI BẢO MẬT: Chưa cấu hình Token Bot trong file .env!")
        print("-> Vui lòng mở file C:\\Users\\trant\\Desktop\\DiscordBot\\.env và dán DISCORD_TOKEN của bạn vào.\n")
        return

    try:
        # Thử khởi chạy với Privileged Intents
        bot = DiscordBot(intents=create_bot_intents(enable_privileged=True))
        async with bot:
            await bot.start(token)
    except discord.errors.PrivilegedIntentsRequired:
        print("\n[!] CẢNH BÁO: Privileged Intents chưa được bật trên Discord Developer Portal.")
        print("-> Đang tự động chuyển sang Chế Độ Tiêu Chuẩn (Default Intents)...")
        bot = DiscordBot(intents=create_bot_intents(enable_privileged=False))
        async with bot:
            await bot.start(token)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[!] Bot đã tắt thành công!")
    except Exception as e:
        print(f"\n[!] Lỗi vận hành: {e}")
