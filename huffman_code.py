# cook your code here
###Huffman Compression and Decompression Code in Python 2.7
###By Mohammad Akram Sid.
from __future__ import division
import heapq
import re

###CREATE CLASS NODE
class Node:
    def __init__(self,char,left=None,right=None):
        self.char = char
        self.left = left
        self.right = right


###BUILD HUFFMAN TREE
def build_tree(frequencies):
    nodes = []
    for char,frequency in frequencies.items():
        heapq.heappush(nodes, (frequency, Node(char)))
    
    while len(nodes) > 1:
        f1, n1 = heapq.heappop(nodes)
        f2, n2 = heapq.heappop(nodes)
        node = Node('*',left=n1,right=n2)
        heapq.heappush(nodes, (f1+f2, node))

    root = nodes[0][1]

    return root

###ENCODING FUNCTION
def encode(root, string, mappings):
    if not root:
        return
    
    if not root.left and not root.right:
        mappings[root.char] = string

    encode(root.left, string+'0', mappings)
    encode(root.right, string+'1', mappings)

    return mappings


###GETTING KEY BY VALUE
def get_by_val(val,mappings):
    for key,value in mappings.items():
        if val == value:
            return key
    return '-1';


###DECODING FUNCTION
def decode(compressed_string, mappings):
    val = ''
    original_string = ''
    mutated_compressed_string = str(compressed_string[2:])
    
    for char in mutated_compressed_string:
        val = val+char

        if val in mappings.values():
            original_string = original_string + get_by_val(val,mappings)
            val = val.replace(val,'')
    
    return original_string

    

print "HUFFMAN COMPRESSION AND DECOMPRESSION PROGRAM"
print "BY MOHAMMAD AKRAM SID.\n***************************************\n\n"

uncompressed_string = raw_input("Please Enter String to be compressed : ")
uncompressed_string_len = len(uncompressed_string)

###Counting frequencies of each character

print "\n********************************\nCOMPRESSING FILE\n********************************\n"
frequencies = {}

for letter in uncompressed_string:
    if letter not in frequencies.keys():
        frequencies[letter] = uncompressed_string.count(letter);

# for char, freq in frequencies.items():
#     print(char,freq)

root = build_tree(frequencies)
mappings = {}
string = ''
mappings = encode(root,string,mappings)

# for char,code in mappings.items():
#     print(char,code)

bit_string = ''

for letter in uncompressed_string:
    bit_string = bit_string + mappings[letter]

# print bit_string

###converting binary string into bit equivalent using bin function and base=2
compressed_string = (bin(int(bit_string, base=2)))

# print compressed_string

uncompressed_string_size = uncompressed_string_len*7
compressed_string_len = len(compressed_string)
compressed_string_size = compressed_string_len-2

print "The original file was :\n",uncompressed_string,"\n\nThe size of uncompressed string was",uncompressed_string_size,"bits"
print "\nThe compressed file is :\n",compressed_string,"\n\nThe size of compressed string is",compressed_string_size,"bits"
print "\nThis is a saving of",uncompressed_string_size-compressed_string_size,""
print "The Compression Ratio is :", round(uncompressed_string_size/compressed_string_size,2),":1"


print "\n********************************\nDECOMPRESSING FILE\n********************************\n"

original_string = decode(compressed_string,mappings)
        
print "AFTER DECOMPRESSING THE STRING IS : \n",original_string,""