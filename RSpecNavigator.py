# coding: utf-8
import sublime, sublime_plugin
import re
import codecs

class RspecExamplesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_name = self.view.file_name()
        if file_name.endswith(".rb") == False:
            return
        with codecs.open(file_name, 'r', 'utf-8') as f:
            text = f.read()

        matches = []
        items = []
        pattern = 'describe|context|should|it|feature|scenario|test'

        for m in re.finditer(r'( *)(' + pattern + r')\s+[\'"]{0,1}([^\'"]+)[\'"]{0,1}\s+do', text):
            matches.append(m)
            item = m.group()
            items.append(item)

        def on_done(index):
            if index >= 0:
                self.view.sel().clear()
                m = matches[index]
                region = sublime.Region(m.start(), m.end())
                e = self.view.begin_edit()
                self.view.sel().clear()
                self.view.sel().add(region)
                self.view.show(region)
                self.view.end_edit(e)

        self.view.window().show_quick_panel(items, on_done)
