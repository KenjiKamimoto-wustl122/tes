import urllib
from urllib.request import URLError

def check_web_site_status(url, print_detail=False):
    try:
        response = urllib.request.urlopen(url)
        code = response.getcode()
        if print_detail:
            print('url:', response.geturl())
            print('code:', code)
            print('Content-Type:', response.info()['Content-Type'])
            content = response.read()
            print(content)
        response.close()
        return True, f"OK, code: {code}"
    
    except URLError as e:
        return False, "URL error"
    
    except:
        return False, "Unknown error"
    
    
def main():
    status, comment = check_web_site_status(url="https://celloracle.org/", print_detail=False)
    print(comment)
    assert(status)
    
if __name__ == "__main__":
    main()