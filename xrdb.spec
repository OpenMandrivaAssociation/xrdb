Name: xrdb
Version: 1.2.1
Release: 1
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
%autosetup -n %{name}-%{version} -p1

%build
autoreconf -fi
%configure --with-cpp=%{_bindir}/mcpp

%make_build

%install
%make_install

%files
%{_bindir}/xrdb
%{_mandir}/man1/xrdb.*
