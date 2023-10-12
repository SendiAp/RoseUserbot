"""
I am responsible for misuse of this script or code, I only correct it so that these modules and plugins function properly for other users.

https://www.github.com/SendiAp/RoseUserbot

https://t.me/RoseUserbotV2 | © Rose Userbot 
"""

import asyncio
import io
import os
import random
import textwrap
import requests
from io import BytesIO
from base64 import b64decode
from pyrogram import Client, errors
from pyrogram.types import Message
from ..modules.basic import ReplyCheck
from ..modules.basic import edit_or_reply
from ..modules.tools import get_arg
from ..modules import *
from ..import *
from ..modules.vars import *

QURAN = """
1. Al-Fatihah (Pembuka, 7 ayat)
2. Al-Baqarah (Sapi Betina, 286 ayat)
3. Ali-Imran (Keluarga Imran, 200 ayat)
4. An-Nisa' (Wanita, 176 ayat)
5. Al-Ma'idah (Jamuan, 120 ayat)
6. Al-An’am (Hewan Ternak, 165 ayat)
7. Al-A'raf (Tempat yang Tertinggi, 206 ayat)
8. Al-Anfal (Harta Rampasan Perang, 75 ayat)
9. At-Taubah (Pengampunan, 129 ayat)
10. Yunus (Nabi Yunus, 109 ayat)
11. Hud (Nabi Hud, 123 ayat)
12. Yusuf (Nabi Yusuf, 111 ayat)
13. Ar-Ra’d (Guruh, 43 ayat)
14. Ibrahim (Nabi Ibrahim, 52 ayat)
15. Al-Hijr (Gunung Al Hijr, 99 ayat)
16. An-Nahl (Lebah, 128 ayat)
17. Al-Isra' (Perjalanan Malam, 111 ayat)
18. Al-Kahfi (Penghuni-penghuni Gua, 110 ayat)
19. Maryam (Maryam, 98 ayat)
20. Ta Ha (Ta Ha, 135 ayat)
21. Al-Anbiya' (Nabi-Nabi, 112 ayat)
22. Al-Hajj (Haji, 78 ayat)
23. Al-Mu'minun (Orang-orang mukmin, 118 ayat)
24. An-Nur (Cahaya, 64 ayat)
25. Al-Furqan (Pembeda, 77 ayat)
26. Asy-Syu'ara' (Penyair, 227 ayat)
27. An-Naml (Semut, 93 ayat)
28. Al-Qasas (Kisah-kisah, 88 ayat)
29. Al-Ankabut (Laba-laba, 69 ayat)
30. Ar-Ruu (Bangsa Romawi, 60 ayat)
31. Luqman (Keluarga Luqman, 34 ayat)
32. As-Sajdah (Sajdah, 30 ayat)
33. Al-Ahzab (Golongan-golongan yang Bersekutu, 73 ayat)
34. Saba' (Kaum Saba', 54 ayat)
35. Fatir (Pencipta, 45 ayat)
36. Ya sin (Yaasiin, 83 ayat
37. Ash-Shaaffat (Barisan-barisan, 182 ayat)
38. Shad (Shaad, 88 ayat)
39. Az-Zumar (Rombongan-rombongan, 75 ayat)
40. Ghafir (Yang Mengampuni, 85 ayat)
41. Fushshilat (Yang Dijelaskan, 54 ayat)
42. Asy-Syura (Musyawarah, 53 ayat)
43. Az-Zukhruf (Perhiasan, 89 ayat)
44. Ad-Dukhan (Kabut, 59 ayat)
45. Al-Jaatsiyah (Yang Bertekuk Lutut, 37 ayat)
46. Al-Ahqaf (Bukit-bukit Pasir, 35 ayat)
47. Muhammad (Nabi Muhammad, 38 ayat)
48. Al-Fath (Kemenangan, 29 ayat)
49. Al-Hujurat (Kamar-kamar, 18 ayat)
50. Qaaf (Qaaf, 45 ayat)
51. Adz-dzariyat (Angin yang Menerbangkan, 60 ayat)
52. Ath-Thuur (Bukit, 49 ayat)
53. An-Najm (Bintang, 62 ayat)
54. Al-Qamar (Bulan, 55 ayat)
55. Ar-Rahman (Yang Maha Pemurah, 78 ayat)
56. Al-Waqi'ah (Hari Kiamat, 96 ayat)
57. Al-Hadid (Besi, 29 ayat)
58. Al-Mujadilah (Wanita yang Mengajukan Gugatan, 22 ayat)
59. Al-Hasyr (Pengusiran, 24 ayat)
60. Al-Mumtahanah (Wanita yang Diuji, 13 ayat)
61. Ash-shaf (Satu Barisan, 14 ayat)
62. Al-Jumu'ah (Hari Jum'at, 11 ayat)
63. Al-Munafiqun (Orang-orang yang Munafik, 11 ayat)
64. At-taghabun (Hari Dinampakkan Kesalahan-kesalahan, 18 ayat)
65. Ath-Thalaq (Talak, 12 ayat)
66. At-Tahrim (Mengharamkan, 12 ayat)
67. Al-Mulk (Kerajaan, 30 ayat)
68. Al-Qalam (Pena, 52 ayat)
69. Al-Haqqah (Hari Kiamat, 52 ayat)
70. Al-Ma'arij (Tempat Naik, 44 ayat)
71. Nuh (Nabi Nuh, 28 ayat)
72. Al-Jin (Jin, 28 ayat)
74. Al-Muddatstsir (Orang yang Berkemul, 56 ayat)
75. Al-Qiyamah (Kiamat, 40 ayat)
76. Al-Insan (Manusia, 31 ayat)
77. Al-Mursalat (Malaikat-Malaikat Yang Diutus, 50 ayat)
78. An-Naba' (Berita Besar, 40 ayat)
79. An-Nazi'at (Malaikat-Malaikat Yang Mencabut, 46 ayat)
80. 'Abasa (Ia Bermuka Masam, 42 ayat)
81. At-Takwir (Menggulung, 29 ayat)
82. Al-Infithar (Terbelah, 19 ayat)
83. Al-Muthaffifin (Orang-orang yang Curang, 36 ayat)
84. Al-Insyiqaq (Terbelah, 25 ayat)
85. Al-Buruj (Gugusan Bintang, 22 ayat)
86. Ath-Thariq (Yang Datang di Malam Hari, 17 ayat)
87. Al-A’laa (Yang Paling Tinggi, 19 ayat)
88. Al-Ghasyiyah (Hari Pembalasan, 26 ayat)
89. Al-Fajr (Fajar, 30 ayat)
90. Al-Balad (Negeri, 20 ayat)
91. Asy-Syams (Matahari, 15 ayat)
92. Al-Lail (Malam, 21 ayat)
93. Adh-Dhuha (aktu Matahari Sepenggalahan Naik (Dhuha), 11 ayat)
94. Al-Insyirah (Melapangkan, 8 ayat)
95. At-Tin (Buah Tin, 8 ayat)
96. Al-'Alaq (Segumpal Darah, 19 ayat)
97. Al-Qadr (Kemuliaan, 5 ayat)
98. Al-Bayyinah (Pembuktian, 8 ayat)
99. Al-Zalzalah (Kegoncangan, 8 ayat)
100. Al-'Adiyat (Berlari Kencang, 11 ayat)
101. Al-Qari'ah (Hari Kiamat, 11 ayat)
102. At-Takatsur (Bermegah-megahan, 8 ayat)
103. Al-'Ashr (Masa, 3 ayat)
104. Al-Humazah (Pengumpat, 9 ayat)
105. Al-Fil (Gajah, 5 ayat)
"""

