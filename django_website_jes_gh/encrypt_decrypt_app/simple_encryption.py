#!/usr/bin/env python
# coding: utf-8

#     Hi! For this project, I was inspired by our assignment 2 where we worked with encryption and decryption. While I was doing that assignment, I couldn't help but think, "what if I continously added more and more ridiculous things to the encoder until it becomes an absolute beast and encrypts a message that is so impossible to decrypt, it would have even Alan Turing pulling his hair out?" Well I set out upon this goal, which, as the main focus was adding more and more things, I also changed the way I had the encryption actually work. Now I couldn't do an actual impossible encryption, as not only would that be too easy since you can just add a bunch of random.choice() everywhere, but also because I challenged myself to decrypt everything I encrypted. Now This wouldn't seem like a big deal, however, I made sure that the decryption only decrypted back, so I couldn't do something plain and simple like either connecting the decoder to the encoder allowing me to simply just take the inputed message back, or copying the encoded function to the decoder and have it loop through that as it figures out the original message. Now another thing i could have done is had both the encoder and decoder in the same class; this would've allowed me to simply retrieve the original message and paste it back, which would have been a lot easier. But No, I truly hated myself and did it the way shown in assignment 2, where you flip the message, reverse all the keys, then flip it back. This may sounds easy, but its not so easy when you have the encoder multiply to such huge numbers that it has to reset, and you have to find a way to find that reset point, but backwords, and where that point depends on numerous factors like message length and key values.
# 
#     Now enough about that, more importantly, I've made the encoder and decoder really simple to use by incorporating a chatbot. With this chatbot, you simply tell it if you want to encode or decode something, then input the message along with 3 unique numbers, which are the 3 keys you choose that will allow you to customize your encryption and have it be your very own! The chatbot is also built in a way that if it somehow fails, it will try again with new numbers you've inputed. This is because the range of unicode is only between 0 and 1114111. I know, only a million, how limiting can it get. If you attempt to use chr() outside of this range, it will produce an error. Since the encryption gets VERY large VERY fast, it is easy for numbers to exceed this limit, but I have put plenty counter-measures. Should anything go haywire there are try and except commands to allow you to continue. To get started, enter 'secret_messenger()' and then run it, and the chat bot will get started.
#     
#     What the chatbot actually does is it continuously loops through all my functions. It will first direct you to either an encoding function, where you will input a message and 3 keys, or the decoding function, which will ask you to copy and paste the encrypted message, as well as enter the 3 keys you've chosen. After the encoding function has all the inputs it needs, it will then utilize the Impossible class to encode this message, looping through many iterations to trult scramble the message. After this the encoding function, to make everything easier, will ask you if you want to immediately decode the function, rather than simply going all the way back and needing to input all the variables again. If you say yes it will utilize the MakeTheImpossiblePossible class to decode the message, which is faster because it stores the encrypted message and simply uses the variable rather than needing you to copy and paste. It also remembers the key values as they were inputed within the same function, so with all these it runs the decoder and returns your original message. Now for the decoder, It will start off by asking if you have an already encoded message along with its keys. If you respond no, it will redirect you to the encoder rather than restarting the whole loop and having you need to once again specify what you want to do. If you respond yes it will continue on normally. It first asks you to paste the encrypted message, then it will ask, one at a time, to input the 3 keys you used. After this it will run the MakeTheImpossiblePossible class and it will decode the entire message. Upon doing any of these options, it will loop, allowing you to coninue to encode and decode messages as you please, until you input exit/stop to leave the loop.
# 
# 

# In[18]:


#to get started, we need to import the random module introduced in our assignments.
#this is the only imported file that is needed

import random


