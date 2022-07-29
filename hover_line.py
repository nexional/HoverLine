import sublime
import sublime_plugin
import re
import math
import html
from textwrap import wrap
this_package = 'HoverLine: '

def plugin_loaded():
    global settings
    settings = sublime.load_settings('HoverLine.sublime-settings')
    settings.clear_on_change('enable')
    settings.add_on_change('enable', HoverLineToolTipCommand.is_enabled())

class HoverLineCommand(sublime_plugin.WindowCommand):
    def run(self, toggle_package=False, set_tooltip_timeout=False):
        global settings
        win = self.window
        if True not in locals().values(): return
        if locals()['toggle_package']:
            settings.clear_on_change('enable')
            settings.set('enable', not settings.get('enable'))
            settings.add_on_change('enable', HoverLineToolTipCommand.is_enabled())
            sublime.save_settings('HoverLine.sublime-settings')
            sublime.message_dialog(this_package + 'package now ' + ('enabled' if settings.get('enable') else 'disabled'))
        elif locals()['set_tooltip_timeout']:
            num = settings.get('tooltip_timeout')
            if num is None or not str(num).isdigit() or int(num) < 0: num = 3
            def on_done(num):
                if num and str(num).isdigit() and int(num) >= 0:
                    settings.set('tooltip_timeout', int(num))
                    sublime.save_settings('HoverLine.sublime-settings')
                    sublime.message_dialog(this_package + 'tooltip_timeout updated to ' + str(num))
                else:
                    sublime.error_message(this_package + 'please provide a valid whole number')
                    win.show_input_panel('tooltip_timeout:', str(num), on_done, None, None)
            win.show_input_panel('tooltip_timeout:', str(num), on_done, None, None)
        return True

class HoverLineToolTipCommand(sublime_plugin.ViewEventListener):
    def on_hover(self, point, hover_zone):
        global settings
        view = self.view
        if not self.is_enabled() or view.settings().get('word_wrap'): return
        row = view.rowcol(point)[0]
        max_width = math.floor(view.viewport_extent()[0])
        wrap_len = math.floor(max_width / view.em_width())
        content = view.substr(view.line(view.text_point(row, 0)))
        first_visible_col = math.floor(view.viewport_position()[0] / view.em_width())
        if wrap_len >= len(content) and first_visible_col == 0: return

        clist = wrap(text=content, width=wrap_len-2, replace_whitespace=False, drop_whitespace=False, break_long_words=True, tabsize=view.settings().get('tab_size'))
        if len(clist) > 10: clist = wrap(text=content, width=wrap_len-4, replace_whitespace=False, drop_whitespace=False, break_long_words=True, tabsize=view.settings().get('tab_size'))

        content = '<div>' + '<br>'.join(re.sub(r'\s', '&nbsp;', html.escape(x)) for x in clist) + '</div>'
        max_height = int(min(len(clist), 10) * view.line_height()) + 30
        view.show_popup(content=content, location=view.text_point(row, first_visible_col+1), max_width=max_width, max_height=max_height)
        tooltip_timeout = int(settings.get('tooltip_timeout'))
        if tooltip_timeout > 0: sublime.set_timeout_async(lambda: view.hide_popup(), tooltip_timeout * 1000)

    def is_enabled(self=None):
        global settings
        return settings.get('enable')


