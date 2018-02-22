# Author: Jordan Cameron Uehara
# Description:
# Accounts that are used for transfers only have expiring passwords that expire per CIS-CAT rules and
# rotating passwords will not always work in normal operations. Creating a method that will automatically
# check for certain users password expirations and change them to random strings generated via [some method].

# Change log
# Version 0.1 02/19/2018
# Initial release

# Generating a random string needs to be secure and include enough obfuctstation as possible.

import subprocess, random, itertools, string

openssl_rand = 8  # openssl psudeo random byte length, use above 8 but less than 48 this will increase your base4 password length
password_len = (openssl_rand/3)*4+4 # Length is calculated by Every 3 bytes increase by 4 chars length
master_len = 32 # Generate 32 sets of x length strings
random_array = []   # initiates array

for a in range(master_len):
    static_output = subprocess.check_output("openssl rand -base64 {0}" .format(openssl_rand), shell=True, stderr=subprocess.PIPE)
    random_array.append(static_output.rstrip()) # openssl likes to add newlines (\n) at the end of the base64 randoms

merged_array = [y for x in random_array for y in x] # merge the array into a single massive array[['313...'],['12331...']] into [['313...12331....']]
merged_string = ''.join(merged_array) # take the newly merged array and turn it into a string by joining them
start = random.randint(1,len(merged_string)-password_len)   # set the start value to something between the first char to the end (sanity checks that it wont be the exactly last char it leaves room set by password_len)
end = start + password_len  # end value is start + password length
initial_gen = merged_string[start:end]  # generate the string #TODO could remove the start,end vars and just do it in one line readability vs less lines

finish_gen = list(initial_gen)  # turn the string back into list #TODO might be a better way to do this without wasting time...
# Lets guarentee that a symbol/digit will be used
"""
Take this for example: we get a finish_gen string of "sanajsbsbASDssAgb", no numbers no symbols!
If we generate a random digit and symbol using python random.choice we can ensure every password can
pass whatever policy we decide to use on our machines.
TODO Will need to include a check to ensure that the string NEEDS one before hand. This currently always assumes a digit and
    symbol is needed it also (while a small chance) could overwrite a digit or symbol already lol
"""
random_symbol_pos = random.randint(0,len(finish_gen)-1)     # Use randint to generate a value between 0 (start of the array) and the end length
random_digit_pos = random.randint(0,len(finish_gen)-1)      # Ditto ^

# Check that you didn't just randomly picked the same numbers
while random_digit_pos == random_symbol_pos:
    random_digit_pos = random.randint(0,len(finish_gen)-1)
# Set the symbol and digit values
finish_gen[random_symbol_pos] = random.choice(string.punctuation)
finish_gen[random_digit_pos] = random.choice(string.digits)

# debugging until passwd intergration is completed DO NOT USE IN PROD
print "Initial Gen: {0}" .format(initial_gen)
print "Finish Gen:  {0}" .format(''.join(finish_gen))
