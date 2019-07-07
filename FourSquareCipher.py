# In this exercise, we want to implement the Four-Square Cipher encryption method.

# Start by reading the principle of the method on the Wikipedia web page to get some examples and to understand the main principles behind this method.

# Table generation

# The first thing to do is to write a function gen_table(key='') that takes a key (a sentence, a word) as parameter and that will return one encryption table, as described on the Wikipedia web page.

# For instance, if the key is keyword, then gen_table('keyword') should return :

# 1
# 2
# >>> gen_table('keyword')
# ['KEYWO', 'RDABC', 'FGHIJ', 'LMNPS', 'TUVXZ']
import string
def uniq(str):
    seen = set()
    return "".join(ch for ch in str if not(ch in seen or seen.add(ch)))

def clean(str):
    exclude = set(string.punctuation+string.whitespace+'Q')
    return "".join(ch for ch in str if not ch in exclude).upper()

def gen_table(str):
    alphabet = 'ABCDEFGHIJKLMNOPRSTUVWXYZ'
    str = clean(uniq(str))
    table = ['' for i in range(5)]
    for i in range(len(str)):
        table[i // 5] += str[i]
        alphabet = alphabet.replace(str[i], '')
    
    for i, ch in enumerate(alphabet, len(str)):
        table[i // 5] += ch
    return table
# The digraph function

# Then, write a function digraph(sentence) that returns a list (or an iterator) of the letter of sentence grouped two by two.

# If the number of letters is not even, then character X will be added at the end of the sentence.

# For instance you should have the following result :

# >>> digraph('Hello world')
# ['HE', 'LL', 'OW', 'OR', 'LD']
 
# >>> list(digraph('Hello world')) # if you choose to use an iterator
# ['HE', 'LL', 'OW', 'OR', 'LD']
 
# >>> list(digraph('house')) # odd number of letters, we add an X at the end
# ['HO', 'US', 'EX']
def digraph(str):
    str = clean(str)
    for i in range(0, len(str), 2):
        try:
            yield str[i] + str[i+1]
        except IndexError:
            yield str[i] + 'X'

def digraph_list(str):
    mylist = []
    for i in range(0, len(str), 2):
        try:
            mylist.append(str[i] + str[i+1])
        except IndexError:
            mylist.append(str[i] + 'X')
    return mylist
# Generators and Yield Function
# Generators are iterators, but you can only iterate over them once. It’s because they do not store all the values in memory, they generate the values on the fly:

# >>> mygenerator = (x*x for x in range(3))
# for i in mygenerator:
    # print(i)
# for j in mygenerator:
    # print("Hello") // will not print anything
# 0
# 1
# 4
# It is just the same except you used () instead of []. BUT, you can not perform for i in mygenerator a second time since generators can only be used once: they calculate 0, then forget about it and calculate 1, and end calculating 4, one by one.

# Yield
# Yield is a keyword that is used like return, except the function will return a generator.

# >>> def createGenerator():
# ...    mylist = range(3)
# ...    for i in mylist:
# ...        yield i*i
# ...
# >>> mygenerator = createGenerator() # create a generator
# >>> print(mygenerator) # mygenerator is an object!
# <generator object createGenerator at 0xb7555c34>
# >>> for i in mygenerator:
# ...     print(i)
# 0
# 1
# 4
# Now look at the digraph(), when I used yield inside a for loop, it keep on iterating and generating the values and then return the 2 letter substrings from the function. Pretty cool it is.

# Let’s encrypt !

# Now, using the gen_table(key) and the digraph(sentence) functions, we have to write an encrypt(message, keys)function.

# This function take two parameters, first the message to encrypt, then a 2-uplet containing the two keys used to generate the tables. You expect the following results :

# keys = ('alpha', 'beta')
# encrypt('hello world', keys)
# 'GTJKJZJUME'

def encrypt(sentence, keys):
    table_0 = gen_table(keys[0])
    table_1 = gen_table(keys[1])
    alphabet = 'ABCDEFGHIJKLMNOPRSTUVWXYZ'  # alphabet without Q
    sentence = clean_string(sentence)
    encrypted_sentence = ''
 
    for a, b in digraph(sentence):
        pos_a = alphabet.index(a)
        pos_b = alphabet.index(b)
 
        encrypted_sentence += table_0[pos_a // 5][pos_b % 5]
        encrypted_sentence += table_1[pos_b // 5][pos_a % 5]
    return encrypted_sentence
	
def decrypt(encrypted_sentence, keys):
    table_0 = gen_table(keys[0])
    table_1 = gen_table(keys[1])
    plain_table = gen_table()

    alphabet_0 = ''.join(table_0)
    alphabet_1 = ''.join(table_1)
    sentence = ''

    for a, b in digraph(encrypted_sentence):
        pos_a = alphabet_0.index(a)
        pos_b = alphabet_1.index(b)

        sentence += plain_table[pos_a // 5][pos_b % 5]
        sentence += plain_table[pos_b // 5][pos_a % 5]

    return sentence