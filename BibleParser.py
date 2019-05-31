class BibleParser():
    file = 'bible.txt'
    bible = []

    def readBible(self):
        with open(self.file) as f:
            for line1, line2 in zip(f,f):
                line1.rstrip()
                line1 += line2
                self.bible.append(line1)
                f.readline()
        return self.bible