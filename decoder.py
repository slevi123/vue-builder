import render_actions as ra
from pathlib import Path

from codeblock import CodeBlock


class Decoder:
    """  """
    def __init__(self, input_path: Path, output_path: Path, minimal=''):

        self.input_path, self.output_path = input_path.resolve(), output_path.resolve()

        self.minimal = minimal  # {False, visible, True}

        if not minimal:
            self.render_actions = {
                "simple": ra.default_render_action,
            }
        elif minimal == 'visible':
            self.render_actions = {
                "simple": ra.default_render_action_visible,
            }
        else:
            self.render_actions = {
                "simple": ra.default_render_action_min,
            }

        self.method_like_blocks = {}

    def run_checks(self):
        pass

    def _render_file(self):
        """for now it renders one file"""

        app_name, code_blocks = CodeBlock.read_from_a_file(self.input_path)

        if self.minimal:
            start__string = f"var {app_name} = new Vue({{"
            join_string = ","
            end_string = "})"
        else:
            start__string = f"var {app_name} = new Vue({{\n"
            join_string = ",\n"
            end_string = "\n})"

        for code_block in code_blocks:
            render_action = self.render_actions.get(code_block.type, ra.default_render_action)
            render_action(code_block)

        return start__string + join_string.join(map(lambda x: x.rendered, code_blocks)) + end_string

    def compile_file(self):
        self.run_checks()
        self.output_path.write_text(self._render_file())
        print("File compiled successfully.")


if __name__ == "__main__":
    Decoder(input_path=Path('./test_files/test_1.sljs'),  output_path=Path('./test_files/test_1.js'), minimal='')\
        .compile_file()

