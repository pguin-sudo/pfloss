from pfloss import FlossArt, converters

img_paths = (
    # "tests/images/penis.png",
    # "tests/images/python.png",
    # "tests/images/serega.jpg",
    "tests/images/nastya.jpg",
    # "tests/images/jaba.jpg",
)

my_converters = (
    converters.DMCConverter(),
)

for img_path in img_paths:
    for color_converter in my_converters:
        test_art = FlossArt.from_path(
            img_path, color_converter
        ).resize(new_height=200)
        test_art.save()
