import logging

class LogGen:
    @staticmethod
    def loggg():
        logging.basicConfig(filename="C:\\Users\\Arun\\PycharmProjects\\nopsaikanchi\\Logs\\saa.log",
                       # format='%(asctime)s:%(levelname)s:%(message)s',
                       # datefmt='%d%m%Y %I:%M:%S %p'
                            )
        logger_object=logging.getLogger(__name__)
        fhandler=logging.FileHandler("C:\\Users\\Arun\\PycharmProjects\\nopsaikanchi\\Logs\\nop.log")
        formatter= logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
        fhandler.setFormatter(formatter)
        logger_object.addHandler(fhandler)
        logger_object.setLevel(logging.INFO)
        return logger_object


