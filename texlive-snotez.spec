%global tl_name snotez
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7
Release:	%{tl_revision}.1
Summary:	Typeset notes, in the margin
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/snotez
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/snotez.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/snotez.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a macro \sidenote, that places a note in the margin
of the document, with its baseline aligned with the baseline in the body
of the document. These sidenotes are numbered (both in the text, and on
the notes themselves). The package loads the package etoolbox, pgfopts
and marginnote.