#This is the class for encoding the actual message. All of the seperate encoders lead in to one another.
class Impossible():
    """this class takes 4 arguments, your message, start key, key increment, and your key increments increment.
    the message must be a string, while the remaining 3 arguments must be integers. This will take the message
    and convert it to a different string, which can only be converted back through a decoder.
    
    Parameters
    ----------
    message : string
        string that will become encoded.
    start_key : integer
        int that will change the value of the string.
    key_increment : integer
        int that will change the value of the start_key.
    key_increments_increment : integer
        int that will change the value of the key_increment.
        
    Returns
    -------
    encrypted : string
        string that is the modified version of the message string.
    """
    
    #this defines the arguments required for this class, they are set to None by default which will cause an error.
    #this is to make it more difficult to know how the encoder works forcing you to manually input variables.
    def __init__(the, message, start_key=None, key_increment=None, key_increments_increment=None):
        
        the.message = message
        the.start_key = start_key
        the.key_increment = key_increment
        the.key_increments_increment = key_increments_increment

    #This function starts the loop. It's purpose is to make a more convenient name for the encryption, encoder.
    def encoder(the):
        
        return the.scramble()

    #chnages message so that each even character is first, followed by the odd characters 
    def scramble(the):
        
        message = the.message
        scrambled = ''
        msg_len = len(message)
        
        #if the length of the message is even, this code will run
        if msg_len % 2 == 0:
            list1=[]
            list2=[]
            
            #converts string to list so we can iterate through it
            even = message[0::2]
            list1.append(even)
            
            odd = message[1::2]
            list2.append(odd)
            
            #converts list back to string
            for evens in list1:
                evens = str(evens)
                even_stevens = ''.join(evens)
            
            for odds in list2:
                odds = str(odds)
                odd_1s_out = ''.join(odds)
            
            #combines the two even and odd strings into a scrambled version of the original string
            scrambled = scrambled + even_stevens + odd_1s_out

            return the.cust_dict(scrambled)
       
        #if the message is odd, this will skip to the next function, making it harder to decrypt
        else:
            
            return the.cust_dict(message)
    
    #will manually replace vowels in the message into symbols
    def cust_dict(the,scrambled):
        
        message = scrambled
        and_sometimes_y = 'y'
        evil_dictionary = {'a':'$',
                           'e':'&', 
                           'i':'@', 
                           'o':'#', 
                           'u':'^', 
                           and_sometimes_y:'`'}
        
        for letter in message:
            
            for evil in evil_dictionary:
                new_evil = evil_dictionary[evil]
                
                #this will replace the letter with its corresponding dictionary value if it's in the message
                if evil in letter:
                    message = message.replace(letter, new_evil)
        
        return the.key_inc_multiplication(message)    

    #adds the key increment to the starting key,which is added to the message's unicode
    #it then multiplies the key increments increment to the key increment
    def key_inc_multiplication(the,encryption): 
        
        #multiple variable are assigned to one variable here because every variable will be changing.
        #this means we have to keep another variable as the original key for when the numbers get too big.
        message = encryption
        start_key = the.start_key
        key = the.start_key
        org_key_increment = the.key_increment
        key_increment = the.key_increment
        key_increments_increment = the.key_increments_increment
        encoded = ''
        
        for mes in message:
            code = ord(mes)
            code = code + key
            new_code = chr(code)
            encoded = encoded + new_code
            key = key + key_increment
            key_increment = key_increment * key_increments_increment
            
            #if the increment has surpassed 1114111, anything it adds won't work because its out of the unicode zone
            #this will have it convert back to the original key increment, then continue expanding again.
            if key_increment >= 1114111:
                key_increment = org_key_increment
            
            #if the key surpasses 1114111, the code will produce an error because the chr() wont be able to convert it.
            #this converts it back to the original starting key
            if key >= 1114111:
                key = start_key
        
        encrypted = encoded
        
        return the.add_key_inc(encrypted)
    
    #adds the key to the message's unicode, then adds the key increment to the key,
    #then adds the key increments increment to the key increment.
    def add_key_inc(the,new_message):
        
        #similar to the previous, multiple variable are assigned variables because every variable will be changing.
        #so we also have to keep another variable here as the original key for when the numbers get too big.
        message = new_message
        key_increment = the.key_increment
        key_increments_increment = the.key_increments_increment
        start_key = the.start_key
        key = start_key
        orig_key_increment = key_increment
        encoded = ''
        
        for mes in message:
            code = ord(mes)
            code = code + key
            new_code = chr(code)
            encoded = encoded + new_code
            key = key + key_increment
            key_increment = key_increment + key_increments_increment
            
            #converts key to original key once it has surpassed 1114111
            if key >= 1114111:
                key = start_key
            
            #converts key_increment back to the original increment once it surpasses 1114111
            if key_increment >= 1114111:
                key_increment = orig_key_increment
        
        encrypted = encoded
        
        #with certain numeric combination, at this point the message's unicode may already by too big.
        #in such a case, multiplying keys will make it much bigger, so this will skip the next part if error is raised.
        try:
            return the.key_multiplication(encrypted)
        
        except:
            return the.variable_encoder(encrypted)
    
    #adds the key to the message's unicode, then multplies the key increment to the key.
    def key_multiplication(the,different_message):
        
        encoded = ''
        message = different_message
        start_key = the.start_key
        key = start_key
        key_increment = the.key_increment
        
        for mes in message:
            code = ord(mes)
            code = code + key
            new_code = chr(code)
            encoded = encoded + new_code
            
            #key is now multiplied by the increment
            key = key * key_increment
            
            #reverts key to starting key if it has passed 1114111.
            if key >= 1114111:
                key = start_key
        
        return the.variable_encoder(encoded)
    
    #a basic encoder which adds the key increment to the key, but also adds a random assortment of letters to the message.
    #this then returns the new encoded message. 
    def variable_encoder(the,crypt):
        
        message = crypt
        key = the.start_key
        key_increment = the.key_increment
        
        #these are added because since we are adding, in case the keys add up to more than max value, it'll instead be
        #set to a default of 5, since otherwise it would produce an error.

        if (len(message) * key_increment) >= 1114111:
            key_increment = 5
        if (key + (len(message) * key_increment)) >= 1114111:
            key = 5
        if key is None:
            return("you didn't enter any keys:(")
       #this is a counter for the while loop to ensure it doesn't loop infinitely 
        while_attempts = 0
        
        while True:
            
            try:
        #to make sure no one tries decrypting from the front, i randomized the first 4 letters so that it would change the whole message if attempted this way.
        #I also made the fourth letter the precedes the actual message be closer to symbols for the message in case someone realizes that the first 3 #'s are ridiculously big, so it fits in with the message and they only remove the first 3.
        #some may say I may have went a little overboard, BUT NAY! I MUST DO EVERYTHING I CAN TO PROTECT MY PRECIOUS ENCRYPTION!!!
                
                random_letter1 = (((random.choice(range(0, 255))) * (random.choice(range(1, 255)))) - (random.choice(range(0, 100)))) + (random.choice(range(100, 200)))
                
                random_letter2 = ord(':')*random.choice(range(0, 19208))
                
                random_letter3 = ord(' ')*random.choice(range(0, 34815))
                
                #combines the letters and the smaller letter that is produced at the end.
                finishd = chr(random_letter1) + chr(random_letter2) + chr(random_letter3) + chr(random.choice(range(50,255)))
                
                encoded=''
                
                #these messages prevent hackers from thinking anything is even going on! the fools!
                banter=['nothing suspicious going on around here... ',
                        'urrp... wait... i think im gonna hurl... urr..blegh...: ',
                        "I promise you that the following symbols are not some weired encoded message. You're pretty paranoid you know that? "]
                
                #this loop was derived from the work we did on our second assignment.
                for mes in message:

                    code = ord(mes)
                    code = code + key
                    new_code = chr(code)
                    encoded = encoded + new_code
                    key = key + key_increment
                
                #adds a random string from string list, then combines it with the 4 random letters and the encoded message.
                encrypted = finishd + encoded
                
                return encrypted
            
            #should this encryption not work because of an error with the key/key increment, this will attempt it again.
            except:
                
                while_attempts = while_attempts + 1
                
                if while_attempts >= 2:
                    return 'uh-oh. something went wrong.'
                
                key = 5
                key_increment = 5
                print('uh-oh, something went wrong. I tried again with a new key and key increment; they are:                 key: 5 and key increment: 5.')
                continue
            
            #should this encryption not work because the unicode got way too high, this will break out of the loop.
            else:
                
                return('uh-oh, something went SUPER wrong.')
                
                break


