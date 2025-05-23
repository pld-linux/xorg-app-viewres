Summary:	viewres application - graphical class browser for Xt
Summary(pl.UTF-8):	Aplikacja viewres - graficzna przeglądarka klas dla Xt
Name:		xorg-app-viewres
Version:	1.0.8
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/viewres-%{version}.tar.xz
# Source0-md5:	4ac938b5ce5d190ae0d3ba5fd6eaea4a
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The viewres program displays a tree showing the widget class hierarchy
of the Athena Widget Set. Each node in the tree can be expanded to
show the resources that the corresponding class adds (i.e. does not
inherit from its parent) when a widget is created. This application
allows the user to visually examine the structure and inherited
resources for the Athena Widget Set.

%description -l pl.UTF-8
Program viewres wyświetla drzewo obrazujące hierarchię klas widgetów
Athena. Każdy węzeł drzewa może być rozszerzony aby pokazywać zasoby
dodawane przez odpowiadającą mu klasę (tzn. nie dziedziczone od
rodzica) podczas tworzenia widgetu. Ta aplikacja pozwala użytkownikowi
wizualnie przeglądać strukturę i dziedziczone zasoby widgetów Athena.

%prep
%setup -q -n viewres-%{version}

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
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/viewres
%{_datadir}/X11/app-defaults/Viewres
%{_datadir}/X11/app-defaults/Viewres-color
%{_mandir}/man1/viewres.1*
