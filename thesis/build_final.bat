@echo off

pdflatex -interaction=nonstopmode thesis.tex
bibtex thesis
pdflatex -interaction=nonstopmode thesis.tex
pdflatex -interaction=nonstopmode thesis.tex

gswin64c -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/printer -dNOPAUSE -dQUIET -dBATCH -sOutputFile=thesis_compressed.pdf thesis.pdf


copy thesis_compressed.pdf jsl76-phd_thesis.pdf

