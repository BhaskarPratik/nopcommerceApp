import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="E://nopcommerceApp//Logs//automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
