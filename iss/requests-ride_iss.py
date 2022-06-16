#!/usr/bin/python3
"""tracking the iss using
   api.open-notify.org/astros.json | Alta3 Research"""

# notice we no longer need to import urllib.request or json
import requests

## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    """reading json from api"""

    ## Call the webservice
    groundctrl = urllib.request.urlopen(MAJORTOM)
    # send a post with requests.post()
    # send a put with requests.put()
    # send a delete with requests.delete()
    # send a head with requests.head()
    helmet = groundctrl.read()
    ## strip the json off the 200 that was returned by our API
    ## translate the json into python lists and dictionaries
    helmetson = json.loads(helmet.decode("utf-8"))

    ## display our Pythonic data
    print("People in Space: " + str(helmetson["number"]))
    
    for astro in helmetson["people"]:

        print(astro["name"] + " on the " + astro["craft"])
if __name__ == "__main__":
    main()

