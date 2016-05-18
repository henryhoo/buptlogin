import requests
URL="http://10.3.8.211"
URLOUT="http://10.3.8.211/F.htm"
username='2012211009'
password='shangwoba'
payload = {'DDDDD':username, 'upass':password,'0MKKey':''}
def account():
    return (username+password)
def changeaccount(u,p):
    username=u
    password=p
def test():
    r = requests.get('http://zhihu.com')
    return r.url
def login():    
    if (test()=='http://10.3.8.211'):
        try:    
            r = requests.post(URL, data=payload)
            if (test()=='http://10.3.8.211'):
                return "log in fail"
            return "log in success"
        except HTTPError:
            print ('/nHTTPError')
            return 'HTTPError'
        except Timeout:
            print ('/nTimeout')
            return 'Timeout'
        except:
            print ('/nError')
            return 'Error'
    else:
        return "you have been login"
def logout():    
    if (test()=='http://www.zhihu.com/'):
        try:    
            r = requests.get(URLOUT)
            return "log out success"
        except HTTPError:
            print ('/nHTTPError')
            return 'HTTPError'
        except Timeout:
            print ('/nTimeout')
            return 'Timeout'
        except:
            print('/nError')
            return 'Error'
    else:

        return "you have been logout"
	
