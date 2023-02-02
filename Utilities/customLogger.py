import logging

class LogGen:
    """
    # not runnign code------
    @staticmethod
    def loggen():
        logging.basicConfig(filename="C://Users//Asheesh//PycharmProjects//nopcommerceApp//Logs//automatiom.log", format='%(asctime)s: %(levelname)s: %(message)s', level=logging.DEBUG)
        #logging.FileHandler('.//Logs//automatiom.log')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
    """

    @staticmethod
    def loggen():
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        logger.setLevel(logging.DEBUG)

        f_handler = logging.FileHandler('./Logs/Report.log')
        formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')

        f_handler.setFormatter(formatter)
        logger.addHandler(f_handler)
        return logger

    """ 
    # running code ------
    import logging
    
    logging.basicConfig(filename="C://Users//Asheesh//PycharmProjects//nopcommerceApp//Logs//automatiom.log", format='%(asctime)s: %(levelname)s: %(message)s', level=logging.DEBUG)
    
    logging.debug("this is test message")
    """