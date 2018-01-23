"""
From https://stackoverflow.com/a/13882791/2452770
"""

import datetime, getpass
import sublime, sublime_plugin


class AddDateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command(
            "insert_snippet",
            {"contents": "[{}]".format(
                datetime.date.today().strftime("%Y-%m-%d"))
            }
        )


class AddTimeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command(
            "insert_snippet",
            {"contents": datetime.datetime.now().strftime("%H:%M")}
        )
