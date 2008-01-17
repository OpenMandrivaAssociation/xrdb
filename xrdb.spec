Name: xrdb
Version: 1.0.4
Release: %mkrel 2
Summary: X server resource database utility
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros	>= 1.1.5
BuildRequires: libx11-devel	>= 1.1.3
BuildRequires: libxmu-devel	>= 1.0.3
Requires: gcc-cpp

%description
Xrdb is used to get or set the contents of the RESOURCE_MANAGER property on the
root window of screen 0, or the SCREEN_RESOURCES property on the root window of
any or all screens, or everything combined.

%prep
%setup -q -n %{name}-%{version}

%build
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xrdb
%{_mandir}/man1/xrdb.*
