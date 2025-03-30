import requests
import logging
from base_plugin import EvidenceCollectionPlugin

BASE_URL = "https://dummyjson.com"
LOGIN_URL = f"{BASE_URL}/auth/login"
USER_DETAILS_URL = f"{BASE_URL}/auth/me"
POSTS_URL = f"{BASE_URL}/posts"
POST_COMMENTS_URL = POSTS_URL + "/{post_id}/comments"
# "Test: {} {}".format(123, 321)
# "Test: {0} {1}".format(123, 321)
# "Test: {a} {b}".format(a=123, b=321)

NUM_OF_POSTS = 60

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("logger")

class DummyJsonEvidenceCollectionPlugin(EvidenceCollectionPlugin):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.reset_details()

    def reset_details(self):
        self.token = None
        self.headers = {}

    def log_error(self, error):
        logger.error(f"Error: {error}") 

    def connectivity_test(self):
        body_json = {
            "username": self.username,
            "password": self.password
        }
        try:
            response = requests.post(url=LOGIN_URL, json=body_json)
            if response.status_code == 200:
                self.token = response.json().get("accessToken")
                self.headers["Authorization"] = f"Bearer {self.token}"
                logger.info("Connected successfully!")
                return True
            else:
                raise Exception(f"Failed to connect, received status code {response.status_code}")
        except Exception as e:
            self.log_error(e)
            self.reset_details()
            return False
    
    def collect_user_details(self):
        if not self.token:
            self.log_error("No token available. Cannot collect user details without authentication.")
            return None
        try:
            response = requests.get(url=USER_DETAILS_URL, headers=self.headers)
            if response.status_code == 200:
                logger.info("User deatils collected successfully.")
                return response.json()
            else:
                raise Exception(f"Failed to collect user details, received status code {response.status_code}")
        except Exception as e:
            self.log_error(e)
            return None
    
    def collect_posts(self, num_of_posts):
        if not self.token:
            logger.error("No token available. Cannot collect posts without authentication.")
            return None
        try:
            response = requests.get(url=POSTS_URL, headers=self.headers, params={"limit": num_of_posts})
            if response.status_code == 200:
                logger.info("Posts collected successfully.")
                return response.json()['posts']
            else:
                raise Exception(f"Failed to collect posts, received status code {response.status_code}")
        except Exception as e:
            self.log_error(e)
            return None
    
    def collect_post_with_comments(self, num_of_posts):
        if not self.token:
            self.log_error("No token available. Cannot collect posts with comments without authentication.")
            return None
        try:
            all_posts = self.collect_posts(num_of_posts)
            if all_posts is None:
                raise Exception("Failed to collect posts.")
            all_posts_with_comments = []
            for post in all_posts:
                post_id = post.get("id") # post_id = post["id"]
                response = requests.get(url=POST_COMMENTS_URL.format(post_id=post_id), headers=self.headers)
                if response.status_code == 200:
                    logger.info(f"Comments collected successfully for post {post_id}.")
                    comments = response.json()['comments']
                    post['comments'] = comments 
                    all_posts_with_comments.append(post)
                else:
                    raise Exception(f"Failed to collect comments for post {post_id}, received status code {response.status_code}")
        except Exception as e:
            self.log_error(e)
            return None
        return all_posts_with_comments
    
    def collect_evidence(self):
        if not self.token:
            self.log_error("No token available. Cannot collect data without authentication.")
            return None
        
        collected_evidences = {}
        collected_evidences["user_details"] = self.collect_user_details()
        collected_evidences["posts"] = self.collect_posts(NUM_OF_POSTS)
        collected_evidences["posts_with_comments"] = self.collect_post_with_comments(NUM_OF_POSTS)
        import ipdb; ipdb.set_trace()

        return collected_evidences