Name: xrdb
Version: 1.0.5
Release: %mkrel 3
Summary: X server resource database utility
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxmu-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
Requires: gcc-cpp

%description
Xrdb is used to get or set the contents of the RESOURCE_MANAGER property on the
root window of screen 0, or the SCREEN_RESOURCES property on the root window of
any or all screens, or everything combined.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
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
