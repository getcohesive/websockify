class BasePlugin():
    def __init__(self, src=None):
        self.source = src

    def authenticate(self, headers, query,target_host, target_port):
        pass




class BasicHTTPAuth():
    """Verifies Basic Auth headers. Specify src as username:password"""

    def __init__(self, src=None):
        self.src = src

    def authenticate(self, headers,query, target_host, target_port):
       queries = query.split('?',1)
       if len(queries) != 2:
           self.auth_error()
       print("case1 passed")
       params = queries[1].split('&',1)
       print("params:")
       key = ""
       for p in params:
           val = p.split('=',1)
           if val[0] == "token":
               key = val[1]
           if val[0] == "identifier" and key == "":
               key = val[1]
       print("key "+key)
       if not self.validate_creds(key):
                self.demand_auth()


    def validate_creds(self, val):
        if val == self.src:
            return True
        else:
            return False

    def auth_error(self):
        raise AuthenticationError(response_code=403)

    def demand_auth(self):
        raise AuthenticationError(response_code=401,
                                  response_headers={'WWW-Authenticate': 'Basic realm="Websockify"'})