# In[19]:


#this is the class for decoding the message returned from the encoder. it will reveres everything the encoder has done.
class MakeTheImpossiblePossible():
    """this class takes 4 arguments, your message, start key, key increment, and your key increments increment.
    the message must be a string, while the remaining 3 arguments must be integers. This will take the string from
    the encoder, along with the 3 keys used in the encryption, and return the original message inputted into the
    encoder.
    
    Parameters
    ----------
    message : string
        string that will become decoded.
    start_key : integer
        int that will change the value of the string.
    key_increment : integer
        int that will change the value of the start_key.
    key_increments_increment : integer
        int that will change the value of the key_increment.
        
    Returns
    -------
    encrypted : string
        string that is the modified version of the message string, and the original string entered into the encoder
    """
    
    #this defines the arguments required for this class, they are set to None by default which will cause an error.
    #this is to make it more difficult to know how the decoder works, forcing you to manually input variables.
    def __init__(the, message, start_key=None, key_increment=None, key_increments_increment=None):
        
        the.message = message
        the.start_key = start_key
        the.key_increment = key_increment
        the.key_increments_increment = key_increments_increment
    
    #this will remove the string inputed to deter hackers, as well as remove the 4 random symbols at the beginning.
    def decoder(the):
        
        banter = ['nothing suspicious going on around here... ',
                  'urrp... wait... i think im gonna hurl... urr..blegh...: ',
                  "I promise you that the following symbols are not some weired encoded message. You're pretty paranoid you know that? "]
        #in case the message doesn't somehow get inputted as a string, this will fix that.
        #this is required for the chatbot as it may directly link to this but the original message is not a string
        message = str(the.message)
        
        #removes the string from the banter list.
        for phrase in banter:
            message = message.replace(phrase, '')
        
        #removes the randomized 4 letters from the beginning
        true_message = message.replace(message[0:4], '')
       
        return the.true_decoder(true_message)
    
    #this begins reversing the encryption, it reverses the variable_encoder function.
    def true_decoder(the, true_message):
        
        mess = true_message
        start_key = the.start_key
        key_increment = the.key_increment
        
        #this is similar to the parameters of variable encoder, otherwise we would produce an error.
        if (len(mess) * key_increment) >= 1114111:
            key_increment = 5
        if (start_key + (len(mess) * key_increment)) >= 1114111:
            start_key = 5
        
        #ensures the while loop doesn't continue to loop until the planets been destroyed
        count = 0
        
        #this will return a message in case the decryption fails for any reason.
        while True:
            
            try:
                
                #this will give us the last key that was used in the encoder so that we may use it in reverse.
                key = start_key + (len(mess) * key_increment)
                decoded = ''
                
                #loops through the message in reverse
                for char in mess[::-1]:
                    
                    #key is subtracted first because in the encoder it was added after the key.
                    #so since this is reversed, we subtract first before we use the key.
                    key = key - key_increment
                    orig_ord = ord(char) - key
                    orig_chr = chr(orig_ord)
                    decoded = decoded + orig_chr
                
                #this will flip the message back around to its original placement
                multiplied_msg = decoded[::-1]
                
                #just as the encoder may skip the multiplication process, so doeas 
                try:
                    
                    return the.key_unmultiplication(multiplied_msg)
                
                except:
                    
                    return the.un_add_key_inc(multiplied_msg)
            
            #in case the keys don't work, this will convert them to 5
            except:
                
                count = count + 1
                
                if count >= 2:
                    return 'uh-oh. something went wrong.'
                
                start_key = 5
                key_increment = 5
                continue
            
            #this will break out of the loop if everything fails
            else:
                
                print("whoops, I couldn't decode this message.")
                break

    #this reverses the key_multiplication function of the encoder.
    def key_unmultiplication(the, multiplied_message):
       
        encoded = multiplied_message
        key_increment = the.key_increment
        start_key = the.start_key
        key = start_key
        max_key = key
        #big_key is assigned to false by default so we can continuously update the max_key.
        big_key = False
        counter = 0
        
        #this while loop will figure out what the starting key was, as well as the maximum value the key can hold.
        #this is because the key will default to this max value whenever its range is out of unicode range.
        while counter < len(encoded) - 1:
            
            key = key * key_increment
            counter = counter + 1
            
            #if the big_key is false that means that the key is never out of the unicode range.
            #so the max_key is whatever the last iteration of the loops is.
            if big_key == False:
                max_key = key
            
            #if the key exceeds unicode range, then that means it must have looped in the encryption,
            #so this will tell us what the maximum value of the key is at that moment, as it can go no higher,
            #and it will prevent further changes to the max key because of this by having big key equal true.
            if key >= 1114111:
                max_key = key
                key = start_key
                big_key = True
        
        #this is the original key that the encoder last used
        new_key = key
        decoded = ''
        
        for char in encoded[::-1]:
            code = int(ord(char))
            new_code = int(code - key)
            
            #we divide here because the keys were multiplied in the encoder
            key = int(key / key_increment)
            
            #once the key is smaller than the starting key, it means that the encoder has looped,
            #so to decode, we must set the key back to the maximum value.
            if key < start_key:
                key = int(max_key / key_increment)
            
            orig_chr = chr(new_code)
            decoded = decoded + orig_chr
        
        added_message = decoded[::-1]
        
        return the.un_add_key_inc(added_message)
    
    #this will subtract the additions to the key and key increment in the add_key_inc part of the encryption
    def un_add_key_inc(the, added_message):
        
        message = added_message
        start_key = the.start_key
        key_increment = the.key_increment
        key_increments_increment = the.key_increments_increment
        orig_key = start_key
        orig_key_increment = key_increment
        
        #this is a placeholder for the key increment in case the increment was very small.
        key_inc = key_increment + (len(message) * key_increments_increment)
        
        #we will assign key value pairs to a list of tuples in the while loop
        keychain = []
        
        #allows the max key and max inc to continuously update given they are small values
        big_key = False
        big_inc = False
        max_key = start_key
        counter = 0
        
        while counter < len(message):
            start_key = start_key + key_increment
            key_increment = key_increment + key_increments_increment
            counter = counter + 1
            
            #allows max key and max inc to continuously update given they are small values
            if big_key == False:
                max_key = start_key
            
            if big_inc == False:
                max_inc = key_increment
                
            #if the starting key has exceed the unicode range, then that means the original encryption has looped
            if start_key >= 1114111:
                max_key = start_key
                start_key = orig_key
                
                #we'll need both the key increment at this time, as well as the key,
                #this is because the increment is continously changing, meaning that the increment for a key will always be unique
                max_keys_key_increment = (key_increment - key_increments_increment)
                
                #makes a tuple out of max_key and max keys key increment
                maximum_keychain = (max_key, max_keys_key_increment)
                
                #this makes a list out of every instance of max_key and keys increment in case it loops multiple times
                keychain.append(maximum_keychain)
                big_key = True
            
            #the maximum key increment is reached once it exceeds 1114111 so it is stored in a variable, reverted back, then looped
            if key_increment >= 1114111:
                max_inc = key_increment
                key_increment = orig_key_increment
                big_inc = True
        
        key = start_key
        key_inc = key_increment
        
        #this reverses the list since we will be decoding backwords
        if big_key == True:
            keychain = keychain[::-1]
        
        decoded = ''
        
        #this allows us to determine which point in looping we are in order to assign that specific max key and max_inc to the key.
        key_inc_counter = 0
        
        for char in message[::-1]:
            key_inc = key_inc - key_increments_increment
            key = key - key_inc
            
            #if the key is smaller than the original key, that means the encryption has looped, so we revert back.
            if key < orig_key:
                #this assigns a variable which represent the current iteration of the encryption loop,
                #meaning the time when the encoder reached a maximum value and reset
                key_list = key_inc_counter
                key_inc_counter = key_inc_counter + 1
                
                #we subtract the max key and the increment at the time of it from each other
                #we figure out which to use based on the counter, it tells us which iteration we are currently on
                key = keychain[key_list][0] - keychain[key_list][1]
            
            #if the key increments becomes smaller than the starting key increment, the encoder has looped,
            #so to decode, we must set the key increment back to the maximum value, as well as the key
            if key_inc < orig_key_increment:
                key_inc = max_inc - key_increments_increment
                
                #the key here must be reset because if the increment is big, than so to is the key since it is added to the key
                key = start_key + key_inc

            orig_ord = ord(char) - key
            orig_chr = chr(orig_ord)
            decoded = decoded + orig_chr

        inc_multiplied_msg = decoded[::-1]
        
        return the.key_inc_unmultiplication(inc_multiplied_msg)
    
    #This will undo the increment multiplication process done in the key_inc_multiplication portion of the encoder.
    def key_inc_unmultiplication(the, inc_multiplied_msg):
        
        message = inc_multiplied_msg
        key1 = the.start_key
        start_key = key1
        org_key_increment = the.key_increment
        key_increment = the.key_increment
        key_increments_increment = the.key_increments_increment
        counter = 0
        max_key = start_key
        max_inc = key_increment
        
        #we first need to determine the values of the starting key, and its increment.
        #then we need to find the maximum values they reach
        #if the length is less then 2, the encryption works in an odd way, so we'll use else for that and focus on 2+
        if len(message) >= 2:
            
            #if the counter reaches the excat length of the message, the values would be too big, so we use -1
            while counter < len(message) - 1:
                start_key = start_key + key_increment
                key_increment = key_increment * key_increments_increment
                counter = counter + 1
                
                #this continuously updates max_inc so long as it is smaller than the current key_increment
                if max_inc < key_increment:
                    max_inc = int(key_increment / key_increments_increment)
                
                #this continuously updates max_key so long as it is smaller than the current key
                if max_key < start_key:
                    max_key = start_key

                #replaces the key with default value if exceeds unicode range, then stores max value of it
                if start_key >= 1114111:
                    max_key = start_key
                    start_key = key1
                
                #replaces the key incrementvwith default value if exceeds unicode range.
                if key_increment >= 1114111:
                    key_increment = org_key_increment
        
        elif len(message) == 1:
            
            while counter < 1:
                start_key = start_key
                key_increment = key_increment * key_increments_increment
                counter = counter + 1
                
                #since the string only has 1 character, the max_key and max_inc will be the first iteration of the loop.
                max_key = start_key
                max_inc = int(key_increment / key_increments_increment)
                
                #in case of the keys exceeding unicode range, this sets their max values as that key value and resets the key
                if start_key >= 1114111:
                    max_key = start_key
                    start_key = key1
                    key_increment = org_key_increment
                #in case of the key increment exceeding unicode range,
                #this sets its max value as that key value and resets the increment
                if key_increment >= 1114111:
                    max_inc = int(key_increment / key_increments_increment)
                    max_key = start_key
                    start_key = key1
                    key_increment = org_key_increment
        
        #if the length is zero this will return a message saying to enter something
        else:
            
            return('please enter a message')
        
        key_inc = key_increment
        
        #this represents the custom length that each key increment will have, in other words, sets the lowest and highest value the key increment can go
        org_key_inc = range(org_key_increment, max_inc)
        key = start_key
        
        #this represents the custom length that each key will have, in other words, sets the lowest and highest value the key can go
        starter_key = range(key1, max_key)
        decoded = ''
        
        for char in message[::-1]:
            orig_ord = ord(char) - key
            orig_chr = chr(orig_ord)
            decoded = decoded + orig_chr
            key_inc = int(key_inc / key_increments_increment)
            key = key - key_inc
            
            #if the key increment either exceeds the max_value, or is lower than its lowest value, this will reset the values
            if key_inc not in org_key_inc:
                add_inc = key_inc
                key_inc = max_inc
                
                #in case the starter key is still in its range, we will need to reset it.
                #this must be a conditional because there is a different method to change the key if its not int range.
                if key in starter_key:
                    key = int((key + add_inc) - key_inc)
            
            #if the key either exceeds the max_value, or is lower than its lowest value, this will reset the values
            if key not in starter_key:
                key = int(max_key - max_inc)
                
                #resets the key increment if its in its range
                if key_inc in org_key_inc:
                    key_inc = max_inc
        
        convert_message = decoded[::-1]
        
        return the.undo_cust_dict(convert_message)
     
    #this reverts the letters the custom dictionary in the encryption changed back to the original letters.   
    def undo_cust_dict(the, convert_message):
        
        message = convert_message
        and_sometimes_y = 'y'
        evil_dictionary = {'a':'$',
                           'e':'&',
                           'i':'@',
                           'o':'#',
                           'u':'^',
                           and_sometimes_y:'`'}
        
        #we first must loop through the message in order to assign each letter as a variable
        for letter in message:
            
            #now we loop through the dict to get a variable assigned to each key and value
            for evil in evil_dictionary:
                new_evil = evil_dictionary[evil]
                
                #this will replace the modifications the custom dictionary applied to the original string,
                #and return it by replacing these symbols with the original letters
                if new_evil in letter:
                    message = message.replace(letter, evil)
        
        scrambled_message = message
        
        return the.unscramble(scrambled_message)
    
    #this will undo the even and odd string categorization the scramble function in the encoder did.
    def unscramble(the, scrambled_message):
        
        final_message = scrambled_message
        unscrambled = ''
        msg_len = len(final_message)
        
        #this will allow the function to carry out if the length of the string is even
        if msg_len % 2 == 0:
            half = msg_len / 2
            list1 = []
            list2 = []
            
            for letters in final_message:
                #this separates the first half of the message and the second into 2 different lists
                #this is because the encryption ordered the even strings on the first half, then the odd pairs.
                if len(list1) < half:
                    list1.append(letters)
                
                elif len(list1) == half:
                    list2.append(letters)
            
            #using the zip function, this reverts the string back to the original form by placing the even,
            #then the odd string variables one at a time, until out original message is assembled.
            for even, odd in zip(list1, list2):
                even = str(even)
                odd = str(odd)
                combine = [even,odd]
                
                #this converts the list back into a string
                orig_msg = ''.join(combine)
                unscrambled = unscrambled + orig_msg
            
            #this will return the original message types into the encryption.
            return unscrambled
        
        #this will return the original message in case the length of the string was odd,
        #because the encryption only occured if the length was even.
        else:
            
            return final_message


