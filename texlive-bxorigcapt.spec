%global tl_name bxorigcapt
%global tl_revision 78793

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	To retain the original caption names when using Babel
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bxorigcapt
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxorigcapt.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxorigcapt.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package forces the caption names (\chaptername, \today, etc)
declared by the document class in use to be used as the caption names
for a specific language introduced by the Babel package.

