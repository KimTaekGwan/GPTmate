from instagrapi import Client
from instagrapi.types import Usertag

from dotenv import load_dotenv
import os


class InstagramAPI:
    def __init__(self):
        self.client = Client()
        self.origin_tags = ['블로그', '개발자', '기획자', 'AI']
        self.setting()

    def __del__(self):
        self.client.logout()

    def setting(self):
        load_dotenv()
        self.client.login(os.getenv('META_ACCOUNT_USERNAME'),
                          os.getenv('META_ACCOUNT_PASSWORD'))

        # self.client.account_info()

    def set_caption(self, title, tags: list, detail=None):
        res = '[ ' + title + " ]\n"
        if detail:
            res += detail + "\n"
        res += "\n\n\nPlease check the profile link for details." + "\n"
        res += "@gwani_17 @gwani_portfolio" + "\n"
        for tag in tags + self.origin_tags:
            res += '#' + tag + ' '
        return res

    def post_photo(self, path_to_photo, caption):
        user = self.client.user_info_by_username('gwani_17')
        media = self.client.photo_upload(path=path_to_photo, caption=caption,
                                         usertags=[
                                             Usertag(user=user, x=0.5, y=0.5)],
                                         extra_data={"custom_accessibility_caption": "alt text example",
                                                     "like_and_view_counts_disabled": 0,
                                                     "disable_comments": 0})
        return media.dict()

    def post_story(self, path_to_photo, caption):
        self.client.story_upload(path_to_photo, caption=caption)


if __name__ == '__main__':
    insta = InstagramAPI()

    path_to_photo = 'data/230416.jpg'
    title = 'CH 001. why?'
    tags = ['why', '도전', '계획관리', '기록', '여유']

    caption = insta.set_caption(title, tags)
    # print(caption)
    insta.post_photo(path_to_photo, caption)
