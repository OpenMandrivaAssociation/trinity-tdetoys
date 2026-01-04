%bcond clang 1
%bcond gamin 1

# BUILD WARNING:
#  Remove qt-devel and qt3-devel and any kde*-devel on your system !
#  Having KDE libraries may cause FTBFS here !

# TDE variables
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 3

%define tde_pkg tdetoys
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity

Name:		trinity-%{tde_pkg}
Summary:	Trinity Desktop Environment - Toys and Amusements
Version:	%{tde_version}
Release:	%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Group:		Amusements/Graphics
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


Source0:	https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/core/%{tarball_name}-%{version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DPKGCONFIG_INSTALL_DIR=%{tde_prefix}/%{_lib}/pkgconfig
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

# Trinity dependencies
BuildRequires: trinity-tdelibs-devel >= %{tde_version}
BuildRequires: trinity-kdesktop >= %{tde_version}
BuildRequires: trinity-kicker >= %{tde_version}
BuildRequires: trinity-tdebase-devel >= %{tde_version}

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	fdupes

BuildRequires: desktop-file-utils
BuildRequires: gettext

# IDN support
BuildRequires:	pkgconfig(libidn)

# GAMIN support
%{?with_gamin:BuildRequires:	pkgconfig(gamin)}

# ACL support
BuildRequires:  pkgconfig(libacl)

# PCRE2 support
BuildRequires:  pkgconfig(libpcre2-posix)

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(xext)


Obsoletes:		trinity-kdetoys < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-kdetoys = %{?epoch:%{epoch}:}%{version}-%{release}

# Metapackage
Requires: trinity-amor = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-eyesapplet = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-fifteenapplet = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kmoon = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kodo = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kteatime = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-ktux = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kweather = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kworldclock = %{?epoch:%{epoch}:}%{version}-%{release}


%description
Includes: 
* amor: Amusing Misuse Of Resources put's comic figures above your windows
* eyesapplet: a kicker applet similar to XEyes
* fifteenapplet: kicker applet, order 15 pieces in a 4x4 square by moving them
* kmoon: system tray applet showing the moon phase
* kodo: mouse movement meter
* kteatime: system tray applet that makes sure your tea doesn't get too strong
* ktux: Tux-in-a-Spaceship screen saver
* kweather: kicker applet that will display the current weather outside
* kworldwatch: application and kicker applet showing daylight area on the world
               globe

NOTE: kicker applets and screen savers require tdebase to be installed, 
and user to be logged-in to TDE.

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README

##########

%package -n trinity-amor
Summary:	a Trinity creature for your desktop
Group:		Amusements/Graphics

%description -n trinity-amor
AMOR stands for Amusing Misuse Of Resources. It provides several different
characters who prance around your X screen doing tricks and giving you tips.

Note that AMOR will only work with some window managers. Both TWin (the
TDE window manager) and Metacity (a GTK2 window manager) are supported.

This package is part of Trinity, and a component of the TDE toys module.

%files -n trinity-amor
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{tde_prefix}/bin/amor
%{tde_prefix}/share/apps/amor/
%{tde_prefix}/share/applications/tde/amor.desktop
%{tde_prefix}/share/icons/hicolor/*/apps/amor.png
%{tde_prefix}/share/doc/tde/HTML/en/amor/
%{tde_prefix}/share/man/man*/amor.*

##########

%package -n trinity-eyesapplet
Summary:	eyes applet for Trinity
Group:		Amusements/Graphics

Requires:	trinity-kicker >= %{tde_version}

%description -n trinity-eyesapplet
An applet for the TDE panel containing a pair of eyes that follow your mouse
around the screen.

This package is part of Trinity, and a component of the TDE toys module.

%files -n trinity-eyesapplet
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{tde_prefix}/%{_lib}/trinity/eyes_panelapplet.la
%{tde_prefix}/%{_lib}/trinity/eyes_panelapplet.so
%{tde_prefix}/share/apps/kicker/applets/eyesapplet.desktop

##########

%package -n trinity-fifteenapplet
Summary:	fifteen pieces puzzle for Trinity
Group:		Amusements/Graphics

%description -n trinity-fifteenapplet
An applet for the TDE panel that lets you play the Fifteen Pieces
sliding block puzzle. You have to order 15 pieces in a 4x4 square by
moving them around.

This package is part of Trinity, and a component of the TDE toys module.

%files -n trinity-fifteenapplet
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{tde_prefix}/%{_lib}/trinity/fifteen_panelapplet.la
%{tde_prefix}/%{_lib}/trinity/fifteen_panelapplet.so
%{tde_prefix}/share/apps/kicker/applets/kfifteenapplet.desktop

##########

%package -n trinity-kmoon
Summary:	moon phase indicator for Trinity
Group:		Amusements/Graphics

Requires:	trinity-kicker >= %{tde_version}

%description -n trinity-kmoon
An applet for the TDE panel that displays the current phase of the moon.

This package is part of Trinity, and a component of the TDE toys module.

%files -n trinity-kmoon
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{tde_prefix}/%{_lib}/trinity/kmoon_panelapplet.la
%{tde_prefix}/%{_lib}/trinity/kmoon_panelapplet.so
%{tde_prefix}/share/apps/kicker/applets/kmoonapplet.desktop
%{tde_prefix}/share/apps/kmoon/
%{tde_prefix}/share/icons/hicolor/*/apps/kmoon.png
%{tde_prefix}/share/doc/tde/HTML/en/kmoon/

##########

%package -n trinity-kodo
Summary:	mouse odometer for Trinity
Group:		Amusements/Graphics

%description -n trinity-kodo
KOdometer measures your desktop mileage. It tracks the movement of your mouse
pointer across your desktop and renders it in inches/feet/miles! It can
do cm/metres/km too. Its most exciting feature is the tripometer.

This package is part of Trinity, and a component of the TDE toys module.

%files -n trinity-kodo
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{tde_prefix}/bin/kodo
%{tde_prefix}/share/applications/tde/kodo.desktop
%{tde_prefix}/share/apps/kodo/
%{tde_prefix}/share/icons/hicolor/*/apps/kodo.png
%{tde_prefix}/share/doc/tde/HTML/en/kodo/
%{tde_prefix}/share/man/man*/kodo.*

##########

%package -n trinity-kteatime
Summary:	Trinity utility for making a fine cup of tea
Group:		Amusements/Graphics

%description -n trinity-kteatime
KTeaTime is a handy timer for steeping tea. No longer will you have to
guess at how long it takes for your tea to be ready. Simply select the
type of tea you have, and it will alert you when the tea is ready to
drink.

KTeaTime sits in the Trinity system tray.

Please note that KTeaTime is written explicitly for Trinity. If you are
using a non-TDE window manager or desktop environment then it is quite
possible that KTeaTime will not work on your system.

This package is part of Trinity, and a component of the TDE toys module.

%files -n trinity-kteatime
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{tde_prefix}/bin/kteatime
%{tde_prefix}/share/applications/tde/kteatime.desktop
%{tde_prefix}/share/apps/kteatime/
%{tde_prefix}/share/icons/hicolor/*/apps/kteatime.png
%{tde_prefix}/share/doc/tde/HTML/en/kteatime/
%{tde_prefix}/share/man/man*/kteatime.*

##########

%package -n trinity-ktux
Summary:	Tux screensaver for Trinity
Group:		Amusements/Graphics

%description -n trinity-ktux
A neat Tux-in-a-spaceship screensaver for the Trinity Desktop Environment (TDE).

This package is part of Trinity, and a component of the TDE toys module.

%files -n trinity-ktux
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{tde_prefix}/bin/ktux
%{tde_prefix}/share/apps/ktux/
%{tde_prefix}/share/applnk/System/ScreenSavers/ktux.desktop
%{tde_prefix}/share/icons/hicolor/*/apps/ktux.png
%{tde_prefix}/share/man/man*/ktux.*

##########

%package -n trinity-kweather
Summary:	weather display applet for Trinity
Group:		Amusements/Graphics

Requires:	trinity-kicker >= %{tde_version}

%description -n trinity-kweather
An applet for the TDE panel that displays your area's current weather.
Information shown includes the temperature, wind speed, air pressure
and more. By pressing a button a full weather report can be obtained.

KWeather also provides a weather service that can track multiple weather
stations and provide this information to other applications, including
Konqueror's sidebar and Kontact's summary page.

This package is part of Trinity, and a component of the TDE toys module.

%files -n trinity-kweather
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{tde_prefix}/bin/kweatherservice
%{tde_prefix}/bin/kweatherreport
%{tde_prefix}/%{_lib}/libtdeinit_kweatherreport.so
%{tde_prefix}/%{_lib}/libtdeinit_kweatherreport.la
%{tde_prefix}/%{_lib}/trinity/kcm_weatherapplet.so
%{tde_prefix}/%{_lib}/trinity/kcm_weatherapplet.la
%{tde_prefix}/%{_lib}/trinity/kcm_weatherservice.so
%{tde_prefix}/%{_lib}/trinity/kcm_weatherservice.la
%{tde_prefix}/%{_lib}/trinity/kcm_weatherstations.so
%{tde_prefix}/%{_lib}/trinity/kcm_weatherstations.la
%{tde_prefix}/%{_lib}/trinity/kweatherreport.so
%{tde_prefix}/%{_lib}/trinity/kweatherreport.la
%{tde_prefix}/%{_lib}/trinity/weather_panelapplet.la
%{tde_prefix}/%{_lib}/trinity/weather_panelapplet.so
%{tde_prefix}/%{_lib}/trinity/weather_sidebar.la
%{tde_prefix}/%{_lib}/trinity/weather_sidebar.so
%{tde_prefix}/share/apps/kicker/applets/kweather.desktop
%{tde_prefix}/share/apps/konqsidebartng/
%{tde_prefix}/share/apps/kweather/
%{tde_prefix}/share/apps/kweatherservice/
%{tde_prefix}/share/icons/hicolor/*/apps/kweather.png
%{tde_prefix}/share/services/kweatherservice.desktop
%{tde_prefix}/share/services/kcmweatherapplet.desktop
%{tde_prefix}/share/services/kcmweatherservice.desktop
%{tde_prefix}/share/services/kcmweatherstations.desktop
%{tde_prefix}/share/doc/tde/HTML/en/kweather/
%{tde_prefix}/share/man/man*/kweatherreport.*
%{tde_prefix}/share/man/man*/kweatherservice.*

##########

%package -n trinity-kworldclock
Summary:	earth watcher for Trinity
Group:		Amusements/Graphics

Requires:	trinity-kdesktop >= %{tde_version}
Requires:	trinity-kicker >= %{tde_version}

%description -n trinity-kworldclock
Displays where in the world it is light and dark depending on time, as
well as offering the time in all of the major cities of the world.
This can be run standalone, as an applet in the TDE panel or as a
desktop background.

Additional kworldclock themes are available in the tdeartwork-misc package.

This package is part of Trinity, and a component of the TDE toys module.

%files -n trinity-kworldclock
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{tde_prefix}/bin/kworldclock
%{tde_prefix}/%{_lib}/trinity/ww_panelapplet.la
%{tde_prefix}/%{_lib}/trinity/ww_panelapplet.so
%{tde_prefix}/share/applications/tde/kworldclock.desktop
%{tde_prefix}/share/apps/kdesktop/programs/kdeworld.desktop
%{tde_prefix}/share/apps/kicker/applets/kwwapplet.desktop
%{tde_prefix}/share/apps/kworldclock/
%{tde_prefix}/share/icons/hicolor/*/apps/kworldclock.png
%{tde_prefix}/share/doc/tde/HTML/en/kworldclock/
%{tde_prefix}/share/man/man*/kworldclock.*

%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"


%install -a
# Useless include file from Amor
%__rm -f %{buildroot}%{tde_prefix}/include/tde/AmorIface.h

