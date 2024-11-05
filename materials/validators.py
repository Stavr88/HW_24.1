from rest_framework.serializers import ValidationError


class ValidatorLink():
    def __init__(self, field):
        self.field = field

    def __call__(self, video_url):
        # url = "youtube" #"http://youtube.com"
        url = [
            "youtube.com",
            "rutube.com"
        ]
        if video_url.get("video_url"):
            for v_u in url:
                if v_u not in video_url.get("video_url"):
                    raise ValidationError("Не верно указан сайт")
        return None

