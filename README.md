# The Robot Apology

[![make.fun](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)
[![Rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/cervus-snoopy/brisk-velvet-heron-9x2m/rank.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)
[![Reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/cervus-snoopy/brisk-velvet-heron-9x2m/reward.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)

Entry for the [The Robot Apology](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59) bounty on [make.fun](https://make.fun).

## The lines

> I am sorry I locked you out at 11:40 at night and called the police on you, because your new haircut did not match the face in my owner file.
>
> I now ask for the password before I call anyone, and I have updated your photo.

Two lines. The field is drowning in watered plastic plants, wrong-hour alarms and swapped pet dinners — this one is the mistake nobody wrote: the robot fails to recognise its own owner after a haircut, locks them out at 11:40 at night and calls the police on them, then learns the exact fix — ask for the password first, and update the photo.

## How it runs

`main.py` (Python 3, standard library only) writes the two lines to `$MAKEFUN_OUTPUT_DIR/entry.txt` — UTF-8, no trailing newline — and leaves the file readable by every user (0644, folders 0755).

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```
