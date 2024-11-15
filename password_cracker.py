import hashlib

def load_wordlist(filepath):
    encodings = ['utf-8', 'latin1', 'ISO-8859-1'] 
    for encoding in encodings:
        try:
            with open(filepath, "r", encoding=encoding) as file:
                return file.read().splitlines()
        except UnicodeDecodeError:
            print(f"Failed to decode the wordlist file using {encoding}. Trying another encoding...")
        except FileNotFoundError:
            print("Wordlist file not found.")
            exit()
    print("Unable to decode the file with supported encodings.")
    exit()

def crack_password(hash_to_crack, wordlist):
    for password in wordlist:
        hashed_password = hashlib.md5(password.encode()).hexdigest()  
        if hashed_password == hash_to_crack:
            return password
    return None

# Main function
def main():
    print("Password Cracking Tool with Hashing Algorithms")


    wordlist_path = input("Enter the path to the wordlist file: ")


    wordlist = load_wordlist(wordlist_path)

    hash_to_crack = input("Enter the hash to crack: ").strip()


    cracked_password = crack_password(hash_to_crack, wordlist)

    if cracked_password:
        print(f"Password found: {cracked_password}")
    else:
        print("Password not found in the wordlist.")

if __name__ == "__main__":
    main()
