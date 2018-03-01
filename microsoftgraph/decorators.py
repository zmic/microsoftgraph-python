from microsoftgraph.exceptions import TokenRequired
from functools import wraps


def token_required(func):
    @wraps(func)
    def helper(*args, **kwargs):
        client = args[0]
        if client.office365 and client.office365_token is None:
            raise TokenRequired('You must set the Token.')
        elif client.token is None:
            raise TokenRequired('You must set the Token.')
        return func(*args, **kwargs)
    return helper
