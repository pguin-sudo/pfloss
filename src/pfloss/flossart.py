from typing import Type, TypeVar

from PIL import Image

from pfloss import converters

T = TypeVar("T", bound="FlossArt")


class FlossArt:
    name: str
    img: Image.Image
    converter: converters.ConverterBase

    def __init__(
        self,
        name: str,
        img: Image.Image,
        converter: converters.ConverterBase,
    ):
        self.name = name
        self.img = img
        self.converter = converter

    @classmethod
    def from_path(
        cls: Type[T],
        path: str = "image.jpg",
        converter: converters.ConverterBase = converters.DMCConverter(),
    ) -> T:
        try:
            img = Image.open(path)
        except:
            print(path, "Unable to find image ")
            raise

        return cls(".".join(path.split(".")[:-1]), img, converter)

    def resize(
        self, new_width: int = 0, new_height: int = 0, ratio_multiplier: float = 1
    ):
        width, height = self.img.size
        aspect_ratio = height / width
        if not new_height and not new_width:
            return self
        elif new_height and not new_width:
            new_width = int(new_height / aspect_ratio / ratio_multiplier)
        elif new_width and not new_height:
            new_height = int(new_width * aspect_ratio * ratio_multiplier)

        self.img = self.img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        return self

    def save(self):
        img = self.converter.convert(self.img)
        img.save(f"{self.name}-result.png", "PNG")
