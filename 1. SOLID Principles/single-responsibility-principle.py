class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count = self.count + 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, filename):
    #     pass
    #
    # def low_from_web(self, uri):
    #     pass


class PersistenceManager:
    @staticmethod
    def save(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()

    def load(self, filename):
        pass

    def low_from_web(self, uri):
        pass


j = Journal()
j.add_entry('I cried today.')
j.add_entry('I ate a bug.')
print(f'Journal entries: {j}')

file = r'c:\temp\journal.txt'
PersistenceManager.save(j, file)

with open(file) as fh:
    print(fh.read())