QURANN = """
106. Quraysh (Suku Quraisy, 4 ayat)
107. Al-Ma'un (Barang-barang yang Berguna, 7 ayat)
108. Al-Kautsar (Nikmat yang Berlimpah, 3 ayat)
109. Al-Kafirun (Orang-orang Kafir, 6 ayat)
110. An-Nashr (Pertolongan, 3 ayat)
111. Al-Lahab (Gejolak Api, 5 ayat)
112. Al-Ikhlas (Ikhlas, 4 ayat)
113. Al-Falaq (Waktu Subuh, 5 ayat)
114. An-Nas (Umat Manusia, 6 ayat)
"""


@app.on_message(commandx(["quran"]) & SUDOERS)
async def quran_audio(client: Client, message: Message):
    prik = await message.edit("`Processing . . .`")
    link = get_arg(message)
    if not link:
       return await message.edit("**Format Salah, Silahkan Lihat .listsurah untuk melihat daftar nomor surah**")
    bot = "AlQuran_audio_bot"
    if link:
        try:
            Rose = await client.send_message(bot, link)
            await asyncio.sleep(5)
            await Rose.delete()
        except YouBlockedUser:
            await client.unblock_user(bot)
            tuyul = await client.send_message(bot, link)
            await asyncio.sleep(10)
            await Rose.delete()
    async for quran in client.search_messages(
        bot, filter=enums.MessagesFilter.AUDIO, limit=1
    ):
        await asyncio.gather(
            prik.delete(),
            client.send_audio(
                message.chat.id,
                quran.audio.file_id,
                caption=f"**Upload by:** {client.me.mention}",
                reply_to_message_id=ReplyCheck(message),
            ),
        )
        await client.delete_messages(bot, 2)
    

