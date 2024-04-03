import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
####################################################
#     functions for encryption and decryption      #
####################################################
def calculate_inverses_mod_26(x):
    """
    Calculate the modular inverse of x modulo 26.

    :param x: An integer representing the value for which the modular inverse is to be calculated.
    :return: The modular inverse of x modulo 26.
    """

    φ_26 = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    inverse = {}
    for i in φ_26:
        for j in φ_26:
            if (1 - i * j) % 26 == 0:
                inverse[i] = j
    return inverse[x]


def abc(k, c):
    """
    Generate the alphabet matrix for affine encryption or decryption.

    :param k: A tuple (a, b) representing the key for the affine cipher where a is the multiplier and b is the constant.
    :param c: An integer representing the ASCII value offset for the alphabet (65 for uppercase, 97 for lowercase).
    :return: A pandas DataFrame representing the alphabet matrix.
    """
    new_abc = [[], []]
    for i in range(26):
        next_cher = k[0] * (i + k[1]) % 26
        new_abc[0].append(next_cher)
        new_abc[1].append(chr(next_cher + c))
    return pd.DataFrame(new_abc[1], index=new_abc[0])


def encryption(data, k, x):
    """
    Encrypt the input data using the affine cipher.

    :param data: A string representing the plaintext message to be encrypted.
    :param k: A tuple (a, b) representing the key for the affine cipher where a is the multiplier and b is the constant.
    :param x: A pandas DataFrame representing the alphabet matrix.
    :return: A string representing the encrypted message.
    """
    ret = []
    for i in data:
        e_x = (k[0] * (int(ord(i)) - 97) + k[1]) % 26
        ret.append(x.loc[e_x][0])
    return ''.join(ret)


def decryption(data, k, x):
    """
    Decrypt the input data using the affine cipher.

    :param data: A string representing the ciphertext message to be decrypted.
    :param k: A tuple (a, b) representing the key for the affine cipher where a is the multiplier and b is the constant.
    :param x: A pandas DataFrame representing the alphabet matrix.
    :return: A string representing the decrypted message.
    """
    b = calculate_inverses_mod_26(k[0])
    ret = []
    for i in data:
        d_x = (b * (int(ord(i)) - 65 - k[1])) % 26
        ret.append(x.loc[d_x][0])
    return ''.join(ret)


def cipher(method: str, data_text: str, k, algorithm: str = None):
    """
    Perform encryption or decryption using the affine cipher.

    :param method: A string specifying the method to be used ('encryption' or 'decryption').
    :param data_text: A string representing the plaintext or ciphertext message.
    :param k: A tuple (a, b) representing the key for the affine cipher where a is the multiplier and b is the constant.
    :param algorithm: A string specifying the algorithm to be used ('shift cipher' or 'affine cipher').
    :return: A string representing the encrypted or decrypted message.
    """
    algorithm_name = {"shift cipher": (1, k), "affine cipher": k}
    if algorithm is not None:
        k = algorithm_name[algorithm]
    c = 65 if method == "encryption" else 97
    x = abc(k, c)
    if method == "encryption":
        return encryption(data_text, k, x)
    else:
        return decryption(data_text, k, x)

####################################################
#     functions for information gathering          #
####################################################
def probability_visualization(x, x_v, y, y_v):
    # Create a DataFrame with absolute differences between x_v and y_v
    diff_df = pd.DataFrame([[abs(x_val - y_val) for y_val in y_v] for x_val in x_v], index=x, columns=y)

    # Set the size of the figure
    plt.figure(figsize=(10, 8))  # Adjust the size as needed

    # Plot the heatmap without annotations
    sns.heatmap(diff_df, cmap='Spectral', annot=False)
    plt.title('Color Heatmap of Differences between x_v and y_v')
    plt.xlabel('y')
    plt.ylabel('x')

    # Adjust font size of the tick labels
    plt.xticks(fontsize=8)  # Adjust font size as needed
    plt.yticks(fontsize=8)  # Adjust font size as needed

    plt.show()


