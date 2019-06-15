# -*- coding: UTF-8 -*-

# GNU General Public License v3.0
#
# Permissions of this strong copyleft license are conditioned on making available
# complete source code of licensed works and modifications, which include larger works
# using a licensed work, under the same license. Copyright and license notices must be
# preserved. Contributors provide an express grant of patent rights.
#
# For more information on this, and how to apply and follow theGNU GPL, see:
# http://www.gnu.org/licenses
#
# (ɔ) Iván Rincón 2019

punctuation = {
    u"\u0021": "!",
    u"\u0022": '"',
    u"\u0023": "#",
    u"\u0024": "$",
    u"\u0025": "%",
    u"\u0026": "&",
    u"\u0027": "'",
    u"\u0028": "(",
    u"\u0029": ")",
    u"\u002A": "*",
    u"\u002B": "+",
    u"\u002C": ",",
    u"\u002D": "-",
    u"\u002E": ".",
    u"\u002F": "/",
    u"\u003A": ":",
    u"\u003B": ";",
    u"\u003C": "<",
    u"\u003D": "=",
    u"\u003E": ">",
    u"\u003F": "?",
    u"\u0040": "@",
    u"\u005B": "[",
    u"\u005C": "\\",
    u"\u005D": "]",
    u"\u005E": "^",
    u"\u005F": "_",
    u"\u0060": "`",
    u"\u007B": "{",
    u"\u007C": "|",
    u"\u007D": "}",
    u"\u007E": "~",
    u"\u00BF": "¿",
    u"\u00A1": "¡",
}

digits = {
    u"\u0030": "0",
    u"\u0031": "1",
    u"\u0032": "2",
    u"\u0033": "3",
    u"\u0034": "4",
    u"\u0035": "5",
    u"\u0036": "6",
    u"\u0037": "7",
    u"\u0038": "8",
    u"\u0039": "9",
}

whitespace = {
    u"\u0020": " ",   # whitespace
    u"\u0009": "\t",  # horizontal tab
    u"\u000A": "\n",  # new line
    u"\u000D": "\r",  # carriage return
    u"\u000B": "\v",  # vertical tab
    u"\u000C": "\f"   # new page
}

printable = {}

printable.update(punctuation)
printable.update(digits)
printable.update(whitespace)
