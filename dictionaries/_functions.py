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


def transliterate(string: str, dictionary: dict, sep=" ", upper=False, like_sep="", remove="",
                  raise_error=False) -> str:
    """Transliterates convertibles UTF8 chars of a given language to its ASCII equivalent

    sep              (str): string delimiter. Whitespace by default.
    upper           (bool): if it's True, returns a string converted to uppercase.
                            False by default.
    like_sep (str or list): chars treated as separator.
    remove   (str or list): chars to remove in the string
    raise_error     (bool): If it's True raise ValueError if a char is not in dict.

    Note: sep and like_sep kwargs are vestiges of a previous version of this function.

    """
    if remove:
        for i in range(len(remove)):
            string = string.replace(remove[i], "")
    if like_sep:
        for i in range(len(like_sep)):
            string = string.replace(like_sep[i], sep)
    s = ""
    for char in string:
        if not raise_error:
            s += dictionary[char] if char in dictionary else char
        else:
            try:
                s += dictionary[char]
            except KeyError as ex:
                raise ValueError("'%s' is not in dictionary" % ex.args[0])
    return s if not upper else s.upper()


def str2unicode(string):
    """Prints the unicode hex representation of each char in a string

        Note: Only for development purposes"""
    def gv(s):
        return s[2:].zfill(4)
    print("{")
    for c in string:
        u = c.encode("unicode_escape").decode()  # é -> \xe9, a -> a, 𐍈 -> \U00010348
        ln = len(u)
        prefix = "\\u" if ln < 7 else u[:2]
        value = gv(hex(ord(u))) if ln < 2 else gv(u) if ln < 7 else u[2:]
        # print('%s: u"%s%s"' % (c, prefix, value.upper()))
        print('    u"%s%s": "%s",' % (prefix, value.upper(), c))
    print("}")
