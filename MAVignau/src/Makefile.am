bin_SCRIPTS = pyhello
CLEANFILES = $(bin_SCRIPTS)
EXTRA_DIST = pyhello.py

do_substitution = sed -e 's,[@]pythondir[@],$(pythondir),g' \
	-e 's,[@]PACKAGE[@],$(PACKAGE),g' \
	-e 's,[@]VERSION[@],$(VERSION),g' 

pyhello: pyhello.py Makefile
	$(do_substitution) < $(srcdir)/pyhello.py > pyhello
	chmod +x pyhello

pyhello_PYTHON = pyhello.py

pyhellodir = $(pythondir)/pyhello
