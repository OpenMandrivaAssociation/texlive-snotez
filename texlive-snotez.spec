# revision 30355
# category Package
# catalog-ctan /macros/latex/contrib/snotez
# catalog-date 2013-05-09 13:28:31 +0200
# catalog-license lppl1.3
# catalog-version 0.3
Name:		texlive-snotez
Version:	0.3
Release:	9
Summary:	Typeset notes, in the margin
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/snotez
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/snotez.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/snotez.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a macro \sidenote, that places a note in
the margin of the document, with its baseline aligned with the
baseline in the body of the document. These sidenotes are
numbered (both in the text, and on the notes themselves). The
package loads the package etoolbox, pgfopts, marginnote and
perpage.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/snotez/snotez.sty
%doc %{_texmfdistdir}/doc/latex/snotez/README
%doc %{_texmfdistdir}/doc/latex/snotez/snotez_en.pdf
%doc %{_texmfdistdir}/doc/latex/snotez/snotez_en.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
