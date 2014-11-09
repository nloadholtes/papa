#
# a library for working with flickr.com as a data source
#
import flickrapi


class FlickrFetch():
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.flickr = flickrapi.FlickrAPI(api_key, api_secret)
        self.token, self.frob = self.flickr.get_token_part_one(perms='read')
        if not self.token:
            raise Exception('Please authorize this app first')
        self.flickr.get_token_part_two((self.token, self.frob))
