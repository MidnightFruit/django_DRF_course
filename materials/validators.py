from rest_framework import serializers


class YouTubeURLValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, data):
        data_url = dict(data).get(self.field)

        if data_url is not None and 'youtube.com' not in data_url:
            raise serializers.ValidationError("URL must link to YouTube!")
