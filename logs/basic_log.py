import logging

logging.basicConfig(level=logging.INFO,format="%(levelname)s | %(message)s | %(asctime)s",
                    handlers=[logging.FileHandler("logs/app.log"),
                              logging.StreamHandler()])


logger = logging.getLogger(__name__)

