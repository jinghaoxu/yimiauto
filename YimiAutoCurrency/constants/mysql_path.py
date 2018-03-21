class CsMysqlPath(object):
    def __init__(self):
        self._host = ''
        self._port = ''
        self._user = ''
        self._passwd = ''
        self._db = ''

    def get_host(self):
        return self._host

    def get_port(self):
        return self._port

    def get_user(self):
        return self._user

    def get_passwd(self):
        return self._passwd

    def get_db(self):
        return self._db

    def set_host(self, value):
        self._host = str(value)

    def set_port(self, value):
        self._port = str(value)

    def set_user(self, value):
        self._user = str(value)

    def set_passwd(self, value):
        self._passwd = str(value)

    def set_db(self, value):
        self._db = str(value)


if __name__ == '__main__':
    a = CsMysqlPath()
    print(a.get_db())
