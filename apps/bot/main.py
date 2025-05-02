import os
import sys
from http.client import RemoteDisconnected

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")  # noqa

# Initialize Django
import django

django.setup()

import time

import requests

from apps.bot.conf import TOKEN
from apps.bot.filters import AdminFilter
from apps.bot.handlers.user import any_user
from apps.bot.middlewares import antispam_func
from apps.bot.handlers.cinema import handle_message
from apps.bot.handlers.register import handle_callback_query
from apps.bot.query.inlinequery import search_query
from telebot import TeleBot, apihelper

from apps.bot.logger import logger

# Log a message to indicate the bot is starting
logger.info("Starting bot...")

# Enable middleware
apihelper.ENABLE_MIDDLEWARE = True
logger.info("Middlewares enabled")

# I recommend increasing num_threads
bot = TeleBot(TOKEN, num_threads=9)
logger.info("Bot created")


def register_handlers(bot: TeleBot):
    bot.register_message_handler(
        any_user, commands=["start"], admin=False, pass_bot=True
    )
    bot.register_message_handler(handle_message, content_types=["text"], pass_bot=True)
    bot.register_callback_query_handler(
        lambda call: handle_callback_query(call, bot), lambda call: True
    )


register_handlers(bot)
logger.info("Handlers registered")

# Inline query
bot.register_inline_handler(
    callback=lambda query: search_query(bot, query), func=lambda query: True
)
logger.info("Inline location query handler registered")

logger.info(f"@{bot.get_me().username} is ready")

# Middlewares
bot.register_middleware_handler(antispam_func, update_types=["message"])
logger.info("Middlewares registered")

# Custom filters
bot.add_custom_filter(AdminFilter())
logger.info("Custom filters registered")


def run():
    """
    Start the bot's polling loop with robust error handling and exponential backoff.
    """
    initial_retry_delay = 1  # Initial delay in seconds
    retry_delay = initial_retry_delay

    while True:
        try:
            logger.info("Starting bot polling...")
            bot.infinity_polling(timeout=60, long_polling_timeout=60)
            retry_delay = initial_retry_delay

        except KeyboardInterrupt:
            logger.info("KeyboardInterrupt received. Shutting down gracefully.")
            break

        except RemoteDisconnected:
            logger.error(
                "Remote server disconnected unexpectedly. Retrying in 10 seconds..."
            )
            time.sleep(10)

        except requests.exceptions.ReadTimeout:
            logger.error("Read timeout occurred. Retrying immediately...")

        except requests.exceptions.ConnectTimeout:
            logger.error("Connection timeout occurred. Retrying in 15 seconds...")
            time.sleep(15)

        except requests.exceptions.ConnectionError:
            logger.error("Network is unreachable. Retrying in 30 seconds...")
            time.sleep(30)

        except requests.exceptions.RequestException as e:
            logger.error(
                f"Network error occurred: {e}. Retrying in {retry_delay} seconds..."
            )
            time.sleep(retry_delay)
            retry_delay = min(retry_delay * 2, 60)

        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            time.sleep(30)


if __name__ == "__main__":
    logger.info("Bot is running...")
    logger.info("Press Ctrl + C to stop the bot")
    run()
    logger.info("Bot stopped")
