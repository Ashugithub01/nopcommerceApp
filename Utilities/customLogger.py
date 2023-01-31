import logging

class LogGen:

    @staticmethod
    def loggen():
        FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
        filename = './/Logs//automatiom.log'
        logging.basicConfig(format=FORMAT, Filename=filename)
        #logging.FileHandler('.//Logs//automatiom.log')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

    """
    @staticmethod
    def loggen():
        # logging.basicConfig(Filename=".//Logs//automatiom.log", format='%(asctime)s: %(levelname)s :%(message)s', datefmt='%m/%d/%Y %I:%M:%S %P')
        logger = logging.getLogger()
        fh = logging.FileHandler('.//Logs//automatiom.log')
        fh.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger
    """