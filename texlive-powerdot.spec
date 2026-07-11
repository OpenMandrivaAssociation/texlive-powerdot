%global tl_name powerdot
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.7
Release:	%{tl_revision}.1
Summary:	A presentation class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/powerdot
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/powerdot.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/powerdot.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/powerdot.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Powerdot is a presentation class for LaTeX that allows for the quick and
easy development of professional presentations. It comes with many tools
that enhance presentations and aid the presenter. Examples are automatic
overlays, personal notes and a handout mode. To view a presentation,
DVI, PS or PDF output can be used. A powerful template system is
available to easily develop new styles. A LyX layout file is provided.

