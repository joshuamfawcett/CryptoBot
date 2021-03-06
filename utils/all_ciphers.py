import base64 as b64
import string

alphabet = string.ascii_lowercase
alphabet_upper = alphabet.upper()


bacon_dict_complete = {'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB', 'E': 'AABAA', 'F': 'AABAB', 'G': 'AABBA', 'H': 'AABBB', 'I': 'ABAAA', 'J': 'ABAAB', 'K': 'ABABA', 'L': 'ABABB', 'M': 'ABBAA', 'N': 'ABBAB', 'O': 'ABBBA', 'P': 'ABBBB', 'Q': 'BAAAA', 'R': 'BAAAB', 'S': 'BAABA', 'T': 'BAABB', 'U': 'BABAA', 'V': 'BABAB', 'W': 'BABBA', 'X': 'BABBB', 'Y': 'BBAAA', 'Z': 'BBAAB'}


bacon_dict_standard = {'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB', 'E': 'AABAA', 'F': 'AABAB', 'G': 'AABBA', 'H': 'AABBB', 'I': 'ABAAA', 'J': 'ABAAA', 'K': 'ABAAB', 'L': 'ABABA', 'M': 'ABABB', 'N': 'ABBAA', 'O': 'ABBAB', 'P': 'ABBBA', 'Q': 'ABBBB', 'R': 'BAAAA', 'S': 'BAAAB', 'T': 'BAABA', 'U': 'BAABB', 'V': 'BAABB', 'W': 'BABAA', 'X': 'BABAB', 'Y': 'BABBA', 'Z': 'BABBB'}



tap_code_dict={'A':'. .' , 'B':'. ..', 'C':'. ...','K':'. ...', 'D':'. ....' , 'E':'. .....'
            ,'F':'.. .','G':'.. ..', 'H':'.. ...', 'I':'.. ....' , 'J':'.. .....'
            ,'L':'... .','M':'... ..', 'N':'... ...', 'O':'... ....' , 'P':'... .....'
            ,'Q':'.... .','R':'.... ..', 'S':'.... ...', 'T':'.... ....' , 'U':'.... .....'
            ,'V':'..... .','W':'..... ..', 'X':'..... ...', 'Y':'..... ....' , 'Z':'..... .....', ' ':'/ /'}


def base64(arg, mode):
  if mode == 'decode':
    padding_needed = len(arg) % 4
    if padding_needed:
      arg += '==='
    decrypt = b64.b64decode(arg).decode('utf-8')
    return decrypt

  elif mode == 'encode':
    message_bytes = arg.encode('ascii')
    base64_bytes = b64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message


def bacon_cipher(text, mode, variant):
    if mode == 'encode':
        if variant == 'complete':
            bacon_dict = bacon_dict_complete
        elif variant == 'standard':

            bacon_dict = bacon_dict_standard
        else:
            text = variant + ' ' + text
            bacon_dict = bacon_dict_standard

        text = text.upper()
        ciphertext = ''
        for char in text:
            try:
                ciphertext += bacon_dict[char] + ' '
            except:
                ciphertext += char + ' '

        return ciphertext
    elif mode == 'decode':
        if variant == 'complete':
            bacon_dict = bacon_dict_complete
        elif variant == 'standard':

            bacon_dict = bacon_dict_standard
        else:
            text = variant + ' ' + text
            bacon_dict = bacon_dict_standard

        text = text.split()
        bacon_dict = dict((v, k) for (k, v) in bacon_dict.items())  # See https://stackoverflow.com/a/50232911/14437456
        plaintext = ''
        for item in text:
            try:
                plaintext += bacon_dict[item]
            except:
                pass

        return plaintext


def tap_encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += tap_code_dict[letter.upper()] + ' '
        else:
            cipher += ' / '

    return cipher

def tap_decrypt(message):
    message = message.replace('/', ' / / ')
    message_pair = []
    i = 0
    while i < len(message.split()) - 1:
        temp_str = message.split()[i] + ' ' + message.split()[i + 1]
        message_pair.append(temp_str)
        i = i + 2
    decipher = ''
    for letter in message_pair:
        #decipher += \
        decipher = decipher + list(tap_code_dict.keys())[list(tap_code_dict.values()).index(letter)]
    return decipher


def tap(text):

	if len(text.split())==1:
		return tap_encrypt(text)
	else:
		try:
			return tap_decrypt(text)
		except:
			return tap_encrypt(text)

def a1z26(message):

	alphabets=list(string.ascii_lowercase)
	cont=message
	encrypt=''
	num_list=[]
	for i in cont[0:]:
		encrypt=encrypt  + str(i) + " "
		try:
			num_list.append(int(i))
		except:
			pass
	decrypt=''
	if cont[0].isalpha():
		for i in encrypt:
			try:
				z=i.lower()
				decrypt=decrypt+' '+str(alphabets.index(z)+1)
			except:
				decrypt=decrypt+str(i)
	else:
		for i in num_list:
			decrypt=decrypt + " " + str(alphabets[i-1])
	return decrypt

def null(string):
    res = ''
    string = string.split()

    for word in string:
      for x in range(len(word)):
        if word[x].isalpha(): res += word[x]; break

    return res