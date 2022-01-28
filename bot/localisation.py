#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AbirHasan2005

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "<b>Hᴇʟʟᴏ 👋,\n\nTʜɪs Is A Tᴇʟᴇɢʀᴀᴍ Vɪᴅᴇᴏ Cᴏᴍᴘʀᴇss Bᴏᴛ.\n\nSᴇɴᴅ Mᴇ Aɴʏ Tᴇʟᴇɢʀᴀᴍ Bɪɢ Vɪᴅᴇᴏ Fɪʟᴇ I Wɪʟʟ Cᴏᴍᴘʀᴇss Iᴛ Tᴏ A Sᴍᴀʟʟ Vɪᴅᴇᴏ Fɪʟᴇ!\n\n/help Fᴏʀ Mᴏʀᴇ Dᴇᴛᴀɪʟs...\n\nPᴏᴡᴇʀᴇᴅ ʙʏ : @AIOM_BOTS</b>"

    ABS_TEXT = " Please don't be selfish."
    
    FORMAT_SELECTION = "Sᴇʟᴇᴄᴛ Tʜᴇ Dᴇsɪʀᴇᴅ Fᴏʀᴍᴀᴛ :\n\n<a href='{}'>ꜰɪʟᴇ sɪᴢᴇ ᴍɪɢʜᴛ ʙᴇ ᴀᴘᴘʀᴏxɪᴍᴀᴛᴇ</a>\n\nɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴇᴛ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ, sᴇɴᴅ ᴘʜᴏᴛᴏ ʙᴇꜰᴏʀᴇ ᴏʀ ǫᴜɪᴄᴋʟʏ ᴀꜰᴛᴇʀ ᴛᴀᴘᴘɪɴɢ ᴏɴ ᴀɴʏ ᴏꜰ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs.\n\nʏᴏᴜ ᴄᴀɴ ᴜsᴇ /deletethumbnail ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴀᴜᴛᴏ-ɢᴇɴᴇʀᴀᴛᴇᴅ ᴛʜᴜᴍʙɴᴀɪʟ."
    
    DOWNLOAD_START = "Dᴏᴡɴʟᴏᴀᴅɪɴɢ....."
    
    UPLOAD_START = "Uᴘʟᴏᴀᴅɪɴɢ....."
    
    COMPRESS_START = "Cᴏᴍᴘʀᴇssɪɴɢ....."
    
    RCHD_BOT_API_LIMIT = "Uᴘʟᴏᴀᴅɪɴɢ..... "
    
    RCHD_TG_API_LIMIT = "Dᴏᴡɴʟᴏᴀᴅᴇᴅ Iɴ {} Sᴇᴄᴏɴᴅs.\n\nDᴇᴛᴇᴄᴛᴇᴅ Fɪʟᴇ Sɪᴢᴇ: {}\n\nSᴏʀʀʏ. Bᴜᴛ, I Cᴀɴɴᴏᴛ Uᴘʟᴏᴀᴅ Fɪʟᴇs Gʀᴇᴀᴛᴇʀ Tʜᴀɴ 1.99ɢʙ Dᴜᴇ Tᴏ Tᴇʟᴇɢʀᴀᴍ Aᴘɪ Lɪᴍɪᴛᴀᴛɪᴏɴs."

    COMPRESS_SUCCESS = "Dᴏᴡɴʟᴏᴀᴅᴇᴅ Iɴ {}\n\nCᴏᴍᴘʀᴇssᴇᴅ Iɴ {}\n\nUᴘʟᴏᴀᴅᴇᴅ Iɴ {}\n\nA Boᴛ Bʏ : @AIOM_BOTS"

    COMPRESS_PROGRESS = "ETA: {}\nPʀᴏɢʀᴇss : {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Tʜᴜᴍʙɴᴀɪʟ Sᴀᴠᴇᴅ Sᴜᴄᴄᴇssꜰᴜʟʟʏ"
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "Tʜᴜᴍʙɴᴀɪʟ Cʟᴇᴀʀᴇᴅ Sᴜᴄᴄᴇsꜰᴜʟʟʏ"
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "Mᴇᴅɪᴀ Cʟᴇᴀʀᴇᴅ Sᴜᴄᴄᴇsꜰᴜʟʟʏ"
    
    SAVED_RECVD_DOC_FILE = "Dᴏᴡɴʟᴏᴀᴅ Sᴜᴄᴄᴇssꜰᴜʟʟ "
    
    CUSTOM_CAPTION_UL_FILE = "A Bᴏᴛ Bʏ : @AIOM_BOTS"
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail Found."
    
    NO_VOID_FORMAT_FOUND = "No-One Gonna Help You\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "Already One Process Going On! \n\nCheck Live Status On Log Channel."
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "Hi, I Am Video Compressor Bot \n\n1. Send Me Your Telegram Big Video File \n2. Reply To The file With: /compress 50 \n\n- @AIOM_BOTS -"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
