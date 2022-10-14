import os
import iio
import numpy as np

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input0", type=str)
    parser.add_argument("input1", type=str)

    args = parser.parse_args()
    img = iio.read(args.input0)
    print(f"Image 0 shape is {img.shape}, dtype is {img.dtype}.")
