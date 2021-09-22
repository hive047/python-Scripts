import whois
from validate_domains import is_registered

domain_name = "google.com"
if is_registered(domain_name):
    whois_info = whois.whois(domain_name)
    print("Domain registrar: ", whois_info.registrar)
    print("Whois server: ", whois_info.whois_server)
    print("Domain creation date: ", whois_info.creation_date)
    print("Expiration date: ", whois_info.expiration_date)
    print(whois_info)