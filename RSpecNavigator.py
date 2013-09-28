import sublime, sublime_plugin

class RspecExamplesCommand(sublime_plugin.TextCommand):
    PATTERN = '(describe|context|should|it|feature|scenario|test).*do'

    def run(self, edit):
        org_sel = list(self.view.sel())

        regions = [self.view.line(_) for _ in self.view.find_all(self.PATTERN)]
        items   = [self.view.substr(_) for _ in regions]

        def on_done(index):
            if index >= 0:
                region = regions[index]
                self.view.sel().clear()
                self.view.sel().add(region)
                self.view.show_at_center(region)
            else:
                self.view.sel().clear()
                self.view.sel().add_all(org_sel)
                self.view.show(org_sel[0])

        if int(sublime.version()) > 3000:
            self.view.window().show_quick_panel(items, on_done, sublime.MONOSPACE_FONT, -1, on_done)
        else:
            self.view.window().show_quick_panel(items, on_done)