%define	name	bg5ps
%define	version	1.3.0
%define	release	9mdk

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A program for converting PostScript files to Chinese PostScript files.
Source0:	ftp://ftp.debian.org/debian/dists/unstable/main/source/text/%{name}_%{version}.orig.tar.bz2
Patch0:		bg5ps-geoff.patch
Patch1:		bg5ps-Makefile.patch
Source1:	gb2312-bg5ps.conf
Source2:	gbps
# note: should we apply debian's patch? heavy hacky hack ..!!
Group:		System/Internationalization
Requires:	fonts-ttf-big5 fonts-ttf-gb2312 locales-zh
BuildRequires:	freetype-devel
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description

bg5ps is a program for converting normally unreadable PostScript files 
which are encoded in Big5 or GB to be readable using TrueType fonts.

Its command line options are a bit harsh to get working but there
are detailed instructions on how to do so.

The default system wide encoding is Big5. This can be overridden either by
using the GB configuration file in the documents directory, which will then
prevail to be the system wide policy for bg5ps or alternatively you may want to
use a custom-defined one in your home directory, which will be on a per-user
basis.


%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/chinese}
make BINDIR=$RPM_BUILD_ROOT%{_bindir} \
   ETCDIR=$RPM_BUILD_ROOT%{_sysconfdir}/chinese install

#install default big5 configuration file to /etc/chinese.
install -m644 big5-bg5ps.conf $RPM_BUILD_ROOT%{_sysconfdir}/chinese/bg5ps.conf
install -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/chinese/gb2312-bg5ps.conf
install -m755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/gbps

%clean
rm -rf $RPM_BUILD_ROOT

# we don't use noreplace, stupid. we have a user defined one in ~/ ...

%files
%defattr(-,root,root)
%doc [A-Z][A-Z]* TESTTTF2PSM.short Readme doc examples *.conf
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/chinese/*

