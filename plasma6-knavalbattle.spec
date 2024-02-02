%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	Battleship game with built-in game server
Name:		plasma6-knavalbattle
Version:	24.01.95
Release:	1
License:	GPLv2 and LGPLv2 and GFDL
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/games/navalbattle/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/knavalbattle-%{version}.tar.xz
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Crash) cmake(KDEGames6)
BuildRequires:	cmake(KF6DBusAddons) cmake(KF6DNSSD) cmake(KF6I18n) cmake(KF6TextWidgets) cmake(KF6XmlGui)
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
Obsoletes:	kbattleship < 1:4.9.80
Provides:	kbattleship = %{EVRD}

%description
Naval Battle (ex-KBattleship) is a Battle Ship game for KDE.

Ships are placed on a board which represents the sea. Players try to hit each
others ships in turns without knowing where they are placed. The first player
to destroy all ships wins the game.




#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n knavalbattle-%{?git:master}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build 
%ninja -C build

%install
%ninja_install -C build
%find_lang knavalbattle --with-html

%files -f knavalbattle.lang
%{_bindir}/knavalbattle
%{_iconsdir}/hicolor/*/apps/knavalbattle.*
%{_datadir}/applications/org.kde.knavalbattle.desktop
%{_datadir}/knavalbattle/pictures/default.desktop
%{_datadir}/knavalbattle/pictures/default_theme.svgz
%{_datadir}/knavalbattle/sounds/ship-player-shoot-water.ogg
%{_datadir}/knavalbattle/sounds/ship-player1-shoot.ogg
%{_datadir}/knavalbattle/sounds/ship-player2-shoot.ogg
%{_datadir}/knavalbattle/sounds/ship-sink.ogg
%{_datadir}/metainfo/org.kde.knavalbattle.appdata.xml
%{_datadir}/qlogging-categories6/knavalbattle.categories
