class ColorMarker(object):
    def __init__(self, editor, active_color):
        super(ColorMarker, self).__init__()
        
        self.editor       = editor
        self.active_color = active_color

    def colorize(self, line_number, color, clearbool):
        
        block = self.editor.document().findBlockByLineNumber(line_number)
        diff = line_number - block.firstLineNumber()
        count = 0
        if diff == 0:
            line_len = len(block.text().split("\n")[0])
        else:
            # Probably don't need. Just in case a block has more than 1 line.
            line_len = 0
            for i, item in enumerate(block.text().split("\n")):
                # Find start
                if i + 1 == diff: # + for line offset. split starts 0
                    count += 2 # \n
                    line_len = len(item)
                else:
                    count += len(item)

        loc = block.position() + count

        # Set the cursor to select the text
        cursor = self.editor.textCursor()

        cursor.setPosition(loc)
        cursor.movePosition(cursor.Right, cursor.KeepAnchor, line_len)

        charf = block.charFormat()
        if clearbool == False:
            charf.setForeground(color)
        else:
            charf.clearForeground()
        cursor.setCharFormat(charf)
        
    def activate(self, line_number):
        self.colorize(line_number, self.active_color, False)
        
    def reset(self, line_number):
        self.colorize(line_number, self.active_color, True)

