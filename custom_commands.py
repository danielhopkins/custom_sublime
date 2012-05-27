import sublime, sublime_plugin

class ToggleGutterCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # grab the gutter setting from the current view
    # and set all views to "not" that
    first_setting = self.view.settings().get("gutter")

    for v in self.view.window().views():
      v.settings().set("gutter", not first_setting)

class ToggleDarkLightCommand(sublime_plugin.WindowCommand):
  def run(self):
    first_setting = self.window.views()[0].settings().get("color_scheme").find("Light")

    new_setting   = "Packages/Color Scheme - Default/Solarized (Light).tmTheme"
    if first_setting != -1:
      new_setting = "Packages/Color Scheme - Default/Solarized (Dark).tmTheme"

    for v in self.window.views():
      v.settings().set("color_scheme", new_setting)

