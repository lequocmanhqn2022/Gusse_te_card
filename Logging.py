import logging

logging.basicConfig(level=logging.CRITICAL, filename="log.log", filemode="w")

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")