import sublime, sublime_plugin

class RspecExamplesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        pattern = '(describe|context|should|it|feature|scenario|test).*do'

        regions = self.view.find_all(pattern)
        regions = map(lambda _: self.view.line(_), regions)
        items   = map(lambda _: self.view.substr(_), regions)

        def on_done(index):
            if index >= 0:
                self.view.sel().clear()
                region = regions[index]
                e = self.view.begin_edit()
                self.view.sel().clear()
                self.view.sel().add(region)
                self.view.show(region)
                self.view.end_edit(e)

        self.view.window().show_quick_panel(items, on_done)
