# PFP - Pun, Forrest, Pun!

A command line tool for generating puns from a certain word.

## Usage

To view basic usage and the available flags use:
```bash
pfp --help
```

To run PFP to generate the complete list of puns from a word, ordered by quality:
```bash
pfp <word>
```

To also show info about where each pun comes from:
```bash
pfp -l <word>
```

To generate a single random (but at least quality 2) pun from a word:
```bash
pfp -r -m 1 -t 2 <word>
```

## Installation

For easy access anywhere on your system it can be installed to /usr/local/share/pfp using the following:
```bash
sudo make install
```

To uninstall:
```bash
sudo make uninstall
```

## Adding more phrases

The phrases folder initially comes with several files containing many common idioms, movie quotes and various other recognisable phrases. To add your own simply add to these files or make another file in that directory.

Use hashes to state where the following phrases come from, as follows:

```
# <Movie 1 Title>
<Quote 1 from movie 1>
<Quote 2 from movie 1>

# <Movie 2 Title>
<Quote 1 from movie 1>
<Quote 2 from movie 1>

# English Idiom
<Some English idiom>

# <Song Name>
<Famous lyric from this song>
```
