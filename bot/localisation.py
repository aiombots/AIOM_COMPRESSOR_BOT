#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AbirHasan2005

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "<b>Hᴇʟʟᴏ 👋,\n\nTʜɪs Is A Tᴇʟᴇɢʀᴀᴍ Vɪᴅᴇᴏ Cᴏᴍᴘʀᴇss Bᴏᴛ.\n\nSᴇɴᴅ Mᴇ Aɴʏ Tᴇʟᴇɢʀᴀᴍ Bɪɢ Vɪᴅᴇᴏ Fɪʟᴇ I Wɪʟʟ Cᴏᴍᴘʀᴇss Iᴛ Tᴏ A Sᴍᴀʟʟ Vɪᴅᴇᴏ Fɪʟᴇ!\n\n/help Fᴏʀ Mᴏʀᴇ Dᴇᴛᴀɪʟs...</b>"

    ABS_TEXT = " Please don't be selfish."
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "Downloading To My Server...\n"
    
    UPLOAD_START = "Uploading To Telegram...\n"
    
    COMPRESS_START = "Trying to compress..."
    
    RCHD_BOT_API_LIMIT = "Size Greater Than Maximum Allowed Size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} Seconds.\nDetected File Size: {}\nSorry. But, I Cannot Upload Files Greater Than 1.95GB Due To Telegram API limitations."
    
    COMPRESS_SUCCESS = "Downloaded in {}\n\nCompressed in {}\n\nUploaded in {}\n\nBy @AIOM_BOTS"

    COMPRESS_PROGRESS = "ETA: {}\nProgress: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file Thumbnail Saved. This Image Will Be Used In The Video / file."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "Custom Thumbnail Cleared Succesfully."
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "Media Cleared Succesfully."
    
    SAVED_RECVD_DOC_FILE = "Downloaded Successfully."
    
    CUSTOM_CAPTION_UL_FILE = " "
    
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

    
