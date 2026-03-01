.PHONY: all book book-en clean

COMPILE = python3 scripts/compile_v2.py
OUT = build

all: book book-en

book:
	@echo "📖 Building Russian edition..."
	@mkdir -p $(OUT)
	$(COMPILE) --lang ru --output $(OUT)/autonom-ru

book-en:
	@echo "📖 Building English edition..."
	@mkdir -p $(OUT)
	$(COMPILE) --lang en --output $(OUT)/autonom-en

clean:
	rm -rf $(OUT)
