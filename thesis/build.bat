@echo off

pdflatex -synctex=1 -interaction=nonstopmode thesis.tex
bibtex thesis
pdflatex -synctex=1 -interaction=nonstopmode thesis.tex
pdflatex -synctex=1 -interaction=nonstopmode thesis.tex
