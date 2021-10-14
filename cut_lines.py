from cudatext import *

class Command:
    def startEndLine(self, caret):
        startLine = caret[1]
        endLine = caret[3]
        if endLine < 0:
            endLine = startLine
        return min(startLine, endLine), max(startLine, endLine)

    def cut_selected_lines(self):  # menu item, for keyboard shortcut
        line2text = {}

        for caret in ed.get_carets():
            startLine, endLine = self.startEndLine(caret)
            for i in range(startLine, endLine + 1):
                line2text[i] = ed.get_text_line(i)

        lines = list(line2text.keys())
        lines.sort()

        texts = []
        for line in lines:
            texts.append(line2text[line])
        texts.append("")

        app_proc(PROC_SET_CLIP, "\n".join(texts))

        for i in range(len(lines) - 1, -1, -1):
            line = lines[i]
            text = line2text[line]
            ed.delete(0, line, 0, line + 1)

        ed.set_caret(0, lines[0])