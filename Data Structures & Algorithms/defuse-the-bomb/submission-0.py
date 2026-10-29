class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        decrypted_code = [0] * n

        if k == 0:
            return [0] * n

        if k > 0:
            start = 1
            end = k

        elif k < 0:
            k = -k
            start = n - k
            end = n - 1

        decrypted_code[0] = sum(code[start: end + 1])

        for i in range(1, n):
            end += 1
            decrypted_code[i] = decrypted_code[i - 1] - code[start % n] + code[end % n]
            start += 1

        return decrypted_code