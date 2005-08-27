Summary:	viewres application
Summary(pl):	Aplikacja viewres
Name:		xorg-app-viewres
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/viewres-%{version}.tar.bz2
# Source0-md5:	a6a9428e15720124601f3dbeb6e2db11
Patch0:		viewres-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
viewres application.

%description -l pl
Aplikacja viewres.

%prep
%setup -q -n viewres-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/X11/app-defaults/Viewres
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
