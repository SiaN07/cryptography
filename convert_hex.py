import base64

# hex to byte number
hex_str = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
bytes_str = bytes.fromhex(hex_str)
print(bytes_str)

# Byte data to hex
str = b'crypto{You_will_be_working_with_hex_strings_a_lot}'
new_hex = str.hex()

# Decode into bytes then encode into base64
hex_str2 = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
byte_str2 = bytes.fromhex(hex_str2)
print(byte_str2)

# # encode into base64
base_str2 = base64.b64encode(byte_str2)
print(base_str2)
