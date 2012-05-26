import sublime, sublime_plugin

class ToggleGutterCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # grab the gutter setting from the current view
    # and set all views to "not" that
    first_setting = self.view.settings().get("gutter")

    for v in self.view.window().views():
      v.settings().set("gutter", not first_setting)
