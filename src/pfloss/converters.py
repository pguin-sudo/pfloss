from abc import ABC, abstractmethod
import json
from pathlib import Path

from PIL import Image

with open(str(Path(__file__).parent.resolve() / "./colors.json"), "r") as f:
	COLORS = json.load(f)

class ConverterBase(ABC):
	self.color_scheme = "dmc"

	@abstractmethod
	def convert(self, img: Image.Image) -> Image.Image:
		...

	def get_colors(self) -> list:
		COLORS[self.color_scheme]

class DMCConverter(ConverterBase):
	self.color_scheme = "dmc"
	def convert(self, img: Image.Image) -> Image.Image:
		return img
