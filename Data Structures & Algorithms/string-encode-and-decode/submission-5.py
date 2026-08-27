class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_strs = ""
        for ch in strs:
            encoded_strs += str(len(ch)) + "#" + ch

        return encoded_strs

    def decode(self, s: str) -> List[str]:

        decoded_lst = []
        i = 0

        while i < len(s):

            delimiter_pos = s.find('#', i)
            if delimiter_pos == -1:
                break

            length = int(s[i: delimiter_pos])

            start = delimiter_pos + 1
            last = start + length

            decoded_lst.append(s[start: last])

            i = last

        return decoded_lst