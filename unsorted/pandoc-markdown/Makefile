SRC=$(wildcard *.md)

OS := $(shell uname)

cleanstart:
	make clean
	mkdir static
	echo "PGh0bWw+PGhlYWQ+PHN0eWxlIHR5cGU9InRleHQvY3NzIj5wLHByZSxsaSB7IGxpbmUtaGVpZ2h0OiAxLjU7IH0gYm9keSxwLGgxLGgyLGgzLGg0LGg1LGg2LGxpIHsgZm9udC1zaXplOiAxMnB0OyBmb250LWZhbWlseTogc2Fucy1zZXJpZjsgfSBwcmUgeyBwYWRkaW5nOiA1cHg7IG1hcmdpbjogMTBweDsgYmFja2dyb3VuZDogYmVpZ2U7IG92ZXJmbG93OiBhdXRvOyB9IGJvZHkgeyB3aWR0aDogMTIwMHB4OyBtYXJnaW46IDBweDsgcGFkZGluZzogMTBweDsgbWFyZ2luLWxlZnQ6IDUwcHg7IH08L3N0eWxlPjwvaGVhZD4KCgo8ZnJhbWVzZXQgY29scz0iMzUwLCoiIGJvcmRlcj0iMCIgZnJhbWVib3JkZXI9IjAiPgogICAgCiAgICA8ZnJhbWUgc3JjPSJzZWFyY2guaHRtbCIgbmFtZT0ic2VhcmNoIj48L2ZyYW1lPgogICAgPGZyYW1lIHNyYz0iIiAgICAgICAgICAgIG5hbWU9Im1haW4iPjwvZnJhbWU+Cgo8L2ZyYW1lc2V0Pgo=" | base64 -D >static/index.html
	echo "PGh0bWw+PGhlYWQ+CiAgICA8c3R5bGUgdHlwZT0idGV4dC9jc3MiPgogICAgICAgIGJvZHkgewogICAgICAgICAgICBtYXJnaW46IDBweDsKICAgICAgICAgICAgcGFkZGluZzogMTBweDsKICAgICAgICB9CiAgICA8L3N0eWxlPgo8L2hlYWQ+CgoKPGJvZHkgb25sb2FkPSJrdXAoJycpOyBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgncycpLmZvY3VzKCk7Ij4KCjxzY3JpcHQgdHlwZT0idGV4dC9qYXZhc2NyaXB0Ij4KICAgIGZ1bmN0aW9uIGt1cChzZW5kZXIpIHsKICAgICAgICB2YXIgcyA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJzIik7CiAgICAgICAgdmFyIGwgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgibCIpOwoKICAgICAgICBpZiAocy52YWx1ZSA9PSAiIikgewogICAgICAgICAgICBkb2N1bWVudC5xdWVyeVNlbGVjdG9yQWxsKCcjbCBvcHRpb24nKS5mb3JFYWNoKG9wdGlvbiA9PiBvcHRpb24ucmVtb3ZlKCkpOwogICAgICAgICAgICBkb2N1bWVudHMuZm9yRWFjaChmdW5jdGlvbihpdGVtKSB7CiAgICAgICAgICAgICAgICB2YXIgb3B0ID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgib3B0aW9uIik7CiAgICAgICAgICAgICAgICBvcHQudGV4dCA9IGl0ZW0udGl0bGU7CiAgICAgICAgICAgICAgICBvcHQudmFsdWUgPSBpdGVtLmlkOwogICAgICAgICAgICAgICAgbC5hZGQob3B0KTsKICAgICAgICAgICAgfSk7CiAgICAgICAgICAgIGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3JBbGwoJyNsIG9wdGlvbicpLmZvckVhY2gob3B0aW9uID0+IG9wdGlvbi5yZW1vdmUoKSk7CiAgICAgICAgICAgIGRvY3VtZW50cy5mb3JFYWNoKGZ1bmN0aW9uKGl0ZW0pIHsKICAgICAgICAgICAgICAgIHZhciBvcHQgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCJvcHRpb24iKTsKICAgICAgICAgICAgICAgIG9wdC50ZXh0ID0gaXRlbS50aXRsZTsKICAgICAgICAgICAgICAgIG9wdC52YWx1ZSA9IGl0ZW0uaWQ7CiAgICAgICAgICAgICAgICBsLmFkZChvcHQpOwogICAgICAgICAgICB9KTsKICAgICAgICAgICAgbC5zZXRBdHRyaWJ1dGUoInNpemUiLCBsLmxlbmd0aCk7CiAgICAgICAgfQogICAgICAgIGVsc2UgewogICAgICAgICAgICBkb2N1bWVudC5xdWVyeVNlbGVjdG9yQWxsKCcjbCBvcHRpb24nKS5mb3JFYWNoKG9wdGlvbiA9PiBvcHRpb24ucmVtb3ZlKCkpOwogICAgICAgICAgICB3b3JkcyA9IHMudmFsdWUuc3BsaXQoIiAiKTsKCiAgICAgICAgICAgIGRvY3VtZW50cy5mb3JFYWNoKGZ1bmN0aW9uKGl0ZW0pIHsKICAgICAgICAgICAgICAgIG1hdGNoZXMgPSAwOyAvLyBjb3VudCBpZiBhbGwgd29yZHMgZnJvbSB0aGUgc2VhcmNoLXN0cmluZyAoc3BhY2Ugc2VwYXJhdGVkKSBtYXRjaAogICAgICAgICAgICAgICAgd29yZHMuZm9yRWFjaChmdW5jdGlvbih3b3JkKSB7CiAgICAgICAgICAgICAgICAgICAgaWYgKGl0ZW0udGl0bGUudG9VcHBlckNhc2UoKS5pbmRleE9mKHdvcmQudG9VcHBlckNhc2UoKSkgIT0gLTEpIHsKICAgICAgICAgICAgICAgICAgICAgICAgbWF0Y2hlcysrOwogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgIH0pOwoKICAgICAgICAgICAgICAgIGlmIChtYXRjaGVzID09IHdvcmRzLmxlbmd0aCkgewogICAgICAgICAgICAgICAgICAgIC8vIGFkZCBpZiBhbGwgbWF0Y2gKICAgICAgICAgICAgICAgICAgICB2YXIgb3B0ID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgib3B0aW9uIik7CiAgICAgICAgICAgICAgICAgICAgb3B0LnRleHQgPSBpdGVtLnRpdGxlOwogICAgICAgICAgICAgICAgICAgIG9wdC52YWx1ZSA9IGl0ZW0uaWQ7CiAgICAgICAgICAgICAgICAgICAgbC5hZGQob3B0KTsKICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgfSk7Ci8vICAgICAgICAgICAgdmFyIG9wdCA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoIm9wdGlvbiIpOwovLyAgICAgICAgICAgIG9wdC50ZXh0ID0gIiciICsgcy52YWx1ZSArICInICgiK3MudmFsdWUubGVuZ3RoKyIpIjsKLy8gICAgICAgICAgICBsLmFkZChvcHQpOwoKICAgICAgICAgICAgLy8gaWYgb25seSBvbmUgZWxlbWVudCA9PiBzaG93CgogICAgICAgICAgICBpZiAobC5sZW5ndGggPT0gMSkgewogICAgICAgICAgICAgICAgbC5zZWxlY3RlZEluZGV4ID0gMDsKICAgICAgICAgICAgICAgIHdpbmRvdy50b3AuZnJhbWVzWzFdLmxvY2F0aW9uID0gbC52YWx1ZSArICcuaHRtbCcKICAgICAgICAgICAgfQoKICAgICAgICAgICAgbC5zZXRBdHRyaWJ1dGUoInNpemUiLCBsLmxlbmd0aCArIDEpOwoKICAgICAgICB9CgogICAgfQoKICAgIHZhciBkb2N1bWVudHMgPSBbXTsKPC9zY3JpcHQ+CjxzY3JpcHQgdHlwZT0idGV4dC9qYXZhc2NyaXB0IiBzcmM9InRvYy5qcyI+PC9zY3JpcHQ+CjxpbnB1dCBzdHlsZT0iYmFja2dyb3VuZDogYmVpZ2U7IHdpZHRoOiAxMDAlOyIgaWQ9InMiIG9ua2V5dXA9Imt1cCh0aGlzKTsiIC8+Cgo8YnIvPgoKPHNlbGVjdCBzdHlsZT0iYm9yZGVyOiAwcHggc29saWQgYmxhY2s7IHdpZHRoOiAxMDAlOyIgc2l6ZT0iMTAwIiBpZD0ibCIgb25jbGljaz0iaWYgKHRoaXMudmFsdWUgIT0gJycpIHdpbmRvdy50b3AuZnJhbWVzWzFdLmxvY2F0aW9uID0gdGhpcy52YWx1ZSArICcuaHRtbCc7IiBvbmNoYW5nZT0iaWYgKHRoaXMudmFsdWUgIT0gJycpIHdpbmRvdy50b3AuZnJhbWVzWzFdLmxvY2F0aW9uID0gdGhpcy52YWx1ZSArICcuaHRtbCc7IiAvPgo=" | base64 -D >static/search.html
	echo "documents = [" >static/toc.js
	make all
	echo "];" >>static/toc.js
	echo "documents.sort(function(a,b) { if (a.title <= b.title) { return -1; } else { return 1; } });" >>static/toc.js
	cat static/toc.js | grep -v '""' >static/toc.js.clean
	cat static/toc.js.clean >static/toc.js
	rm -f static/toc.js.clean
	rm -f static-flat.tar
	cd static; scp *.html *.js `cat ../deploy`

