__author__ = 'subin'
import random
class Caesar_cipher():
    def Encription(self, PlaneText):
        Encription_key = random.randint(-25, 25)
        PlaneText_split = PlaneText.split()
        Encripted_string = ''
        for Word in PlaneText_split:
            Encripted_word = ''
            for Letr in Word:
                Letter_value = ord(Letr) + Encription_key
                if Letter_value > 90:
                    Letter_value -= 26
                elif Letter_value < 65:
                    Letter_value += 26
                Encripted_word += chr(Letter_value)
            Encripted_string += Encripted_word + ' '
        return Encripted_string, Encription_key
    def Decription(self, CipherText, Decription_key):
        if Decription_key == None:
            pass
        print 'Decription_key is', Decription_key
        CipherText_split = CipherText.split()
        Decripted_string = ''
        for Word in CipherText_split:
            Decripted_word = ''
            for Letr in Word:
                Letter_value = ord(Letr) - int(Decription_key)
                if Letter_value < 65:
                    Letter_value += 26
                elif Letter_value > 90:
                    Letter_value -= 26
                Decripted_word += chr(Letter_value)
            Decripted_string += Decripted_word + ' '
        return Decripted_string
while True:
    Caesar_cipher_obj = Caesar_cipher()
    Option = raw_input('For Encription: \'E\'\nFor Decription: \'D\'\nEnter your option: ').upper()
    if Option == 'E':
        PlaneText = raw_input('Enter your secret text: ').upper()
        CipherText, Key = Caesar_cipher_obj.Encription(PlaneText)
        print 'CipherText: ', CipherText, '\nEncription key:', Key
        print '='*50
    elif Option == 'D':
        CipherText = raw_input('Enter your cipher text: ').upper()
        Key = raw_input('Enter key: ')
        PlaneText = Caesar_cipher_obj.Decription(CipherText, Key)
        print PlaneText
        print '='*50
    else:
        print 'Error: Invalid option, Try again...'
        print '='*50