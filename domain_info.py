#A script that takes in a target domain and uses the whois library to lookup the registration information of the domain

import whois

domain = input("Enter the domain name: ")
whois_info = whois.whois(domain)



#Extracting registrar information
print("Registrar: ", whois_info.registrar)
#Extracting the creation date
print("Creation date: ", whois_info.creation_date)
#Extracting the expiration date
print("Expiration date: ", whois_info.expiration_date)
#Extracting the nameservers information
print("Name Servers: ", whois_info.nameservers)