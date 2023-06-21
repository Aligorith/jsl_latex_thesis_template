jsl_thesis_template
===================

LaTeX / pdfLaTeX template extracted from the styling code used for Dr Joshua Leung's
PhD Thesis at the University of Canterbury (2017).



## History

From memory, much of this was hacked together + cleaned up from a bunch of old templates,
with a major rewrite a some point to clean it up, followed by several weeks of fine-tuning
to get the look I wanted for various areas.

In particular, this template was originally heavily inspired/based on the UC COSC/CSSE Department one
([uocthesis](https://www.csse.canterbury.ac.nz/students/uocthesis/index.shtml)) 
for postgraduate students originally authored by Dr Michael Jason-Smith back in 2000-2001,
but only a few remanants of that remain in a few places today.


## General Usage Instructions

> **Disclaimer**:
> This was only ever tested to work via pdfLaTeX on Windows (via MikTeX 2.9 or older?).
> Your mileage with other distros / OS's may vary.

**Main Points**:
* The "thesis/" folder contains the main entrypoint. Individual parts and
  chapters are in the other folders at root level, with the intention that
  some of these can be spun out into source files for separate paper projects
  while sharing as much of the common code as possible.

* Use the build-scripts in the "thesis/" folder to compile the PDF output.
  These use pdfLaTex and BibTex.
  
  You will need to modify "build_final.bat" to change the filename that the
  final "compressed" version (i.e. one that has been compressed using
  GhostScript and/or has had all the editing synctex stuff stripped out)
  
* The "diagrams/" folder is for diagrams shared between the various chapters
  and sections. Mostly it is for the templates used when constructing all the
  other diagrams.
  
  Diagrams were mostly as high resolution PNG's (i.e. by targetting 300 dpi 
  in the Inkscape PNG Export settings), with some as PDF's where possible,
  and exported from the source files (e.g. SVG's, or in some cases, Powerpoint
  slide screenshots).

* Each chapter's folder then usually has its own "images" folder for containing
  all the images / figures / diagrams that are only used for that chapter.
  This was done to help keep all the graphs + study-specific figures isolated
  to separate folders to make it easier to manage them.
  
  Within each of these image folders, there is usually a "raw/" subfolder for
  containing all the source-data (e.g. SVG's in particular, but may also be 
  useful to put copies / links to relevant scripts for generating graphs + plots)

* BibTex - The folder where BibTeX libraries can be dumped. As you'll notice,
  the template is set up to allow for multiple `.bib` files to ultimately get
  included. Joshua's ones accumulated over several years working on his thesis
  are included here as a source of reference and/or to help with relevant work.


## Special Features

Check the example / template-docs for examples of some of the special features that are
built into the template. In particular, pay attention to all the various standard formatting
commands that were used to achieve various styling effects in favour of using many of the
standard TeX commands.


A few important ones to get you started:
* `\strong{Some Text}` - This does **bold** formatting

* `\emph{Some Text}` - This does *italic* formatting

* `\enquote{Some Text}` - This puts a pair of double-quotes around a piece of
  text. Use this instead of the normal backtick + straight-tick combo, as it
  triggers the use of custom quote symbols (imported from another font) as the
  default quote glyphs in Palantino are ugly and confusing (i.e. they are
  ugly thin slanting-line glyphs where the start/end ones are mostly 
  indistinguishable from each other).

* `\squote{Some Text}` - Single-quote version of `\enquote{}`

* `\unfinishedTxt{...blah...}` - This command (which features heavily in the
  template stubs included in the repo) can be used to indicate WIP content
  that needs revision. In the PDF, these show up with yellow shaded backgrounds
  for easier identification.

* `\queriedTxt{Dubious Claim}` - This claim is for flagging any fact / statement
  or similar with background shading a small question-mark (?) indicator to
  indicate that the flagged text needs attention / double-checking.


It is highly recommended to add custom commands for any special formatting
to be applied for any content-specific needs you may have (e.g. experiment
conditions, etc.). A bunch defined for such purposes have been left over,
and can be removed or adapted as needed.


## License

The code here is released "as-is" in the hopes that it might be useful + helpful
for someone out there.

If you do find this useful, please credit / reference the original repo at:
https://github.com/Aligorith/jsl_latex_thesis_template


-- Dr Joshua Leung
   June 2023