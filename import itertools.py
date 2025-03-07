import itertools
import random


cipher_text = input("Enter the dtxt : ")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

max_attempts = 10  
print("please wait....\n")

for i, key in enumerate(itertools.islice(itertools.permutations(alphabet), max_attempts)):
   
    decryption_map = dict(zip(key, alphabet))
    decrypted_text = "".join(decryption_map.get(char, char) for char in cipher_text)
    print(f"احتمال {i+1}: {decrypted_text}")

print("\n 10 solution done ")