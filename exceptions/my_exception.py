"""My first exception in Python."""


class MyException(BaseException):
    """My class to handle Exceptions."""

    def with_traceback(self):
        """
        My delegation of with_traceback method
        that prints a friendly message.
        """
        print("Deu merda aí irmão, dá seu seus pulo.")
