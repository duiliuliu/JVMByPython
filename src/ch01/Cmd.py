class Cmd():

    versionFlag = False
    cpOption = ""
    className = ""
    args = []

    def __init__(self, options, argvs):
        if options.versionFlag:
            self.__printVersion()
        elif options.cpOption:
            self.cpOption = options.cpOption

        if argvs:
            self.className = argvs[0]
            self.args = argvs[1:] if argvs[1:] else []

    def __printVersion(self):
        print("version 0.0.1")

    def printClasspath(self):
        print("classpath:{0} class:{1} args:{2}\n".format(self.cpOption, self.className, " ".join(self.args)))