from django.conf import settings

import asyncio

from telegram import Bot
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.error import TelegramError
from telegram.constants import ParseMode

from api.utils.messages import (build_request_message, 
                                build_client_confirm_transaction_message,
                                build_client_cancel_transaction_message,
                                build_admin_status_transaction_message,
                                build_client_confirmation_attempt_message
                                )


async def send_cancel_order_notifications(data: dict, admins_chat_ids: int, caissiers_chat_id: int, client_chat_id: int): 
    await send_message_to_user(
        message=build_client_cancel_transaction_message(**data),
        user_id=client_chat_id,
    )
    
    await send_message_to_users(
        message=build_admin_status_transaction_message(**data),
        users_ids=admins_chat_ids,
    )

async def send_confirm_order_notifications(data: dict, admins_chat_ids: list, caissiers_chat_id: int, client_chat_id: int):
    await send_message_to_user(
        message=build_client_confirm_transaction_message(**data),
        user_id=client_chat_id,
    )
    
    await send_message_to_users(
        message=build_admin_status_transaction_message(**data),
        users_ids=admins_chat_ids,
    )

async def send_notifications(data, admins_chat_ids, caissiers_chat_ids, client_id): 
    await send_message_order_to_employees(
        message=build_request_message(**data),
        users_ids=caissiers_chat_ids,
        order_id=data['id']
    )
    await send_message_to_users(
        message=build_request_message(**data),
        users_ids=admins_chat_ids
    )
    
    await send_message_to_user(
        message=build_client_confirmation_attempt_message(**data),
        user_id=client_id
    )

async def send_message_order_to_employees(message, users_ids, order_id=-1):
    keyboard = [
            [
                InlineKeyboardButton("ANNULER", callback_data=f"cancel_{order_id}"),
                InlineKeyboardButton("CONFIRMER", callback_data=f"confirm_{order_id}"),
            ],
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await send_message_to_users(message, users_ids, reply_markup=reply_markup)

async def send_message_to_users(message, users_ids, **kwargs):
    tasks = []
    for user_id in users_ids:
        tasks.append(send_message_to_user(message, user_id, **kwargs))
        await asyncio.sleep(0.2)  # Délai de 100ms entre chaque envoi pour éviter le throttling
    await asyncio.gather(*tasks)

semaphore = asyncio.Semaphore(10)  # Limite le nombre de requêtes simultanées

async def send_message_to_user(message, user_id, retries=3, **kwargs):
    bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)

    async with semaphore:  # Limite l'accès à cette section à 10 tâches en même temps
        for attempt in range(retries):
            try:
                await bot.send_message(
                    chat_id=user_id, 
                    text=message, 
                    parse_mode=ParseMode.HTML,
                    **kwargs
                )
                print(f"Message sent successfully to user {user_id}")
                return
            except TelegramError as e:
                if attempt < retries - 1:
                    print(f"Retry {attempt + 1} to send message to user {user_id}")
                    await asyncio.sleep(2)  # Attendre avant de réessayer
                else:
                    print(f"Failed to send message to user {user_id} after {retries} attempts: {e}")