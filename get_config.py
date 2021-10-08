class getConfig():

    def __init__(self):
        self.PARAMETERS = {}
        self.read_cfg()

    def read_cfg(self):
        with open("config.txt") as read_cfg:
            for line in read_cfg.readlines():
                line = line.split("=")
                self.PARAMETERS[line[0].strip()] = int(line[1].strip())

    def change_monitor_cfg(self):
        new_list = []
        with open("config.txt") as write_changes:
            for line in write_changes.readlines():
                # print(line)
                if "CHANGE_MONITOR = 1" in line:
                    new_list.append("CHANGE_MONITOR = 0\n")
                elif "CHANGE_MONITOR = 0" in line:
                    new_list.append("CHANGE_MONITOR = 1\n")
                else:
                    new_list.append(line)

        with open("config.txt", "w") as wf:
            for line in new_list:
                wf.write(line)

# a = getConfig()
# a.change_monitor_cfg()
# print(a.PARAMETERS)