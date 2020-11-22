import logging, logging.handlers
import os
import time
"""Basic logging module that will probably be replaced my the user of Deck.
Set $DECK_LOG_LEVEL to control log level.
"""

LOG_LEVEL = os.getenv("DECK_LOG_LEVEL")

if not LOG_LEVEL or LOG_LEVEL == "":
    LOG_LEVEL=logging.INFO
    

LOG_FNAME = 'logs/deck_of_cards.log'
os.makedirs(os.path.dirname(LOG_FNAME), exist_ok=True)


logger = logging.getLogger('log')
logger.setLevel(LOG_LEVEL)
handler = logging.FileHandler(LOG_FNAME)
handler.setLevel(LOG_LEVEL)
formatter = logging.Formatter('%(asctime)s %(levelname)8s: %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("log configured")
