import textwrap


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def __str__(self):
        output = ''
        # * Prints the current room name
        output += self.name + ': ' + '\n'
        wrapper = textwrap.TextWrapper(width=50)
        word_list = wrapper.wrap(text=self.description)
        # * Prints the current description
        for e in word_list:
            output += e + '\n'
        if self.items:
            output += 'In the area you see: \n'
            for x in self.items:
                output += x.name + '\n'
        return output
