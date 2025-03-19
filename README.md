# Gnosis v2 Rulebook


## Makefile

`make dev` - runs a local server that live updates with any changes, this is what is used for normal development.

`make clean` - deletes the build directory.

`make build` - cleans and remakes the build directory.

`make publish` - Commits and pushes the whole project.  A few minutes later, github pages should update. 

## Scripts

`./make-wiki.py` - script to generate a player version of a tiddlywiki campaign source book.  If you aren't me you probably won't use this.

`./ppp.py`, `./levels.py` and `./heuristics.py` are all tools used to figure out the math of dice rolling.  Everything they do can be done by the gnosis-bot.  To use these properly require editing the source files.

