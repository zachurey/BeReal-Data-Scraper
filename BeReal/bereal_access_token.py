"""
    Declares BeRealAccessToken class
"""

from os import environ
from json import dumps
from dotenv import load_dotenv
from requests import post

class BeRealAccessToken:
    """
        Initiates a mock rest API call to retrieve a
        new access token from BeReal's token exchange
    """

    def __init__(self):
        load_dotenv()

        refresh_token = environ.get('refresh-token')

        # pylint: disable=line-too-long
        self.api_url = 'https://securetoken.googleapis.com/v1/token?key=AIzaSyDwjfEeparokD7sXPVQli9NsTuhT6fJ6iA'

        self.headers = {
            "Accept-Language": "en",
            "Content-Length": "273",
            "Accept": "*/*",
            "X-Firebase-Locale": "en",
            "X-Ios-Bundle-Identifier": "AlexisBarreyat.BeReal",
            "X-Firebase-Client": "apple-platform/ios apple-sdk/19F64 appstore/true deploy/cocoapods device/iPhone14, 2 fire-abt/8.15.0 fire-analytics/8.15.0 fire-auth/8.15.0 fire-db/8.15.0 fire-dl/8.15.0 fire-fcm/8.15.0 fire-fiam/8.15.0 fire-fst/8.15.0 fire-fun/8.15.0 fire-install/8.15.0 fire-ios/8.15.0 fire-perf/8.15.0 fire-rc/8.15.0 fire-str/8.15.0 firebase-crashlytics/8.15.0 os-version/15.5 xcode/13F17a",
            "X-Client-Version": "iOS/FirebaseSDK/8.15.0/FirebaseCore-iOS",
            "X-Firebase-GMPID": "1:405768487586:ios:28c4df089ca92b89",
            "Host": "securetoken.googleapis.com",
            "Connection": "keep-alive",
            "Accept-Encoding": "gzip, deflate, br",
            "X-Firebase-Client-Log-Type": "0",
            "User-Agent": "FirebaseAuth.iOS/8.15.0 AlexisBarreyat.BeReal/0.22.1 iPhone/15.5 hw/iPhone14_2",
            "Content-Type": "application/json"
        }

        self.body = {
            "grantType": "refresh_token",
            "refreshToken": refresh_token
        }

    def get_access_token(self):
        """
            Returns a new access token from BeReal
        """
        response = post(self.api_url, headers=self.headers, data=dumps(self.body))
        return response.json()['access_token']