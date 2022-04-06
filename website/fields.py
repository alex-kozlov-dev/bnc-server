from rest_framework import serializers
from imagekit.cachefiles import ImageCacheFile


class ThumbnailField(serializers.ImageField):
    def __init__(self, spec, **kwargs):
        self.spec = spec
        super().__init__(**kwargs)

    def to_representation(self, original_image):
        if not original_image:
            return None

        cached = ImageCacheFile(self.spec(original_image))
        cached.generate()
        return super().to_representation(cached)
