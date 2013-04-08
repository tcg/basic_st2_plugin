import sublime, sublime_plugin

class SelectionToUpperCommand(sublime_plugin.TextCommand):
    """
    Sublime will take any class that extends one of the sublime_plugin classes
    (TextCommand, WindowCommand or ApplicationCommand), remove the suffix
    Command and then convert the CamelCaseinto underscore_notation for the
    command name.

    Thus, to run this command:
        > CTRL+` to open the console.
        > view.run_command('my_new')
    """

    def run(self, edit):
        selections = self.view.sel()
        # Begin our own single Undo group:
        edit = self.view.begin_edit('my_new')

        for selection in selections:
            # Get the selected string, if any.
            s = self.view.substr(selection)
            s = self.string_to_upper(s)
            self.view.replace(edit, selection, s)

        # End the undo block.
        self.view.end_edit(edit)

    def string_to_upper(self, s):
        return s.upper()
