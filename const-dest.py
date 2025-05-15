class Logger:
    def __init__(self):
        print("Logger object has been created.")

    def __del__(self):
        print("Logger object is being destroyed.")

logger = Logger()

# Optionally delete manually to trigger __del__
del logger
