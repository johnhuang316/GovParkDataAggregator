class ApiError(Exception):
    def __init__(self, original_exception):
        self.original_exception = original_exception
        super().__init__(str(original_exception))
        