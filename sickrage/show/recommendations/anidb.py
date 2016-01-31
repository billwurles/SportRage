# coding=utf-8
import requests
from anidbhttp import anidbquery
from anidbhttp.query import QUERY_HOT
from sickbeard.common import try_int

from recommended import RecommendedShow

class AnidbPopular(object):
    def __init__(self):
        self.cache_subfolder = __name__.split('.')[-1] if '.' in __name__ else __name__
        self.session = requests.Session()

    def fetch_latest_hot_shows(self):
        """Get popular show information from IMDB"""

        shows = []
        result = []

        shows = anidbquery.query(QUERY_HOT)
        for show in shows:
            try:
                recommended_show = RecommendedShow(show.id, show.titles['x-jat'][0], 1, show.tvdbid, cache_subfolder=self.cache_subfolder, 
                     rating=str(show.ratings['temporary']['rating']), votes=str(try_int(show.ratings['temporary']['count'],0)), image_href=show.url)
                
                # Check cache or get and save image
                recommended_show.cache_image("http://img7.anidb.net/pics/anime/{0}".format(show.image_path))
                
                result.append(recommended_show)
            except:
                pass

        return result
        
anidb_popular = AnidbPopular()