# In[20]:



def encoding_time(msg,start_key,key_increment,key_increments_increment):
    
    """The secret messenger will lead you to this function if you have chosen to encode a message. It will take
    any message you input, then you will need to enter 3 different keys into it. Ensure the keys are no bigger than
    1113111 and no smaller than 1.
    
    Parameters
    ----------
    There are NO PARAMETERS--this is because you will input these your self as you go along the function.
    
    Return
    ------
    This will return an encoded version of the message you originally inputted, along with the 3 keys used so they
    not forgotten."""
    
    #bot will loop through these at random as its encoding the message.
    talk = ['alright getting your message ready...',
          "ok,that's an interesting message...",
          "don't worry, I won't tell anyone..."]
    
    #sets a variable to be equal to a slightly more limited unicode range.
    num_limit = range(1,1113111)
    
    #stores inputed message
    #msg = input('Please type in the message you want encoded: ')
    
    #stores inputed key
    #start_key = int(input('Please type in your secret key, this must be a positive number: '))
    
    #loops until user input key that is in range of num_limit
    while start_key not in num_limit:
        
        #notifies user value is too big
        if start_key >= 1114111:
            return 'WOAH! That is a huge number, can you please try again with a smaller number?'
        #notifies user value is too small
        if start_key <= 0:
            return 'Please no negative numbers, this includes 0, please try again with a bigger number.'
    
    #stores the variable for later use on the function
    key1 = start_key    
    
    #stores inputed key increment
    #key_increment = int(input('Please type in another number, your key increment, which will affect your secret key: '))
    
    #loops until user input key increment that is in range of num_limit
    while key_increment not in num_limit:
        
        #notifies user value is too big
        if key_increment >= 1114111:
            return 'WOAH! That is a huge number, can you please try again with a smaller number?'
        
        #notifies user value is too small
        if key_increment <= 0:
            return 'Please no negative numbers, this includes 0, please try again with a bigger number.'
    
    #stores the variable for later use on the function
    key2 = key_increment    
    
    #stores inputed key increments increment
    #key_increments_increment = int(input('Please type in one last number, your key increment changer, which will affect the previous number, affecting your secret key. keyception!: '))
    
    #loops until user input key increments increment that is in range of num_limit
    while key_increments_increment not in num_limit:
        
        #notifies user value is too big
        if key_increments_increment >= 1114111:
            return 'WOAH! That is a huge number, can you please try again with a smaller number?'
        #notifies user value is too small
        if key_increments_increment <= 0:
            return 'Please no negative numbers, this includes 0, please try again with a bigger number.'
    
    #stores the variable for later use on the function
    key3 = key_increments_increment    
    
    #sets up the parameters of the Impossible class
    enc = Impossible(msg, start_key, key_increment, key_increments_increment)
    
    #attempts to encode the message
    try:
        
        encoded_msg = enc.encoder()
        
        #this will return the keys along with the code so that the user can immediately transition to decoding.
        return ([encoded_msg, key1, key2, key3])
    
    #resets the loop if encoding fails
    except:
        
        return'Sorry! It looks like something went wrong, please try again from the beginning. '
    
    
def decoding_time(msg,key1,key2,key3):
    
    """The secret messenger will lead into this function if you have entered decode, but you must already have an
    encoded message along with all 3 of it's keys.
    
    Parameters
    ----------
    There are NO PARAMETERS--this is because you will choose them inside this function
    
    Return
    ------
    This will return the original message that was encoded"""
    
    #takes the input of the encoded message
    msg_to_dec = msg
    
    
    #sets up the parameters of the MakeTheImpossiblePossible class
    decoding = MakeTheImpossiblePossible(msg_to_dec, key1, key2, key3)
    
    #will attempt to decode the message
    try:
        
        decoded_msg = decoding.decoder()
        
        #print(decoded_msg)
        return decoded_msg
    
    #if decoding fails, resets the loop after notifying user
    except:
        
        return "uh-oh, the decoding didn't go very well, sorry! please try encoding another message and i'll try to decode it!"
