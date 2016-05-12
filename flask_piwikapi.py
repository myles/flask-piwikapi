class FlaskRequest(object):
    """
    A Request class to connect the Piwik API to Flask
    """

    def __init__(self, request):
        """
        :param request: Flask request object.
        :type request: flask.Request
        :rtype: None
        """
        self.request = request

    @property
    def META(self):
        """
        Return request headers.

        :rtype: dict
        """
        return self.request.headers

    def is_secure(self):
        """
        Returns a boolean, if the connection is secured.

        :rtype: bool
        """
        return self.request.is_secure
