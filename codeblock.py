from pathlib import Path


class CodeBlock:
    def __init__(self, name: str, content: str):

        self.name = name.strip()
        self.content = content.strip()
        self.type = 'simple'

        self.rendered = None

    # @property
    # def rendered(self):
    #     return f"\t{self.name}: {{\n\t\t{self.content}\n\t}}"

    @classmethod
    def read_from_a_file(cls, file: Path):
        raw_text = file.resolve().read_text()
        class_statement_end = raw_text.find('class') + len('class')
        if class_statement_end == len('class')-1:
            raise Exception("Nothing to compile!")  # TODO: to create custom exception classes

        text = raw_text[class_statement_end:]

        first_brace = text.find('{')
        app_name = text[:first_brace].strip()

        text = text[first_brace + 1:-1]  # text wout braces

        return app_name, cls.split_by_braces(text)

    @classmethod
    def split_by_braces(cls, text):
        code_blocks = []
        expexted_character = '{'
        name = ''
        content = ''
        for letter in text:
            if expexted_character == '{':
                if expexted_character == letter:
                    expexted_character = '}'
                else:
                    name += letter
            elif expexted_character == '}':
                if expexted_character == letter:
                    code_blocks.append(cls(name, content))
                    expexted_character = ';'
                else:
                    content += letter
            elif expexted_character == ';' == letter:
                name = ''
                content = ''
                expexted_character = '{'

        return code_blocks

    def __repr__(self):
        return self.name


class MethodLikeBlock(CodeBlock):
    name = ""
    list_of_instances = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list_of_instances.append(self)