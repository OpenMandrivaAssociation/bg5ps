%define	name	bg5ps
%define	version	1.3.0
%define release	16

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A program for converting PostScript files to Chinese PostScript files
Source0:	ftp://ftp.debian.org/debian/dists/unstable/main/source/text/%{name}_%{version}.orig.tar.bz2
Patch0:		bg5ps-geoff.patch
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
%doc TESTTTF2PSM.short Readme doc examples
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/chinese/*



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-15mdv2011.0
+ Revision: 616748
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 1.3.0-14mdv2010.0
+ Revision: 424610
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 1.3.0-13mdv2009.0
+ Revision: 240443
- rebuild
- fix spacing at top of description
- kill re-definition of %%buildroot on Pixel's request
- fix summary-ended-with-dot

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Sep 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.0-11mdv2008.0
+ Revision: 89580
- rebuild

* Wed Apr 25 2007 Adam Williamson <awilliamson@mandriva.org> 1.3.0-10mdv2008.0
+ Revision: 18125
- rebuild for new era, fix spec


* Fri May 12 2006 Stefan van der Eijk <stefan@eijk.nu> 1.3.0-9mdk
- rebuild for sparc

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.3.0-8mdk
- Rebuild

* Tue Jul 22 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.3.0-7mdk
- rebuild
- rm -rf $RPM_BUILD_ROOT in %%install, not %%prep
- use %%make macro

