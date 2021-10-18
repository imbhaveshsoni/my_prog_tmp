def AptExtractHostName(url,port=False,protocol=False):

    #find & remove protocol (http, ftp, etc.) and get hostname

    if(protocol != True):
        if '//' in url:
            hostname = url.split('/')[2]
        else:
            hostname = url.split('/')[0]
    else:
        if '//' in url:
            hostname = url.split('/')[0]+'//'+url.split('/')[2]
        else:
            hostname = url.split('/')[0]

    #find & remove port numbe   r
    if(port != True):
        hostname = hostname.split(':')[0]
    
    #find & remove "?"
    hostname = hostname.split('?')[0]

    return hostname

###### How to use    #######
#print(AptextractHostname('http://127.0.0.1:8000/Media/',True,True))