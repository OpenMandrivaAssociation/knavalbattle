%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	Battleship game with built-in game server
Name:		knavalbattle
Version:	21.08.0
Release:	1
Epoch:		1
License:	GPLv2 and LGPLv2 and GFDL
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/games/navalbattle/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Crash) cmake(KF5KDEGames)
BuildRequires:	cmake(KF5DBusAddons) cmake(KF5DNSSD) cmake(KF5I18n) cmake(KF5TextWidgets) cmake(KF5XmlGui)
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
%autosetup -p1
%cmake_kde5

%build 
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html

%files -f %{name}.lang
%{_kde5_bindir}/knavalbattle
%{_kde5_datadir}/kconf_update/knavalbattle.upd
%{_kde5_iconsdir}/hicolor/*/apps/knavalbattle.*
%{_kde5_datadir}/applications/org.kde.knavalbattle.desktop
%{_kde5_datadir}/knavalbattle/pictures/default.desktop
%{_kde5_datadir}/knavalbattle/pictures/default_theme.svgz
%{_kde5_datadir}/knavalbattle/sounds/ship-player-shoot-water.ogg
%{_kde5_datadir}/knavalbattle/sounds/ship-player1-shoot.ogg
%{_kde5_datadir}/knavalbattle/sounds/ship-player2-shoot.ogg
%{_kde5_datadir}/knavalbattle/sounds/ship-sink.ogg
%{_datadir}/metainfo/org.kde.knavalbattle.appdata.xml
%{_datadir}/qlogging-categories5/knavalbattle.categories
