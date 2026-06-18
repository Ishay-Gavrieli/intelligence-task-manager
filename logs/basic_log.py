import logging

logging.basicConfig(level=logging.INFO,format="%(levelname)s | %(message)s | %(asctime)s",
                    handlers=[logging.FileHandler("app.log"),
                              logging.StreamHandler()])


logger = logging.getLogger(__name__)


if __name__=="__main__":
    logger.info("start the logging")