import re


class word(str):
    @property
    def prefixes(self):
        for i in range(1, len(self)):
            yield word(self[:i])

    @property
    def splits_of_two(self):
        for i in range(1, len(self)):
            yield word(self[:i]), word(self[i:])

    def first(self, language: str) -> bool:
        if not list(self.prefixes):
            return False
        for prefix in self.prefixes:
            if prefix.in_language(language):
                return False
        return True

    def second(self, language: str) -> bool:
        for u, v in self.splits_of_two:
            if u.separable(language) and v.separable(language):
                return True
        return False

    def separable(self, language: str) -> bool:
        return self.first(language) or self.second(language)

    def in_language(self, language: str) -> bool:
        return not not re.match(language, self)


TEST = word("a")
LANG = "^(aa)|(aaa)$"
print(TEST.separable(LANG))
