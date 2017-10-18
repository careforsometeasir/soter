import os
import binascii 
import hashlib 
import json
import ast

users = {}

def salt(length):
    """Will generate a hexadecimal salt of length bytes"""
    byte = os.urandom(length)
    return binascii.hexlify(byte)

def hashify(password, salt):
    """Hashes the password using SHA512 with the salt"""
    return hashlib.sha512(password.encode('utf-8')+salt).hexdigest()

def newUser(username, password, length=16):
    """Adds a user and returns user list"""
    if username in users:
        return 3
    else:
        salty = salt(length)
        hashedPass = hashify(password, salty)
        users[username]={"password":hashedPass,"salt":salty.decode('utf-8')}
        return 5


def generateUser(username, password, length=16):
    """Generates a user"""
    salty = salt(16)
    hashedPass = hashify(password, salty)
    content = {username:{"password":hashedPass, "salt":salty.decode('utf-8')}}
    return content


def login(username, password, content=users):
    """Checks password for username in provided content"""
    if username in content:
        data = content[username]
        #print(data)
        retrievedPassword = data["password"]
        salty = data["salt"].encode('utf-8')
        newPassword = hashify(password, salty)
        #print(newPassword)
        if retrievedPassword == newPassword:
            #print("Success")
            return 1
        else:
            #print("Access Denied")
            return 2
    else:
        return 4

def load(filePath):
    """Loads JSON/Plaintext as dict"""
    file = open(filePath, "r")
    return ast.literal_eval(file.read())
    file.close()

def export(filePath, content=users):
    """Exports local database as JSON to specified file path"""
    file = open(filePath, "w")
    if isinstance(content, str) == True:
        file.write(content)
        return 5
    elif isinstance(content, dict) == True:
        file.write(json.dumps(content))
        return 5
    else:
        return 6
    
    file.close()

def codes():
    """Codes for Error and Success"""
    return {1:"Correct Password", 2:"Incorrect Password", 3:"User Already Exists", 4:"User Doesn't Exist", 5:"Success", 6:"Fail"}

