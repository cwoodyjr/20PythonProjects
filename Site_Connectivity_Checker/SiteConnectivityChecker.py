# import urllib
# use urllib.request to retrieve data a from url
# write a function that takes in a url as a parameter
# check if url returns response

import urllib.request as urllib

def main(url):
    print("checking connection... ")
    
    response = urllib.urlopen(url)
    print("Succesfully Connected to ",url)
    print("the response code was ",response.getcode())
    
print("This is a site connectivity checker programme")
input_url = input("input URL to check: ")
secured = str("https://"+input_url)  #added this line as many users forget to add https://

main(secured)