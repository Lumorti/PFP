# PFP
Pun Forrest, Pun!
A command line tool for generating puns from a certain word.

### Dependancies

None as far as I'm aware.

### Usage

After downloading the zip, extract into a folder and then run using the following in a terminal:
```bash
./pfp [word to make a pun from]
```

Extra command line options are available and are given by the command help using
```bash
./pfp -h
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