all: ${SRC:.md=.html}
	#cat ${SRC:.md=.html} >index.html

clean:
	rm -f *html
	rm -fr static

one:
	make clean
	rm -f index.md
	cat *.md >index.md
	make index.html

ifeq ($(OS),Darwin)
%.html: %.md
	@echo " ======= BEGIN: $@ ========================================"
	pandoc --toc --toc-depth 6 --self-contained -N -f markdown_github -t html -o $@ $<
	tail -c +`egrep -b -e '^<body>$$' $@ | cut -d ':' -f 1` $@ >$@.tmp
	cat $@.tmp | grep -v "<body>" >$@
	rm -f $@.tmp
	echo '<html><head><style type="text/css">table td, table th { padding: 10px; } table td { background: silver; } table th { background: grey; } pre { font-size: 10pt; } div#TOC { margin: 50px; border-left: 2px solid black; } div#TOC a { text-decoration: none; color: black; font-weight: bold; font-size: 8pt; } p,pre,li { line-height: 1.5; } h1,h2,h3,h4,h5,h6 {margin-top: 30px; font-family: sans-serif; } body,p,li { font-size: 12pt; font-family: sans-serif; } pre { padding: 5px; margin: 10px; background: silver; overflow: auto; } body { width: 1000px; margin: 0px; padding: 10px; margin-left: 50px; }</style></head><body>' "<b>`head -20 $< | grep '^# ' | tr -d '#' | head -1`</b><br><br>" >full_$@
	cat $@ >>full_$@
	sed -i "" 's|\</pre\>|\</pre\>\<input style="position: relative; top: -5px; float: right; " type=button value="Copy" onclick="navigator.clipboard.writeText(this.previousSibling.textContent);"/\>|g' full_$@
	cat full_$@ >$@
	rm -f full_$@
	sed -i '' 's|<p>Document ID\: .*</p>||' $@
	cat $@ >static/`head -1 $< | grep '^Document ID: ' | cut -d ' ' -f 3`.html
	echo "{ \"id\": \"`head -1 $< | grep '^Document ID: ' | cut -d ' ' -f 3`\", \"title\": \"`head -20 $< | grep '^# ' | tr -d '#' | head -1`\" }," >>static/toc.js
	rm -f static/.html
	@echo " ======= END: $@ ========================================"
else
%.html: %.md
	pandoc --self-contained -N -f markdown_github -t html -o $@ $<
	tail -c +`egrep -b -e '^<body>$$' $@ | cut -d ':' -f 1` $@ >$@.tmp
	cat $@.tmp | grep -v "<body>" >$@
	rm -f $@.tmp
	echo '<html><head><style type="text/css">p,pre,li { line-height: 1.5; } p,h1,h2,h3,h4,h5,h6,li { font-family: sans-serif; } pre { padding: 5px; margin: 10px; background: beige; overflow: auto; } body { width: 1200px; margin: 0px; padding: 10px; }</style></head><body>' >full_$@
	cat $@ >>full_$@
	sed -i 's|</pre>|</pre><input style="position: relative; top: -5px; float: right; " type=button value="Block into Clipboard" onclick="navigator.clipboard.writeText(this.previousSibling.textContent);"/>|g' full_$@
	cat full_$@ >$@
	rm -f full_$@
endif

dev:
	base64 static/search.html | pbcopy -Prefer txt
	${HOME}/bin/e Makefile:9:7
