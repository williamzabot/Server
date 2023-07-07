class PingInfo:
    def __init__(self):
        self.url = None
        self.ip = None
        self.date = None
        self.currentTime = None
        self.ttl = None
        self.time = None

    def __str__(self):
        return "Ping do servidor:\nData: {}\nHorário {}\nUrl: {}\nIp: {}\nTTL: {}\nTime (média): {} ms".format(
            self.date, self.currentTime, self.url, self.ip, self.ttl, self.time
        )