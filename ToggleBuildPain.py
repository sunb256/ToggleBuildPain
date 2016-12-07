import sublime
import sublime_plugin

class ToggleBuildPainCommand(sublime_plugin.TextCommand):

  def run(self, edit):
    w_name = 'output.exec'
    window = self.view.window()

    if window.active_panel() == w_name:
      window.run_command("hide_panel", {"panel": w_name})
    else:
      window.run_command("show_panel", {"panel": w_name})