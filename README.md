# ScreenLapse

A simple Python script for making a time-lapse screen capture in macOS.

## Usage

```text
usage: screen_lapse.py [-h] [-o OUTPUT_DIRECTORY] time_interval displays [displays ...]

positional arguments:
  time_interval         time interval (second) of each screenshot
  displays              ID of displays to capture

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_DIRECTORY, --output_directory OUTPUT_DIRECTORY
                        output directory for captured frames
```

For example, to make a time-lapse by capturing both primary and secondary display every 10 seconds,
you may use the following command.

```shell script
./screen_lapse.py 10 1 2
```

To stop, just send a `KeyboardInterrupt` (e.g. pressing `^C`).

To convert the frames into a video, you may consider using something like [FFmpeg](https://ffmpeg.org/).

For example, if you want to convert the frames into a 24-FPS video in MP4 format with default settings,
you may use the following command.

```shell script
ffmpeg -r 24 -i ${output_directory}/display_${display_ID}/%d.png -r 24 out.mp4
```

## License

[MIT](./LICENSE)