@app.on_message(commandx(["rquran"]) & SUDOERS)
async def quran_audio(client: Client, message: Message):
    prik = await message.edit("`Processing . . .`")
    link = "random"
    if not link:
       return await message.edit("**Format Salah, Silahkan Lihat .listsurah untuk melihat daftar nomor surah**")
    bot = "IslamicQuranBot"
    if link:
        try:
            Rose = await client.send_message(bot, link)
            await asyncio.sleep(5)
            await Rose.delete()
        except YouBlockedUser:
            await client.unblock_user(bot)
            tuyul = await client.send_message(bot, link)
            await asyncio.sleep(10)
            await Rose.delete()
    async for quran in client.search_messages(
        bot, filter=enums.MessagesFilter.AUDIO, limit=1
    ):
        await asyncio.gather(
            prik.delete(),
            client.send_audio(
                message.chat.id,
                quran.audio.file_id,
                caption=f"**Upload by:** {client.me.mention}",
                reply_to_message_id=ReplyCheck(message),
            ),
        )
        await client.delete_messages(bot, 2)


@app.on_message(commandx(["listsurah"]) & SUDOERS)
async def surah_list(client, message):
    botlog = var.LOG_GROUP_ID
    list_quran = QURAN
    quran_list = QURANN
    await message.edit("`Sedang mengirimkan...`")
    await asyncio.sleep(5)
    xx = await client.send_message(list_quran, botlog)
    await xx.reply(quran_list, botlog)
    await message.edit("`Berhasil Dikirim Di Botlog Chat ID`")

__NAME__ = "alquran"
__MENU__ = f"""
✘ **Perintah:** `.quran` [1]
• **Fungsi:** untuk mendapatkan audio surah Al-Qur'an
[1] Alfatihah surah ke satu

✘ **Perintah:** `.rquran**
• **Fungsi:** Untuk mendapatkan audio surah random.

✘ **Perintah:** `.listsurah`
• **Fungsi:** Untuk mendapatkan list surah nomer.

🆘 **WARNING:** Gunakan ditempat yang baik, dan jangan digunakan 
untuk main main.

© Rose Userbot
"""
