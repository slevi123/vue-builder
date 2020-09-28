

class CodeChecks:

    def bracket_check(self, text):
        """Check if that if every open bracket has a closing one."""
        counter = 0
        for letter in text:
            if letter == '{':
                counter += 1
            elif letter == '}':
                counter -= 1
                if counter < 0:
                    raise Exception("Missing opening/closing bracket")  # TODO: custom exceptions
        if counter == 0:
            return True
        else:
            raise Exception("Missing opening/closing bracket")  # TODO: custom exceptions
