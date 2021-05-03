import pywhatkit

search = input("Search anything: ")

try:
    pywhatkit.search(search)
    print("results found")
    
except:
    print("unknown error")