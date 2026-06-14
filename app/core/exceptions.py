# create business exception class:
class BusinessException(Exception):

    # initialize business exception:
    def __init__(
        self,
        message: str, # message
        status_code: int = 400 # status code
    ):
        self.message = message # message
        self.status_code = status_code # status code