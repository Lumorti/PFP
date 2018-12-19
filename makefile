install:
	mkdir -p /usr/local/share/pfp
	cp -r * /usr/local/share/pfp/
	ln -sf /usr/local/share/pfp/pfp /usr/local/bin/pfp

uninstall:
	rm -r /usr/local/share/pfp
	rm /usr/local/bin/pfp
