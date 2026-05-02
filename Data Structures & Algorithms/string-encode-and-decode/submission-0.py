class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += f"{len(s)}#{s}"
        return encoded_string

    def decode(self, s: str) -> list[str]:
        decoded_list = []
        i = 0
        while i < len(s):
            j = s.find('#', i)  # Find the delimiter
            length = int(s[i:j])  # Extract the length
            
            # Extract the actual string
            decoded_list.append(s[j + 1 : j + 1 + length])
            
            # Move to the start of the next encoded segment
            i = j + 1 + length
        return decoded_list