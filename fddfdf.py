""" Atbash Cipher"""

def main():
    """Atbash Cipher"""
    text = input()
    test = text.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"\
,"zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA")
    print(text.translate(test))
main()
