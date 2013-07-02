Name:		knavalbattle
Version:	4.10.5
Release:	1
Epoch:		1
Summary:	Battleship game with built-in game server
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/navalbattle/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
Obsoletes:	kbattleship < 1:4.9.80
Provides:	kbattleship = %{EVRD}

%description
Naval Battle (ex-KBattleship) is a Battle Ship game for KDE.

Ships are placed on a board which represents the sea. Players try to hit each
others ships in turns without knowing where they are placed. The first player
to destroy all ships wins the game.

%files
%{_kde_bindir}/kbattleship
%{_kde_applicationsdir}/kbattleship.desktop
%{_kde_docdir}/*/*/kbattleship
%{_kde_iconsdir}/hicolor/*/apps/kbattleship.png
%{_kde_appsdir}/kbattleship
%{_kde_services}/kbattleship.protocol

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package

