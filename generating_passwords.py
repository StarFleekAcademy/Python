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
a = False
while a == False:
    random_array = []
    for ini in range(32):
        static_output = subprocess.check_output("openssl rand -base64 12", shell=True, stderr=subprocess.PIPE)
        random_array.append(static_output.rstrip())
    merged_array = [y for x in random_array for y in x]
    merged_string = ''.join(merged_array)
    start = random.randint(1,len(merged_string)-20)
    end = start + 20
    initial_gen = merged_string[start:end]

    finish_gen = list(initial_gen)
    random_symbol_pos = random.randint(0,len(finish_gen)-1)
    random_digit_pos = random.randint(0,len(finish_gen)-1)
    while random_digit_pos == random_symbol_pos:
        random_digit_pos = random.randint(0,len(finish_gen)-1)
    finish_gen[random_symbol_pos] = random.choice(string.punctuation)
    finish_gen[random_digit_pos] = random.choice(string.digits)

    print "Initial Gen: {0}" .format(initial_gen)
    print "Finish Gen:  {0}" .format(''.join(finish_gen))
