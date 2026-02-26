.PHONY: book book-en book-ru clean

book: book-ru book-en

book-ru:
	python3 scripts/compile.py --lang ru --output build/autonom-ru

book-en:
	python3 scripts/compile.py --lang en --output build/autonom-en

clean:
	rm -rf build/
