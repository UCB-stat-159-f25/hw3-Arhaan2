.PHONY: env html clean

env:
	@echo ">>> Creating or updating conda environment 'ligo'..."
	@conda env update -n ligo -f environment.yml || conda env create -n ligo -f environment.yml
	@echo ">>> Done. Environment configured (not activated)."

html:
	@echo ">>> Building MyST site..."
	myst build --html
	@echo ">>> Build complete. View files in _build/html/"

clean:
	@echo ">>> Cleaning generated files..."
	rm -rf figures/* audio/* _build
	@echo ">>> Clean complete."

