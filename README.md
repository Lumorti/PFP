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

To view basic usage and the available flags use:
```bash
pfp --help
```
_For example:_

To run PFP to generate a maximum of 5 random puns from a word:
```bash
pfp -r -m 5 <word>
```

To run PFP to generate the complete ordered list of puns from a word:
```bash
pfp <word>
```

To run PFP to generate a single random pun from a word, with extra info about where the pun came from:
```bash
pfp -rl -m 1 <word>
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
