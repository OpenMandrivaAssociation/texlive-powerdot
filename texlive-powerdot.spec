# revision 25656
# category Package
# catalog-ctan /macros/latex/contrib/powerdot
# catalog-date 2012-03-13 22:44:46 +0100
# catalog-license lppl1.3
# catalog-version 1.4i
Name:		texlive-powerdot
Version:	1.4i
Release:	1
Summary:	A presentation class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/powerdot
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/powerdot.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/powerdot.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/powerdot.source.tar.xz
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
%{_texmfdistdir}/tex/latex/powerdot/powerdot-aggie.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-bframe.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-ciment.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-default.ps
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
%doc %{_texmfdistdir}/doc/latex/powerdot/RunDoc
%doc %{_texmfdistdir}/doc/latex/powerdot/RunExamples
%doc %{_texmfdistdir}/doc/latex/powerdot/RunSlideDoc
%doc %{_texmfdistdir}/doc/latex/powerdot/clemson.eps
%doc %{_texmfdistdir}/doc/latex/powerdot/manifest.txt
%doc %{_texmfdistdir}/doc/latex/powerdot/pawmkorange.eps
%doc %{_texmfdistdir}/doc/latex/powerdot/pawmkorange.png
%doc %{_texmfdistdir}/doc/latex/powerdot/pawmkpurple.eps
%doc %{_texmfdistdir}/doc/latex/powerdot/pawmkpurple.png
%doc %{_texmfdistdir}/doc/latex/powerdot/pawtraceorange.eps
%doc %{_texmfdistdir}/doc/latex/powerdot/pawtraceorange.png
%doc %{_texmfdistdir}/doc/latex/powerdot/pawtracep.eps
%doc %{_texmfdistdir}/doc/latex/powerdot/pawtracep.png
%doc %{_texmfdistdir}/doc/latex/powerdot/powerdot-example.lyx
%doc %{_texmfdistdir}/doc/latex/powerdot/powerdot-example.tex
%doc %{_texmfdistdir}/doc/latex/powerdot/powerdot-example1.pdf
%doc %{_texmfdistdir}/doc/latex/powerdot/powerdot-example1.tex
%doc %{_texmfdistdir}/doc/latex/powerdot/powerdot-example2.pdf
%doc %{_texmfdistdir}/doc/latex/powerdot/powerdot-example2.tex
%doc %{_texmfdistdir}/doc/latex/powerdot/powerdot-example3.pdf
%doc %{_texmfdistdir}/doc/latex/powerdot/powerdot-example3.tex
%doc %{_texmfdistdir}/doc/latex/powerdot/powerdot-styleexample.tex
%doc %{_texmfdistdir}/doc/latex/powerdot/powerdot-styletest.tex
%doc %{_texmfdistdir}/doc/latex/powerdot/powerdot.bib
%doc %{_texmfdistdir}/doc/latex/powerdot/powerdot.layout
%doc %{_texmfdistdir}/doc/latex/powerdot/powerdot.pdf
%doc %{_texmfdistdir}/doc/latex/powerdot/powerdot.tex
%doc %{_texmfdistdir}/doc/latex/powerdot/powerdotDE.pdf
%doc %{_texmfdistdir}/doc/latex/powerdot/powerdotDE.tex
%doc %{_texmfdistdir}/doc/latex/powerdot/powerdotSlide.pdf
%doc %{_texmfdistdir}/doc/latex/powerdot/powerdotSlide.tex
#- source
%doc %{_texmfdistdir}/source/latex/powerdot/powerdot.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
