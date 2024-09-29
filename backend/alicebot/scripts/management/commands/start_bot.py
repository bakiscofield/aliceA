from django.core.management.base import BaseCommand
import asyncio
from alicebot.telegram_bot import run

class Command(BaseCommand):
    help = 'Démarre le bot Telegram'

    def handle(self, *args, **options):
        self.stdout.write('Démarrage du bot Telegram...')
        run()