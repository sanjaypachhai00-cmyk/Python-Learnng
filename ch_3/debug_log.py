# Debugging → finding and fixing errors in your program.
# Logging → recording what your program is doing while it runs.

# # Print debugging
# print(f"{x=}")                    # Python 3.8+

# # Assertions
# assert x > 0, "x must be positive"

# # Interactive debugger
# breakpoint()                      # Python 3.7+

# # pdb module
# import pdb
# pdb.set_trace()
# pdb.post_mortem()                 # inspect crash

# # Reading a traceback: read BOTTOM-UP

                                                            #   import logging

# Quick setup
# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
#     filename="app.log",
#     filemode="a"
# )

# # Log
# logging.debug("detailed info")
# logging.info("normal event")
# logging.warning("something odd")
# logging.error("something failed")
# logging.critical("system down")

# # In except
# logging.exception("Failed")       # auto traceback

# # Per-module logger (best practice)
# logger = logging.getLogger(__name__)
# logger.info("User %s logged in", user)   # lazy formatting

# # Handlers (advanced)
# from logging.handlers import RotatingFileHandler

# handler = RotatingFileHandler("app.log", maxBytes=1_000_000, backupCount=5)
# formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
# handler.setFormatter(formatter)

# logger = logging.getLogger("myapp")
# logger.addHandler(handler)

# # dictConfig (production)
# import logging.config
# logging.config.dictConfig({...})



