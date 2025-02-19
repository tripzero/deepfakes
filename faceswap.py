#!/usr/bin/env python3
import sys
if  sys.version_info[0] < 3:
    raise Exception("This program requires at least python3.2")
if sys.version_info[0] == 3 and sys.version_info[1] < 2:
    raise Exception("This program requires at least python3.2")

from lib.utils import FullHelpArgumentParser

from scripts.extract import ExtractTrainingData
from scripts.train import TrainingProcessor
from scripts.convert import ConvertImage

from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

if __name__ == "__main__":
    parser = FullHelpArgumentParser()
    subparser = parser.add_subparsers()
    extract = ExtractTrainingData(
        subparser, "extract", "Extract the faces from a pictures.")
    train = TrainingProcessor(
        subparser, "train", "This command trains the model for the two faces A and B.")
    convert = ConvertImage(
        subparser, "convert", "Convert a source image to a new one with the face swapped.")
    arguments = parser.parse_args()
    arguments.func(arguments)
