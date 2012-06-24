Summary:	viewres application - graphical class browser for Xt
Summary(pl.UTF-8):	Aplikacja viewres - graficzna przeglądarka klas dla Xt
Name:		xorg-app-viewres
Version:	1.0.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/viewres-%{version}.tar.bz2
# Source0-md5:	cdbed540daf7975b56000420c9aa5bf9
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-util-util-macros >= 0.99.2
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
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/viewres
%{_datadir}/X11/app-defaults/Viewres
%{_mandir}/man1/viewres.1x*
