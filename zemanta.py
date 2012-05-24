from pattern.web import URL,POST
import simplejson
"""
Other Zemanta Arguments
return_rdf_links    Possible values:0,1
sourcefeed_ids    ID for personalized related articles
More Here:http://developer.zemanta.com/docs/suggest/
"""

class ZemantaSuggest():
    
    """TODO: This should eventually return the finished post"""
    
    def __init__(self,api_key):
        self.api_key = api_key
        self._init_args()
        
    def _init_args(self):
        self.args = {'method': 'zemanta.suggest', \
                     'api_key': self.api_key}
        
    def make_call(self):
        self.args['return_categories'] = 'dmoz'
        self.args['format'] = 'json'
        try:
            raw_output = URL('http://api.zemanta.com/services/rest/0.0/'\
                             ,method=POST\
                             ,query=self.args).download()
            json = simplejson.loads(raw_output)
            self._init_args()
            return json
        except:
            return None

    def add_text(self, text):
        """Minimum required data for a call. Text of article submitting to Zemanta."""
        self.args['text'] = text
        
    def add_title(self, title):
        """Title of the text you are sending for better results"""
        self.args['text_title'] = title
        
    def add_required_keywords(self,keywords):
        """Terms to emphasize even when not in text. Terms must be in returned articles."""
        self.args['emphasis'] = keywords
        
    def set_article_count(self,count):
        """Default is 10"""
        self.args['articles_limit'] = count
        
    def set_article_max_age(self, days):
        """Max age of returned articles in days. Default is no limit"""
        self.args['articles_max_age_days'] = days
        
    def get_highlights(self):
        """Return a highlighted search snippet for each article."""
        self.args['articles_highlights'] = 1
    
if __name__ == "__main__":
    pass
