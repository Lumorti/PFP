# PFP
Pun, Forrest, Pun!

A command line tool for generating puns from a certain word.

### Installation on Linux

Download the zip of the source, extract into a folder and then install to the /usr/local/share/pfp directory by running the following in the extracted folder:
```bash
sudo make install
```

To uninstall use in either the extracted folder or in /usr/local/share/pfp:
```bash
sudo make uninstall
```

### Usage

To view basic usage and the available flags use:
```bash
pfp --help
```

To run PFP to generate the complete ordered list of puns from a word:
```bash
pfp <word>
```

To run PFP to generate a maximum of 5 random puns from a word:
```bash
pfp -r -m 5 <word>
```

To run PFP to generate a single random (but at least quality 2) pun from a word, with extra info about where the pun came from:
```bash
pfp -rl -m 1 -t 2 <word>
```

### Adding more phrases

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

### DISCLAIMER

I don't own or claim to own any of the quotes/names/phrases in the phrases folder, nor any words in the dictionaries. I make no money from this and all quotes have the name of their source along with them.
