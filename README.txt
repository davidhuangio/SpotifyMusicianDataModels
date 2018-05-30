David Huang
Revanth Amelia
Zan Javed


In order to run the scrape.py, please create an account with Spotify's Developer Platform and create
an application with any name. Set the redirect url to http://localhost and copy the client ID and secret.
Paste these into the util.prompt_for_user_token() to run the scraper.

If you get an error: "NoneType" object has no attribute 'split' , please modify your oauth2.py file like following:

1) Find the def _is_scope_subset(self,needle_scope,haystack_scope):
2) Add this if statement as the first line of the function:
      if needle_scope == None and haystack_scope == None:
         return True


         
The datasets in the zip are the collection of audio feature values from each track that we pulled along with the url reference to the track.