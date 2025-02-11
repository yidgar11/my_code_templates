__author__ = 'yidgar'
import traceback
from loguru import logger

### to use loguru , need first to install :
# pip install loguru 
# then use is simple 

def main():
    # Set up the logger
    logger.add("file.log", rotation="10 MB", compression="zip")

    logger.debug("Debug")
    logger.info("Info")
    logger.warning("Warning")
    logger.error("Error")
    logger.critical("Critical")

if __name__ == "__main__":
    try:
        main()
    except:
        print (traceback.print_exc())
        exit(1)