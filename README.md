# 🤖 DISCORD BOT PYTHON (SLASH COMMANDS & VOICE AFK 3 TỶ NGÀY)

Dự án Bot Discord bằng Python (`discord.py`) hỗ trợ **Slash Commands (`/`)**, giao diện Embeds & phông chữ trang trí Unicode đẹp mắt, phân quyền Owner đặc quyền, bộ lệnh quản trị server đầy đủ, kiểm tra tính năng server & role, treo phòng voice không giới hạn thời gian (lên tới 3,000,000,000 ngày), xem/tải Avatar HD và phát nhạc từ MỌI ĐƯỜNG LINK (YouTube, SoundCloud, MP3 link, ...).

Thư mục lưu trữ dự án: `C:\Users\trant\Desktop\DiscordBot`

---

## 🚀 HƯỚNG DẪN CÀI ĐẶT & KHỞI CHẠY (DÀNH CHO NGƯỜI MỚI)

### BƯỚC 1: Lấy Token Bot & Cấp Quyền Trên Discord Developer Portal
1. Truy cập [Discord Developer Portal](https://discord.com/developers/applications) và đăng nhập tài khoản Discord của bạn.
2. Nhấn **New Application** -> Đặt tên cho Bot của bạn -> Nhấn **Create**.
3. Vào mục **Bot** ở menu bên trái:
   - Nhấn **Reset Token** hoặc **Copy** để lấy `DISCORD_TOKEN`.
   - Kéo xuống mục **Privileged Gateway Intents**, bật cả 3 công tắc:
     - ✅ **PRESENCE INTENT**
     - ✅ **SERVER MEMBERS INTENT**
     - ✅ **MESSAGE CONTENT INTENT**
   - Nhấn **Save Changes**.
4. Vào mục **OAuth2** -> **URL Generator**:
   - Chọn scope: `bot` và `applications.commands`.
   - Chọn permissions: `Administrator` (Quản trị viên) hoặc chọn các quyền Ban, Mute, Manage Roles, Connect, Speak.
   - Copy đường link được tạo ra và dán vào trình duyệt để **mời Bot vào Server của bạn**.

---

### BƯỚC 2: Cấu Hình File `.env`
1. Mở thư mục `C:\Users\trant\Desktop\DiscordBot` trên màn hình máy tính của bạn.
2. Mở file `.env` bằng Notepad hoặc VS Code.
3. Cập nhật thông tin:
   ```env
   DISCORD_TOKEN=Dán_Token_Bot_Của_Bạn_Vào_Đây
   OWNER_IDS=ID_Discord_Của_Bạn
   ```
   *(Cách lấy ID Discord của bạn: Bật Developer Mode trong Cài đặt Discord -> Nhấp chuột phải vào tên của bạn -> Chọn "Copy User ID")*

---

### BƯỚC 3: Cài Đặt Thư Viện Python
Mở Terminal / PowerShell tại thư mục dự án `C:\Users\trant\Desktop\DiscordBot` và chạy lệnh:

```bash
pip install -r requirements.txt
```

---

### BƯỚC 4: Bật Bot
Chạy lệnh sau để khởi chạy bot:

```bash
python main.py
```

Khi Terminal hiển thị dòng: `🤖 BOT DISCORD ĐÃ SẴN SÀNG HOẠT ĐỘNG!`, bot của bạn đã sẵn sàng sử dụng trên Discord!

---

## 📜 DANH SÁCH LỆNH SLASH COMMANDS (`/`)

### 1. Menu Hướng Dẫn, Kiểm Tra Server & Role
- `/help`: Hiển thị bảng hướng dẫn menu chi tiết dành cho người mới dùng.
- `/serverinfo`: 📊 Kiểm tra chi tiết thông số, tính năng nâng cao và số lượng thành viên/kênh của Server.
- `/roleinfo <role>`: ✨ Kiểm tra thông số, vị trí, danh sách quyền và màu sắc HEX của một Role cụ thể.
- `/checkroles [user]`: 🔍 Kiểm tra toàn bộ danh sách Role và quyền cao nhất của thành viên.
- `/avatar [user]`: Xem ảnh đại diện HD của bạn hoặc thành viên khác kèm **Nút Link Tải Ảnh Trực Tiếp**.
- `/sendmsg <user> <message>`: Gửi tin nhắn thông báo đến thành viên.

### 2. Treo Voice & Phát Nhạc URL / File
- `/playurl <url>`: 🎶 **Phát nhạc từ MỌI ĐƯỜNG LINK URL** (YouTube, SoundCloud, Direct MP3,...).
- `/playfile <file_name>`: Phát file nhạc `.mp3` / `.wav` lưu trong thư mục `music/`.
- `/treoroom [channel] [duration_days]`: Cho bot vào treo trong phòng voice. Mặc định treo **3,000,000,000 ngày (3 tỷ ngày - 24/7 vô hạn)**.
- `/listmusic`: Xem danh sách file nhạc sẵn có.
- `/stopvoice`: Cho bot dừng nhạc và rời phòng voice.

### 3. Quản Lý Server & Thành Viên (Moderation)
- `/ban <user> [reason]`: Ban thành viên khỏi server.
- `/mute <user> <minutes> [reason]`: Timeout / Mute nhắn tin & voice theo phút.
- `/unmute <user>`: Gỡ mute cho thành viên.
- `/mutemic <user> <mute_state>`: Tắt / Mở micro thành viên trong phòng voice (Server Mute Mic).
- `/createrole <name> [color_hex]`: Tạo role mới với màu sắc tùy chỉnh (ví dụ màu HEX `#FF0000`).
- `/nickname <user> [nickname]`: Đổi biệt danh của thành viên.
- **Biệt danh tự động (Auto Nickname)**: Tự động đổi tên thành viên mới tham gia server theo cấu hình.

### 4. Quản Trị Owner (`add owner ms dùng dc`)
- `/owner add <user>`: Thêm một Owner mới sử dụng bot.
- `/owner remove <user>`: Gỡ quyền Owner của người dùng.
- `/owner list`: Xem danh sách tất cả Owner hiện tại.
