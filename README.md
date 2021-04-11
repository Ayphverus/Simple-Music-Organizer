# Simple-Music-Organizer

**!!!THIS CODE WAS CREATED HASTILY, PLEASE MAKE A BACKUP BEFORE RUNNING!!!**

Organizes music (mp3 and flac) via metadata/ tags into:

```
MP3
└── Artist
    └── Album
        ├── music.mp3
        └── music.flac
```

Old files are kept, this program will clone files into a new MP3 directory.

## Disclaimer

This code has not been throughly tested, so please make a backup and look through the code before running it.  I am not responsible for your data loss or any unintended side effects.

## Setup

```
pip3 install tinytag
```

## Usage

Place the music_organizer.py along with Music in the same directory.

```
├── Music
│   ├── unorganizedmusic.mp3
│   └── disorganizedmusic.flac
└── music_organizer.py
```
Run

```
./music_organizer.py
```

Result should be as follows
```
├── Music
│   ├── unorganizedmusic.mp3
│   └── disorganizedmusic.flac
├── MP3
│   └── Artist
│       └── Album
│           ├── unorganizedmusic.mp3
│           └── disorganizedmusic.flac
└── music_organizer.py
```

## Thanks

Thanks to all those who made this possible with simple to use python packages.
