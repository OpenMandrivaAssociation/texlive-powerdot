# revision 31446
# category Package
# catalog-ctan /macros/latex/contrib/powerdot
# catalog-date 2013-07-04 18:59:59 +0200
# catalog-license lppl1.3
# catalog-version 1.4i
Name:		texlive-powerdot
Version:	1.4i
Release:	3
Summary:	A presentation class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/powerdot
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/powerdot.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/powerdot.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Powerdot is a presentation class for LaTeX that allows for the
quick and easy development of professional presentations. It
comes with many tools that enhance presentations and aid the
presenter. Examples are automatic overlays, personal notes and
a handout mode. To view a presentation, DVI, PS or PDF output
can be used. A powerful template system is available to easily
develop new styles. A LyX layout file is provided.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/powerdot/images/clemson.eps
%{_texmfdistdir}/tex/latex/powerdot/images/pawmkorange.eps
%{_texmfdistdir}/tex/latex/powerdot/images/pawmkorange.png
%{_texmfdistdir}/tex/latex/powerdot/images/pawmkpurple.eps
%{_texmfdistdir}/tex/latex/powerdot/images/pawmkpurple.png
%{_texmfdistdir}/tex/latex/powerdot/images/pawtraceorange.eps
%{_texmfdistdir}/tex/latex/powerdot/images/pawtraceorange.png
%{_texmfdistdir}/tex/latex/powerdot/images/pawtracep.eps
%{_texmfdistdir}/tex/latex/powerdot/images/pawtracep.png
%{_texmfdistdir}/tex/latex/powerdot/images/powerdot-default.ps
%{_texmfdistdir}/tex/latex/powerdot/powerdot-aggie.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-bframe.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-ciment.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-default.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-elcolors.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-fyma.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-horatio.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-husky.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-ikeda.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-jefka.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-klope.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-paintings.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-pazik.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-sailor.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-simple.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-tiger.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-tycja.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-upen.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot.cls
%doc %{_texmfdistdir}/doc/latex/powerdot/Changes
%doc %{_texmfdistdir}/doc/latex/powerdot/README
%doc %{_texmfdistdir}/doc/latex/powerdot/docs/RunDoc
%doc %{_texmfdistdir}/doc/latex/powerdot/docs/RunExamples
%doc %{_texmfdistdir}/doc/latex/powerdot/docs/RunSlideDoc
%doc %{_texmfdistdir}/doc/latex/powerdot/docs/manifest.txt
%doc %{_texmfdistdir}/doc/latex/powerdot/docs/powerdot-example1.pdf
%doc %{_texmfdistdir}/doc/latex/powerdot/docs/powerdot-example1.tex
%doc %{_texmfdistdir}/doc/latex/powerdot/docs/powerdot-example2.pdf
%doc %{_texmfdistdir}/doc/latex/powerdot/docs/powerdot-example2.tex
%doc %{_texmfdistdir}/doc/latex/powerdot/docs/powerdot-example3.pdf
%doc %{_texmfdistdir}/doc/latex/powerdot/docs/powerdot-example3.tex
%doc %{_texmfdistdir}/doc/latex/powerdot/docs/powerdot-styleexample.tex
%doc %{_texmfdistdir}/doc/latex/powerdot/docs/powerdot-styletest.tex
%doc %{_texmfdistdir}/doc/latex/powerdot/docs/powerdot.bib
%doc %{_texmfdistdir}/doc/latex/powerdot/docs/powerdot.pdf
%doc %{_texmfdistdir}/doc/latex/powerdot/docs/powerdot.tex
%doc %{_texmfdistdir}/doc/latex/powerdot/docs/powerdotDE.pdf
%doc %{_texmfdistdir}/doc/latex/powerdot/docs/powerdotDE.tex
%doc %{_texmfdistdir}/doc/latex/powerdot/docs/powerdotSlide.pdf
%doc %{_texmfdistdir}/doc/latex/powerdot/docs/powerdotSlide.tex
%doc %{_texmfdistdir}/doc/latex/powerdot/lyx/powerdot-example.lyx
%doc %{_texmfdistdir}/doc/latex/powerdot/lyx/powerdot-example.tex
%doc %{_texmfdistdir}/doc/latex/powerdot/lyx/powerdot.layout

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
