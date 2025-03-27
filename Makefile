# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
ROOT_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = $(ROOT_DIR)docs/source/
BUILDDIR      = $(ROOT_DIR)docs/build/
HTMLDIR	      = $(BUILDDIR)html

GM_BOOK       = "https://nephlm.github.io/tw/gods-reborn.html"
PLAYER_BOOK   = $(SOURCEDIR)_static/html/gods-reborn.html


# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

build:
	make clean
	sphinx-build $(SOURCEDIR) $(HTMLDIR)

dev:
	make clean
	sphinx-autobuild $(SOURCEDIR) $(HTMLDIR)


clean:
	rm -rf $(BUILDDIR)

player-book:
	python $(ROOT_DIR)make-wiki.py $(GM_BOOK) $(PLAYER_BOOK)


publish:
	make player-book
	make build
	git add $(ROOT_DIR)*
	git commit -m "Publish new version."
	git push


.PHONY: dev build clean help Makefile publish player-book

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
