import os
import re
from dotenv import load_dotenv

# Nạp file môi trường .env
load_dotenv()

# TOKEN & OWNERS
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", "")

def get_owner_ids() -> set[int]:
    raw_owners = os.getenv("OWNER_IDS", "")
    owners = set()
    for item in raw_owners.split(","):
        item = item.strip()
        if item.isdigit():
            owners.add(int(item))
    return owners

# Lưu và cập nhật file .env
def save_owner_ids(owner_set: set[int]):
    owners_str = ",".join(str(oid) for oid in owner_set)
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        updated = False
        new_lines = []
        for line in lines:
            if line.startswith("OWNER_IDS="):
                new_lines.append(f"OWNER_IDS={owners_str}\n")
                updated = True
            else:
                new_lines.append(line)
        if not updated:
            new_lines.append(f"OWNER_IDS={owners_str}\n")
        
        with open(env_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)

# Bảng màu Embeds (Màu sắc sang trọng, hiện đại)
class Colors:
    PRIMARY = 0x6C5CE7     # Tím Pastel sang trọng
    SUCCESS = 0x00B894     # Xanh ngọc lục bảo
    DANGER = 0xD63031      # Đỏ đậm bão hòa
    WARNING = 0xFDCB6E     # Vàng hoàng gia
    INFO = 0x0984E3        # Xanh dương sapphire
    OWNER = 0xFD79A8       # Hồng Neon phong cách Owner
    VOICE = 0x00CEC9       # Xanh ngọc Voice Channel

# Emojis trang trí
class Emojis:
    CROWN = "👑"
    SHIELD = "🛡️"
    BAN = "🔨"
    MUTE = "🔇"
    MIC_OFF = "🎙️❌"
    ROLE = "✨"
    NICKNAME = "🏷️"
    VOICE = "🔊"
    MUSIC = "🎶"
    HELP = "📜"
    SUCCESS = "✅"
    ERROR = "❌"
    INFO = "ℹ️"
    TIME = "⏰"
    STAR = "⭐"
    SPARKLES = "💖"

# Bộ chuyển đổi phông chữ Unicode đẹp (Aesthetic Text Generator)
FONT_MAP = {
    'A': '𝒜', 'B': 'ℬ', 'C': '𝒞', 'D': '𝒟', 'E': 'ℰ', 'F': 'ℱ', 'G': '𝒢',
    'H': 'ℋ', 'I': 'ℐ', 'J': '𝒥', 'K': '𝒦', 'L': 'ℒ', 'M': 'ℳ', 'N': '𝒩',
    'O': '𝒪', 'P': '𝒫', 'Q': '𝒬', 'R': 'ℛ', 'S': '𝒮', 'T': '𝒯', 'U': '𝒰',
    'V': '𝒱', 'W': '𝒲', 'X': '𝒳', 'Y': '𝒴', 'Z': '𝒵',
    'a': '𝒶', 'b': '𝒷', 'c': '𝒸', 'd': '𝒹', 'e': '𝑒', 'f': '𝒻', 'g': '𝑔',
    'h': '𝒽', 'i': '𝒾', 'j': '𝒿', 'k': '𝓀', 'l': '𝓁', 'm': '𝓂', 'n': '𝓃',
    'o': '𝑜', 'p': '𝓅', 'q': '𝓆', 'r': '𝓇', 's': '𝓈', 't': '𝓉', 'u': '𝓊',
    'v': '𝓋', 'w': '𝓌', 'x': '𝓍', 'y': '𝓎', 'z': '𝓏'
}

def fancify_text(text: str) -> str:
    """Chuyển đổi văn bản thành chữ hoa mỹ (Calligraphy/Script Unicode)"""
    return "".join(FONT_MAP.get(char, char) for char in text)

def bold_fancy(text: str) -> str:
    """Tạo chữ in đậm kết hợp phông trang trí"""
    return f"**{fancify_text(text)}**"
