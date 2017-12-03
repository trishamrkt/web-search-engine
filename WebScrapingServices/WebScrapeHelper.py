import socket;
import httplib
from urlparse import urlparse
import requests

# Check if numbers are in word
def numbers_in_word(word):
    if ('0' in word or '1' in word or '2' in word or '3' in word or '4' in word or '5' in word \
        or '6' in word or '7' in word or '8' in word or '9' in word) and ('f' in word or 'e' in word \
        or 'u' in word):
        return True;
    else:
        return False;
    
def is_valid_word(word):
     if (';' not in word) and ('&' not in word) and ('<' not in word) and ('>' not in word) \
        and ('-' not in word) and ('(' not in word) and (')' not in word) and ('_' not in word) \
        and ('\\' not in word) and ('/' not in word) and ('}' not in word) and ('{' not in word) \
        and ('=' not in word) and ('$' not in word) and ('meta' not in word) \
        and ('charset' not in word) and ('script' not in word) and ('#' not in word) and ('=' not in word) \
        and ('|' not in word) and not numbers_in_word(word):
         return True;
     else:
         return False; 

def is_ascii_encoded(word):
    try:
        word.decode('ascii');
    except (UnicodeEncodeError, UnicodeDecodeError) as e:
        return False;
    else:
        return True;

def polish_image_url(imageurl, url):
    print '\n';
    print '--------------------------------';
    print 'Polishing URL for: ' + imageurl;
    
    # Add website url to image url if need be
    if not is_dns_valid(imageurl):
        root_domain = get_root_domain(url);
        if imageurl[0] != '/':
            imageurl = root_domain + '/' + imageurl;
        else:
            imageurl = root_domain + imageurl;
        
    # Make sure there is an image there
    if is_image(imageurl):
        print 'adding url to result set'
        return imageurl;
    else:
        print 'SOMETHING WRONGGGG'
        return None;

def is_dns_valid(url):
    new_url = concat_https(url);
    print 'Trying: ' + new_url;
    try:
        r = requests.get(new_url, timeout=0.05)
        if r.status_code < 400:
            print 'Valid url!'
            return True;
        else:
            return False
    except requests.exceptions.MissingSchema:
        print 'Missing Schema Exception!'
        return False
    except requests.exceptions.Timeout:
        print 'Url has timed out: ' + str(0.1);
        return False;
    except requests.exceptions.ConnectionError:
        print 'Error: Connection Error'
        return False;
    except requests.exceptions.InvalidURL:
        print 'Invalid Url Exception'
        return False
    
def is_image(imageurl):
    if is_dns_valid(imageurl) and ('.jpg' in imageurl or '.gif' in imageurl or '.png' in imageurl or '.jpeg' in imageurl):
        return True;
    else:
        return False;
    
def get_root_domain(url):
    return concat_https(urlparse(url).hostname);

def concat_https(url):
    if not ('http://' in url or 'https://' in url ) and '//' not in url[0:10]:
        url = 'http://' + url;
    elif '//' in url[0:2] and ('http://' not in url or 'https://' not in url):
        url = 'http:' + url;
    return url;

