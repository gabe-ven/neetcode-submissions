class Solution:

    def encode(self, strs: List[str]) -> str:
        # we want a way to separate each word when we encode it
        # we can get the length of each word and append it to the front of the word
        # then add a delimiter "#" to know the separation
        # ["neet", "code"] --> 4#neet4#code
        # now we know how to decode it

        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        # i is a pointer
        res, i = [], 0

        while i < len(s):
            j = i
            # still at the integer char
            while s[j] != "#":
                j+= 1
            length = int(s[i:j])
            # gives entire string, append to list
            res.append(s[j + 1 : j + 1 + length])
            # beginning of next string
            i = j + 1 + length
        return res


