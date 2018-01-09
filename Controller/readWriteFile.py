class TopScore:
    def __init__(self, file):
        self.file=file

    def __readFromFile(self):
        """
            Get the top Score from file
        """
        with open(self.file, "r") as f:
            topScore=f.readline()
            if topScore =="":
                topScore=0
        return topScore

    def getTopScore(self):
        return self.__readFromFile()

    def __writeToFile(self, score):
        """
            Write the new score in the file
        """
        with open(self.file, "w") as f:
            f.write(str(score))

    def setNewTopScore(self, score):
        self.__writeToFile(score)
