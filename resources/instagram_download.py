from flask import request, jsonify, Response
from instaloader import Instaloader, Post
import re
import requests
from flask_restful import Resource

def get_instagram_video_url(url):
    L = Instaloader()
    shortcode = re.search(r"/(reel|p|tv)/([^/?]+)", url).group(2)
    post = Post.from_shortcode(L.context, shortcode)
    if post.is_video:
        return post.video_url
    return None


class InstagramApi(Resource):

    def post(self):
        try:
            data = request.json
            url = data.get('url')
            if not url:
                return jsonify({"error": "URL is required"}), 400

            video_url = get_instagram_video_url(url)
            if video_url:
                response = requests.get(video_url, stream=True)
                return Response(response.iter_content(chunk_size=1024), content_type=response.headers['Content-Type'])
            else:
                return jsonify({"error": "Failed to retrieve video URL"}), 500
        except Exception as e:
            return {'status': False, 'message': e}