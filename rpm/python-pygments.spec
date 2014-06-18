Name:           python-pygments
Version:        1.6
Release:        1
Summary:        Syntax highlighting engine written in Python

Group:          Development/Libraries
License:        BSD
URL:            http://pygments.org/
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel >= 2.4
BuildRequires:  python-setuptools

Requires:       python-setuptools
Requires:       python-imaging

%description
Pygments is a generic syntax highlighter for general use in all kinds
of software such as forum systems, wikis or other applications that
need to prettify source code. Highlights are:

  * a wide range of common languages and markup formats is supported
  * special attention is paid to details that increase highlighting
    quality
  * support for new languages and formats are added easily; most
    languages use a simple regex-based lexing mechanism
  * a number of output formats is available, among them HTML, RTF,
    LaTeX and ANSI sequences
  * it is usable as a command-line tool and as a library
  * ... and it highlights even Brainf*ck!

%prep
%setup -q -n %{name}-%{version}/pygments

%build
%{__python} setup.py build
%{__sed} -i 's/\r//' LICENSE

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
pushd docs
install -d %{buildroot}%{_mandir}/man1
mv pygmentize.1 $RPM_BUILD_ROOT%{_mandir}/man1/pygmentize.1
mv build html
mv src reST
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
# For noarch packages: sitelib
%{python_sitelib}/*
%{_bindir}/pygmentize
%lang(en) %{_mandir}/man1/pygmentize.1.gz
