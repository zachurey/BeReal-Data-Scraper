"""
    Declares BeRealAccessToken class
"""

from requests import get

class BeRealDiscoverUsers:
    """
        Initiates a mock rest API call to retrieve a
        new JSON object array from the Discover Users tab
    """

    def __init__(self, access_token):
        # pylint: disable=line-too-long
        self.api_url = 'https://mobile.bereal.com/api/feeds/discovery?limit=20'

        self.headers = {
            "Content-Type": "application/json",
            "Authorization": access_token,
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Host": "mobile.bereal.com",
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate",
            "User-Agent": "BeReal/7310 CFNetwork/1333.0.4 Darwin/21.5.0"
        }


    def get_discover_users_json(self):
        """
            Returns a JSON object of 20 users from the discover tab
        """
        response = get(self.api_url, headers=self.headers)
        return response.json()