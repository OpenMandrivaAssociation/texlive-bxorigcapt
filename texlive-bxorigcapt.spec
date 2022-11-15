Name:		texlive-bxorigcapt
Version:	64072
Release:	1
Summary:	To retain the original caption names when using Babel
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bxorigcapt
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxorigcapt.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxorigcapt.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package forces the caption names (\chaptername, \today,
etc) declared by the document class in use to be used as the
caption names for a specific language introduced by the Babel
package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/bxorigcapt
%doc %{_texmfdistdir}/doc/latex/bxorigcapt

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
