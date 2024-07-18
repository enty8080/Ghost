"""
MIT License

Copyright (c) 2020-2024 EntySec

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from badges import Badges, Tables


class Module(Badges, Tables):
    """ Subclass of ghost.lib module.

    This subclass of ghost.lib module is intended for providing
    wrapper for a module.
    """

    def __init__(self, info: dict = {}) -> None:
        self.info = {
            'Category': "",
            'Name': "",
            'Authors': [
                ''
            ],
            'Description': "",
            'Usage': "",
            'MinArgs': 0,
            'NeedsRoot': False
        }
        self.info.update(info)
        self.device = None

    def run(self, argc: int, argv: list) -> None:
        """ Run this module.

        :param int argc: number of arguments
        :param list argv: arguments
        :return None: None
        """

        pass
