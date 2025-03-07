import re

def prepare_text(text):

    text = re.sub(r'[^A-Za-z]', '', text).upper().replace('J', 'I')
    prepared_text = ''
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'X'
        if a == b:
            prepared_text += a + 'X'
            i += 1
        else:
            prepared_text += a + b
            i += 2
    if len(prepared_text) % 2 == 1:
        prepared_text += 'X'
    return prepared_text

def create_playfair_matrix(keyword):
    
    keyword = keyword.upper().replace('J', 'I')
    seen = set()
    matrix = []
    for char in keyword + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            seen.add(char)
            matrix.append(char)
    return [matrix[i * 5:(i + 1) * 5] for i in range(5)]

def find_position(matrix, letter):
    
    for i, row in enumerate(matrix):
        if letter in row:
            return i, row.index(letter)

def process_pair(matrix, a, b, mode='encrypt'):

    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)
    
    if row1 == row2:  
        col1 = (col1 + 1) % 5 if mode == 'encrypt' else (col1 - 1) % 5
        col2 = (col2 + 1) % 5 if mode == 'encrypt' else (col2 - 1) % 5
    elif col1 == col2:  
        row1 = (row1 + 1) % 5 if mode == 'encrypt' else (row1 - 1) % 5
        row2 = (row2 + 1) % 5 if mode == 'encrypt' else (row2 - 1) % 5
    else:  
        col1, col2 = col2, col1
    
    return matrix[row1][col1] + matrix[row2][col2]

def playfair_cipher(text, matrix, mode='encrypt'):
    text = prepare_text(text)
    result = ''
    for i in range(0, len(text), 2):
        result += process_pair(matrix, text[i], text[i+1], mode)
    return result

def main():
    keyword = input("enter key :  ").strip()
    if not keyword.isalpha():
        print("enter your alph ")
        return

    matrix = create_playfair_matrix(keyword)
    
    print("\nplayfair:")
    for row in matrix:
        print(' '.join(row))

    while True:
        choice = input("\nاختر العملية (e: تشفير، d: فك تشفير، q: خروج): ").lower()
        if choice == 'q':
            break
        text = input("enter txt ")
        if choice == 'e':
            print("C txt :", playfair_cipher(text, matrix, 'encrypt'))
        elif choice == 'd':
            print("P txt :", playfair_cipher(text, matrix, 'decrypt'))
        else:
            print("wronge valid")

if __name__ == "_main_":
    main()
