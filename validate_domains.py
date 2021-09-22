import whois

def is_registered(domain_name):
    try:
        w = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(w.domain_name)

if __name__ == '__main__':
    domains = [
        "thepythoncode.com",
        "google.com",
        "github.com",
        "unknownrandom.com",
        "clearlynotregistered.co"
    ]

for domain in domains:
    print(domain, "is registered" if is_registered(domain) else "is not registered")