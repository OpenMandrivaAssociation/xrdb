Name: xrdb
Version: 1.1.0
Release: 4
Summary: X server resource database utility
Group: Development/X11
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: pkgconfig(xmu) >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
Requires: mcpp

%description
Xrdb is used to get or set the contents of the RESOURCE_MANAGER property on the
root window of screen 0, or the SCREEN_RESOURCES property on the root window of
any or all screens, or everything combined.

%prep
%setup -q -n %{name}-%{version}

%build
autoreconf -fi
%configure2_5x --with-cpp=%{_bindir}/mcpp

%make

%install
%makeinstall_std

%files
%{_bindir}/xrdb
%{_mandir}/man1/xrdb.*


%changelog
* Wed Apr 06 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.0.9-1mdv2011.0
+ Revision: 651346
- new version 1.0.9
- built with mccp to be required instead of (gcc-)cpp

* Thu Feb 03 2011 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.8-1
+ Revision: 635478
- New version: 1.0.8
- Remove redundant configure options

  + Thierry Vignaud <tv@mandriva.org>
    - new release

* Wed Nov 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.6-1mdv2010.1
+ Revision: 464748
- New version: 1.0.6

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.5-3mdv2009.1
+ Revision: 350810
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.0.5-2mdv2009.0
+ Revision: 266152
- rebuild early 2009.0 package (before pixel changes)

* Mon Apr 14 2008 Thierry Vignaud <tv@mandriva.org> 1.0.5-1mdv2009.0
+ Revision: 193007
- new release

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Thu Jan 17 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.4-2mdv2008.1
+ Revision: 154358
- Updated BuildRequires and resubmit package.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0.4-1mdv2008.0
+ Revision: 64853
- fix man pages
- new release


* Mon Feb 05 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.3-1mdv2007.0
+ Revision: 116299
- new upstream version: 1.0.3
- rebuild to fix cooker uploading
- X11R7.1
- increment release
- Adding X.org 7.0 to the repository

  + Frederic Crozat <fcrozat@mandriva.com>
    - Add missing dependency on cpp

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fill in a couple of missing descriptions

