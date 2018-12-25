# PFP
Pun, Forrest, Pun!

A command line tool for generating puns from a certain word.

### Installation

After downloading the zip, extract into a folder and then install to the /usr/share/ directory by running:
```bash
sudo make install
```

To uninstall use:
```bash
sudo make uninstall
```

### Usage

To run PFP to generate a normal list of puns from a word:
```bash
pfp <word>
```

There are many command flags to control the output. To view the available options use:
```bash
pfp --help
```

### Adding more phrases

The phrases folder initially comes with several files containing many common English idioms, movies quotes and various other recognisable phrases. To add your own simply add to these files or make another file in that directory.

Use hashes to state where the following phrases should come from, as follows:

```
# <Movie 1 Title>
<Quote from movie 1>
<Different quote from movie 1>

# <Movie 2 Title>
<Quote from movie 2>
<Different quote from movie 2>

# English Idiom
<Some English idiom>

# <Song Name>
<Famous lyric from this song>
```
