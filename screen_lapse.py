#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import argparse
from pathlib import Path
import subprocess
import sys
import time
from typing import Sequence


def screen_elapse(displays: Sequence[int], time_interval: float, output_directory: Path) -> None:
    output_directory.mkdir()
    display_out_dirs = [output_directory / f'display_{display}' for display in displays]
    for out_dir in display_out_dirs:
        out_dir.mkdir()

    frame = 1
    while True:
        start_time = time.time()

        for display, out_dir in zip(displays, display_out_dirs):
            ret = subprocess.run(
                ['screencapture', '-Cx', '-D', str(display), out_dir / f'{frame}.png'],
                capture_output=True
            )
            stderr = ret.stderr.decode(encoding='utf-8')
            if len(stderr) > 0:
                print(stderr, file=sys.stderr)
                raise RuntimeError('screencapture exited but printed something to stderr')

        frame += 1
        time.sleep(time_interval - ((time.time() - start_time) % time_interval))


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-o', '--output_directory',
        help='output directory for captured frames',
        default=time.strftime('screen_lapse_%d_%b_%Y_%H_%M_%S')
    )
    parser.add_argument('time_interval', help='time interval (second) of each screenshot', type=float)
    parser.add_argument('displays', nargs='+', help='ID of displays to capture', type=int)
    return parser.parse_args()


if __name__ == '__main__':
    try:
        args = _parse_args()
        screen_elapse(args.displays, args.time_interval, Path(args.output_directory))
    except KeyboardInterrupt:
        print('\nKeyboardInterrupt received; exiting...')
        pass
