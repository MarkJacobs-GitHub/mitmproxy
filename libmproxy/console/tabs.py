import urwid

class Tabs(urwid.WidgetWrap):
    def __init__(self, tabs, tab_offset=0):
        urwid.WidgetWrap.__init__(self, "")
        self.tab_offset = tab_offset
        self.tabs = tabs
        self.show()

    def _tab(self, content, attr):
        p = urwid.Text(content)
        p = urwid.Padding(p, align="left", width=("relative", 100))
        p = urwid.AttrWrap(p, attr)
        return p

    def keypress(self, size, key):
        if key == "tab":
            self.tab_offset = (self.tab_offset + 1)%(len(self.tabs))
            self.show()
        else:
            return key

    def show(self):
        headers = []
        for i in range(len(self.tabs)):
            txt = self.tabs[i][0]()
            if i == self.tab_offset:
                headers.append(self._tab(txt, "heading"))
            else:
                headers.append(self._tab(txt, "heading_inactive"))
        headers = urwid.Columns(headers)
        self._w = urwid.Frame(
            body = self.tabs[self.tab_offset][1](),
            header = headers
        )
