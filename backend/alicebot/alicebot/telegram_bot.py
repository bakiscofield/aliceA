import logging
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CallbackQueryHandler, ContextTypes
from django.conf import settings

# Configure le logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# Handler pour traiter les confirmations et annulations de commandes
async def buttons_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("Hello")
    from api.models import Employee
    from api.utils import order_utils, bot_utils
    """Gérer la confirmation ou l'annulation d'une commande via boutons interactifs"""
    query = update.callback_query
    await query.answer()
    result = query.data
    
    # Transformer les opérations synchrones en asynchrones
    loop = asyncio.get_event_loop()
    
    # Récupérer l'ordre
    order_id = result.split('_')[1]
    is_confirm = result.startswith("confirm")
    order = await loop.run_in_executor(None, order_utils.change_order_state, is_confirm, order_id)
    
    # Préparation des notifications
    data = {
        'emoji': '',
        'state': order.state,
        'employee': await loop.run_in_executor(None, lambda o: o.client.fullname(), order),
        'numero': order.id,
        'type_operation': order.order_type,
        'client': await loop.run_in_executor(None, lambda o: o.client.fullname(), order),
    }

    # Récupérer les ID de chats
    admins_chat_ids = await loop.run_in_executor(None, lambda: list(
        Employee.objects.filter(user__groups__name__in=["ADMIN", "SUPERADMIN"])
        .values_list('id_chat', flat=True)
    ))
    caissiers_chat_id = await loop.run_in_executor(None, lambda o: o.employee_payment_method.employee.id_chat, order)
    client_chat_id = await loop.run_in_executor(None, lambda o: o.client.id_chat, order)

    # Si confirmation
    if is_confirm:
        data['emoji'] = '✅'
        await bot_utils.send_confirm_order_notifications(
            data=data, admins_chat_ids=admins_chat_ids, 
            caissiers_chat_id=caissiers_chat_id, client_chat_id=client_chat_id
        )
        await query.edit_message_reply_markup(reply_markup=None)  # Retire les boutons après confirmation
    else:
        # Si annulation, proposer à nouveau la confirmation via un bouton
        keyboard = [[InlineKeyboardButton("CONFIRMER", callback_data=f"confirm_{order_id}")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        data['emoji'] = '❌'
        await bot_utils.send_cancel_order_notifications(
            data=data, admins_chat_ids=admins_chat_ids, 
            caissiers_chat_id=caissiers_chat_id, client_chat_id=client_chat_id
        )
        await query.edit_message_reply_markup(reply_markup=reply_markup)


application = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()

def main() -> None:
    # Crée l'instance du bot Telegram
    application = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()

    application.add_handler(CallbackQueryHandler(buttons_handler))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

def run():
    asyncio.run(main())