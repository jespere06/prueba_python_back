import logging
import sys

LOG_FORMAT = '%(levelname)s:  (%(name)s) %(message)s'

LEVEL_COLORS = {
     'INFO': '\033[94m',        # Azul
    'WARNING': '\033[93m',      # Amarillo
    'ERROR': '\033[91m',        # Rojo
}

RESET = '\033[0m'
HIGHLIGHT = '\033[96m'

class ColoredFormatter(logging.Formatter):
    def format(self, record):
        color = LEVEL_COLORS.get(record.levelname, '')
        record.levelname = f'{color}{record.levelname}{RESET}'
        record.name = f'{HIGHLIGHT}{record.name}{RESET}'
        return super().format(record)

def setup_logger():
    
    handler =logging.StreamHandler(sys.stdout)
    formatter = ColoredFormatter(LOG_FORMAT)
    handler.setFormatter(formatter)
    
    logging.basicConfig(level=logging.WARNING, format=LOG_FORMAT, handlers=[handler])