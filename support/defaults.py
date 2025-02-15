""" !/usr/bin/env python3
    -*- coding: utf-8 -*-
    Name     : inline-tube-mate [ Telegram ]
    Repo     : https://github.com/ShadowKing9/ShadowYtDownloader
    Author   : Shadow King[ https://t.me/ShadowKing9o ]
    Credits  : https://github.com/SpEcHiDe/AnyDLBot """

from presets import Presets
from support.buttons import get_reply_markup
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

async def get_info(username):
    result = []
    set1 = InlineQueryResultArticle(
        title=Presets.DEFAULT_TITLE,
        input_message_content=InputTextMessageContent(
            message_text=Presets.DEFAULT_LINK
        ),
        thumb_url=Presets.DEFAULT_THUMB_URL,
        description=Presets.DEFAULT_DESCRIPTION,
        reply_markup=get_reply_markup(username)
    )
    set2 = InlineQueryResultArticle(
        title=Presets.DEV_TITLE,
        input_message_content=InputTextMessageContent(
            message_text=Presets.DEV_LINK
        ),
        thumb_url=Presets.DEV_THUMB_URL,
        description=Presets.DEV_DESCRIPTION,
        reply_markup=get_reply_markup(username)
    )
    result.extend([set1, set2])
    return result
