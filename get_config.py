from os import read


class getConfig():

    def __init__(self):
        self.params = {}

    def read_cfg(self):
        with open("config.txt") as read_cfg:
            for line in read_cfg.readlines():
                line = line.split("=")
                self.params[line[0].strip()] = line[1].strip()

    def change_monitor_cfg(self):
        with open("config.txt", "r+") as write_changes:
            for line in write_changes.readlines():
                line = line.split("=")
                if line[0].strip() == "CHANGE_MONITOR":
                    print(line[0])
                    write_changes.write("CHANGE_MONITOR = 0") 