def count_cher_in_text(data_text):
    """
    Counts the occurrences of each letter (A-Z) in the given text data_text.

    :param data_text: The input text data to analyze.
    :return: A pandas DataFrame containing the counts of each letter (A-Z) in the text.
    """
    # Initialize a list to store the counts of each letter (A-Z)
    count_cher = [0] * 26

    # Generate a list of alphabet letters (A-Z)
    abc = [chr(ord('A') + i) for i in range(26)]  # [ A,B,C,D....Z]

    # Iterate through each character in the input text
    for char in data_text:
        # Calculate the index of the character in the count_cher list
        countchar = (ord(char) - ord('A'))  # [0,1,00,]
        # Increment the count for the corresponding letter
        count_cher[countchar] += 1

    # Create a DataFrame to store the counts of each letter
    df = pd.DataFrame(count_cher, index=abc, columns=['Count'])

    # Sort the DataFrame by the count of each letter in descending order
    return df.sort_values(by=['Count'], ascending=False)


def maybe_is_The(text, size=3, top_num=3):
    """
    Find the most frequent n-grams of size 'size' in the given text.

    :param text: A string representing the text.
    :param size: An integer representing the size of n-grams to search for.
    :param top_num: An integer representing the number of top frequent n-grams to return.
    :return: A pandas DataFrame containing the top frequent n-grams.
    """
    n_grams = [text[i: i + size] for i in range(len(text) - size + 1)]
    df_n_grams = pd.DataFrame(n_grams)
    top = df_n_grams.value_counts().head(top_num)
    return top


def info(character_count, frequency_table, top=None, visualization=True):
    """
    Display information about character frequencies and their percentages, and visualize the frequency distribution.

    :param character_count: A pandas DataFrame containing the count of each character.
    :param frequency_table: A pandas DataFrame containing the frequency table.
    :param top: An integer specifying the number of top characters to display. If None, all characters are considered.
    :param visualization: A boolean indicating whether to visualize the frequency distribution. Default is True.
    :return: A pandas DataFrame containing the character count and frequency information.
    """
    if top is None:
        top = len(frequency_table)

    real_percentage = [i[0] / character_count.sum().iloc[0] for i in character_count.head(top).values]
    real_percentage = [round(num, 4) for num in real_percentage]

    Subtotal = [character_count.head(top).index,
                frequency_table.head(top).index,
                frequency_table.head(top).values.flatten(),  # Flatten the array
                character_count.head(top).values.flatten(),  # Flatten the array
                real_percentage
                ]

    if visualization:
        probability_visualization(Subtotal[0], Subtotal[2], Subtotal[1], Subtotal[4])

    info_incidence = pd.DataFrame(Subtotal).transpose()
    return info_incidence

####################################################
#     functions for Saving and reading files       #
####################################################


def open_file(file_name):
    """
    Open and read the contents of a file, converting all text to uppercase.

    :param file_name: A string representing the name of the file.
    :return: A string containing the contents of the file in uppercase.
    """
    with open(file_name, 'r') as f:
        file_contents = f.read().upper()
    return file_contents


def open_file_incidences(frequency_file):
    """
    Open and read the frequency table from a CSV file.

    :param frequency_file: A string representing the name of the CSV file containing the frequency table.
    :return: A pandas DataFrame containing the frequency table.
    """
    frequency_table = pd.read_csv(frequency_file, index_col=0)
    return frequency_table.sort_values(by=['percent'], ascending=False)

def save_decrypted_text(encrypted_text, key, output_file):
    """
    Decrypt the given text using the provided key and save the decrypted text to a file.

    :param encrypted_text: A string representing the encrypted text.
    :param key: A tuple (a, b) representing the key for the affine cipher where a is the multiplier and b is the constant.
    :param output_file: A string representing the name of the output file.
    :return: None
    """
    decrypted_text = cipher(method="decryption", data_text=encrypted_text, k=key)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(decrypted_text)
    print(f"Decrypted text using key {key}: \n{decrypted_text}")


if __name__ == "__main__":
    # Example usage
    text = 'char'
    K = (3, 10)
    a = cipher(method="encryption", data_text=text, k=K)
    b = cipher(method="decryption", data_text=a, k=K)
    print(f"Encrypted: {text} --> {a}")
    print(f"Decrypted: {a} --> {b}")